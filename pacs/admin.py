from django.contrib import admin
from .models import PacsMO,TransportMO,PopulationServedMO
# Register your models here.
@admin.register(PacsMO)
class PacsMOAdmin(admin.ModelAdmin):
    list_display = ('namePacsMO', 'modelPacsMO', 'inventoryPacsMO')

@admin.register(TransportMO)
class TransportMOAdmin(admin.ModelAdmin):
    list_display = ('nameTransMO', 'modelTransMO', 'regNoMO','costLastMO')

@admin.register(PopulationServedMO)
class PopulationServedMOAdmin(admin.ModelAdmin):
    list_display = ('territoryMO', 'districtMO', 'cityMO','settlementMO')