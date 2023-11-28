from django.contrib import admin
from myapp.models import Greenhouse, InGreenhouse, Compatibility, Plant, Temperature, PlantCare
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

class GreenhouseAdmin(ImportExportModelAdmin): 
    list_display = ['user', 'rows', 'row_length']
    list_filter = ['user']
    search_fields = ['user__username']

class InGreenhouseAdmin(SimpleHistoryAdmin, ImportExportModelAdmin): 
    list_display = ['user', 'plant', 'cell', 'planting_date', 'history']
    list_display_links = ['user']
    date_hierarchy = 'planting_date'
    list_filter = ['user', 'plant']
    raw_id_fields = ['user', 'plant']
    search_fields = ['user__username', 'plant__name']
    readonly_fields = ['cell']

    def history(self, obj):
        
        history_records = obj.history.all()
       
        history_info = [
            f'{record.history_date}: {record.history_type}'  
            for record in history_records
        ]
        return format_html('<br>'.join(history_info))

    history.short_description = 'History'
    history.allow_tags = True

class CompatibilityAdmin(ImportExportModelAdmin):  
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

class PlantAdmin(ImportExportModelAdmin):  
    list_display = ['name', 'time', 'image']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['time']

class TemperatureAdmin(ImportExportModelAdmin): 
    list_display = ['user', 'temperature', 'time']
    date_hierarchy = 'time'
    readonly_fields = ['time']

class PlantCareAdmin(ImportExportModelAdmin): 
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
