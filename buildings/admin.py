from django.contrib import admin
from .models import BuildingMO,InfrastructureMO
# Register your models here.



@admin.register(BuildingMO)
class BuildingMOAdmin(admin.ModelAdmin):
    list_display = ('bldgMOName', 'bldgNoMO', 'bldgTypeMO','bldgPurposeMO','bldgSquareMO')

    @admin.register(InfrastructureMO)
    class InfrastructureMOAdmin(admin.ModelAdmin):
        list_display = ('infrastructureName', 'infrastructureCountMO', 'infrastructureNoMO')