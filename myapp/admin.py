from django.contrib import admin
from myapp.models import InGreenhouse,Compatibility,Plant,Temperature,PlantCare

# Register your models here.
admin.site.register(InGreenhouse)
admin.site.register(Compatibility)
admin.site.register(Plant)
admin.site.register(Temperature)
admin.site.register(PlantCare)
