from django.db import models
from django.contrib.auth.models import User

class Greenhouse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rows = models.PositiveIntegerField()
    row_length = models.FloatField()
    class Meta:
        verbose_name = 'Размеры теплицы'
        verbose_name_plural = 'Размеры теплицы'

class InGreenhouse(models.Model):
    # поля для таблицы "То что сейчас в теплице растет"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE)
    cell = models.CharField(max_length=255)
    planting_date = models.DateTimeField()

    class Meta:
        verbose_name = 'То что сейчас в теплице растет'
        verbose_name_plural = 'То что сейчас в теплице растет'

class Compatibility(models.Model):
    # поля для таблицы "Таблица совместимости"
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='compatibilities')
    compatible_with = models.ManyToManyField('Plant', related_name='compatible_plants', blank=True)
    incompatible_with = models.ManyToManyField('Plant', related_name='incompatible_plants', blank=True)

    class Meta:
        verbose_name = 'Таблица совместимости'
        verbose_name_plural = 'Таблицы совместимости'

class Plant(models.Model):
    # поля для таблицы "Растения"
    name = models.CharField(max_length=255)
    time = models.IntegerField()
    image = models.ImageField(upload_to='plants/',null=True, blank=True) 

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.name

class PlantType(models.Model):
    plant_type = models.ForeignKey('Plant', on_delete=models.CASCADE)

class Temperature(models.Model):
    # поля для таблицы "Температура"
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температура'

class PlantCare(models.Model):
    # поля для таблицы "Уход за растениями"
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE)
    care_instructions = models.TextField()

    class Meta:
        verbose_name = 'Уход за растением'
        verbose_name_plural = 'Уход за растениями'
