from django.shortcuts import render, redirect
from .models import InGreenhouse, Compatibility, Plant, Temperature, PlantCare, Greenhouse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import PlantForm, GreenhouseForm,InGreenhouseForm
from .forms import UserRegistrationForm
from .forms import UserLoginForm
import json
from random import uniform
from datetime import timedelta



class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

@login_required
def home(request):
    user = request.user
    try:
        greenhouse = Greenhouse.objects.get(user=user)
        in_greenhouse = InGreenhouse.objects.filter(user=user)  # Извлекаем все записи для данного пользователя

        plant_data = {plant.pk: {'name': plant.name, 'image': plant.image.url, 'time': plant.time} for plant in Plant.objects.all()}
        in_greenhouse_json = serialize('json', in_greenhouse)  # сериализуем объекты in_greenhouse
        care_instructions = PlantCare.objects.all()  # Извлекаем все записи об уходе за растениями
        care_instructions_json = serialize('json', care_instructions)  # Сериализуем их в JSON

        if request.method == 'POST':
            form = InGreenhouseForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.planting_date = timezone.now()
                existing_entries = InGreenhouse.objects.filter(user=user, cell=instance.cell)

                # Удалить все существующие записи для этой ячейки
                if existing_entries.exists():
                    existing_entries.delete()

                # Затем сохраните новый экземпляр
                instance.save()

        form = InGreenhouseForm()
        context = {
            'form_in_greenhouse': form,
            'rows': greenhouse.rows,
            'row_length': greenhouse.row_length,
            'plant_data': json.dumps(plant_data), # передаем словарь с изображениями растений
            'in_greenhouse_json': in_greenhouse_json,  # передаем сериализованный объект in_greenhouse
            'care_instructions_json': care_instructions_json,  # передаем сериализованный объект care_instructions
        }
        return render(request, 'index.html', context)
    except Greenhouse.DoesNotExist:
        return redirect('greenhouse_form')



@login_required
def get_current_plants(request):
    user = request.user
    records = InGreenhouse.objects.filter(user=user).values()

    records_list = list(records)

    return JsonResponse(records_list, safe=False)




@login_required
def greenhouse_form(request):
    if request.method == 'POST':
        form = GreenhouseForm(request.POST)
        if form.is_valid():
            greenhouse = form.save(commit=False)
            greenhouse.user = request.user
            greenhouse.save()
            return redirect('index')
    else:
        form = GreenhouseForm()
    return render(request, 'greenhouse_form.html', {'form': form})

@csrf_exempt
def change_plant(request):
    if request.method == 'POST':
        # Получить ID ячейки из запроса
        cell_id = request.POST.get('cell')
        # Получить ID растения из запроса
        plant_id = request.POST.get('plant')
        
        try:
            # Найти запись в базе данных с данным ID ячейки
            in_greenhouse = InGreenhouse.objects.get(cell=cell_id)
            # Обновить ID растения в этой записи
            in_greenhouse.plant_id = plant_id
            # Сохранить изменения в базе данных
            in_greenhouse.save()

            return JsonResponse({'status': 'success'}, status=200)
        except InGreenhouse.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Plant not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@login_required
def water_plant(request):
    if request.method == 'POST':
        cell_id = request.POST.get('cell')
        ingreenhouse = InGreenhouse.objects.filter(user=request.user, cell=cell_id).order_by('-planting_date').first()
        if ingreenhouse:
            ingreenhouse.planting_date = timezone.now()
            ingreenhouse.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "error"}, status=400)

@csrf_exempt
def remove_plant(request):
    if request.method == 'POST':
        cell_id = request.POST.get('cell')
        plants = InGreenhouse.objects.filter(cell=cell_id)
        if plants:
            plants.delete()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "failure", "error": "Plant does not exist"})
    else:
        return JsonResponse({"status": "failure", "error": "Invalid request method"})
    
def get_compatibility_table(request):
    data = Compatibility.objects.all()
    context = {
        'data': data
    }
    return render(request, 'compatibility_table.html', context)

def get_current_temperature(request):
    # Сгенерировать случайное число от 20 до 30 и сохранить в базе данных
    current_temperature = round(uniform(20, 30), 1)
    
    maintain_temperature_records()

    temperature_data = Temperature(temperature=current_temperature)
    temperature_data.save()

    # Удалить записи, которые старше 24 часов
    old_records = Temperature.objects.filter(time__lte=timezone.now() - timedelta(hours=24))
    old_records.delete()

    return JsonResponse({"temperature": current_temperature})

@csrf_exempt
def get_temperature_statistics(request):
    last_24_records = Temperature.objects.order_by('-time')[:24]
    temperatures = list(last_24_records.values('temperature', 'time'))
    return JsonResponse(temperatures, safe=False)

def maintain_temperature_records():
    # Получение всех записей о температуре, отсортированных по времени создания
    temperature_records = Temperature.objects.order_by('time')

    # Проверка количества записей
    if temperature_records.count() > 24:
        # Удаление самой старой записи
        temperature_records.first().delete()
