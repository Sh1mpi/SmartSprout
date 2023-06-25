from django.contrib import admin
from django.urls import path,include
from myapp import views

from myapp.views import CustomLoginView
from myapp.views import SignUpView
from myapp.views import water_plant
from myapp.views import change_plant
from myapp.views import get_current_temperature
from myapp.views import get_temperature_statistics

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('greenhouse_form/', views.greenhouse_form, name='greenhouse_form'),
    path('current-plants/', views.get_current_plants, name='current-plants'),
    path('remove-plant/', views.remove_plant, name='remove-plant'),
    path('water-plant/', water_plant, name='water-plant'),
    path('change-plant/', water_plant, name='change-plant'),
    path('get-compatibility-table/', views.get_compatibility_table, name='get_compatibility_table'),
    path('get_current_temperature/', get_current_temperature, name='get_current_temperature'),
    path('get_temperature_statistics/', get_temperature_statistics, name='get_temperature_statistics'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
