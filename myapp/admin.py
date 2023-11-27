from django.contrib import admin
from myapp.models import Greenhouse, InGreenhouse, Compatibility, Plant, Temperature, PlantCare

class GreenhouseAdmin(admin.ModelAdmin):
    list_display = ['user', 'rows', 'row_length']
    list_filter = ['user']
    search_fields = ['user__username']

class InGreenhouseAdmin(admin.ModelAdmin):
    list_display = ['user', 'plant', 'cell', 'planting_date']
    list_display_links = ['user']
    date_hierarchy = 'planting_date'
    list_filter = ['user', 'plant']
    raw_id_fields = ['user', 'plant']
    search_fields = ['user__username', 'plant__name']
    readonly_fields = ['cell']

class CompatibilityAdmin(admin.ModelAdmin):
    list_display = ['plant', 'compatible_with_list', 'incompatible_with_list']
    filter_horizontal = ['compatible_with', 'incompatible_with']
    list_filter = ['plant']
    raw_id_fields = ['plant']
    search_fields = ['plant__name']
    
    def compatible_with_list(self, obj):
        return ", ".join([p.name for p in obj.compatible_with.all()])
    compatible_with_list.short_description = "Compatible Plants"
    
    def incompatible_with_list(self, obj):
        return ", ".join([p.name for p in obj.incompatible_with.all()])
    incompatible_with_list.short_description = "Incompatible Plants"

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'image']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['time']

class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'time']
    date_hierarchy = 'time'
    readonly_fields = ['time']

class PlantCareAdmin(admin.ModelAdmin):
    list_display = ['plant', 'care_instructions']
    list_filter = ['plant']
    raw_id_fields = ['plant']
    search_fields = ['plant__name', 'care_instructions']

admin.site.register(Greenhouse, GreenhouseAdmin)
admin.site.register(InGreenhouse, InGreenhouseAdmin)
admin.site.register(Compatibility, CompatibilityAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Temperature, TemperatureAdmin)
admin.site.register(PlantCare, PlantCareAdmin)