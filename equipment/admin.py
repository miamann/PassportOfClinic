from django.contrib import admin
from .models import MedicalDeviceCardMO,AccountingMDMO,ConsumablesMDMO,DeviceCardMO
# Register your models here.
@admin.register(MedicalDeviceCardMO)
class MedicalDeviceCardMOAdmin(admin.ModelAdmin):
    list_display = ('medDeviceCls', 'inventoryNo', 'subdivision','termMD')

@admin.register(AccountingMDMO)
class AccountingMDMOAdmin(admin.ModelAdmin):
    list_display = ('medicalDeviceCardMO', 'dateInAccounting', 'contractNo','costMDMO')

@admin.register(ConsumablesMDMO)
class ConsumablesMDMOAdmin(admin.ModelAdmin):
    list_display = ('medicalDeviceCardMO', 'consumables', 'other')

@admin.register(DeviceCardMO)
class DeviceCardMOAdmin(admin.ModelAdmin):
    list_display = ('nameDeviceMD', 'modelTransMO', 'inventoryNo')