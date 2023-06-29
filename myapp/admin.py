from django.contrib import admin
from myapp.models import Greenhouse, InGreenhouse, Compatibility, Plant, Temperature, PlantCare

class GreenhouseAdmin(admin.ModelAdmin):
    list_display = ['user', 'rows', 'row_length']

class InGreenhouseAdmin(admin.ModelAdmin):
    list_display = ['user', 'plant', 'cell', 'planting_date']
    date_hierarchy = 'planting_date'

class CompatibilityAdmin(admin.ModelAdmin):
    list_display = ['plant']
    filter_horizontal = ['compatible_with', 'incompatible_with']

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'image']

class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'time']

class PlantCareAdmin(admin.ModelAdmin):
    list_display = ['plant', 'care_instructions']

admin.site.register(Greenhouse, GreenhouseAdmin)
admin.site.register(InGreenhouse, InGreenhouseAdmin)
admin.site.register(Compatibility, CompatibilityAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(PlantCare, PlantCareAdmin)
