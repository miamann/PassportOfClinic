from django.contrib import admin
from .models import (helpIndosMO, LicensesMO,CurrentAccountMO,ISMO,spesMO,ServiceMO,TechsMO,
                     SecondServicesMO,BranchesMO,HeadsMO)
# Register your models here.
@admin.register(helpIndosMO)
class helpIndosMOAdmin(admin.ModelAdmin):
    list_display = ('levelSub', 'levelMO', 'capitalEquipment','capitalLabor')


@admin.register(LicensesMO)
class LicensesMOAdmin(admin.ModelAdmin):
    list_display = ('licensesNoMO', 'issueDate', 'regNoMO','inDate','outDate')


@admin.register(CurrentAccountMO)
class CurrentAccountMOAdmin(admin.ModelAdmin):
    list_display = ('currentAccountMOName', 'currentAccountMOBank', 'accountNoMO')


@admin.register(ISMO)
class ISMOAdmin(admin.ModelAdmin):
    list_display = ('nameISMO', 'typeISMOName', 'developerISMO','inDateISMO')


@admin.register(spesMO)
class spesMOAdmin(admin.ModelAdmin):
    list_display = ('codeProfileMO', 'profileMOName', 'licenseNoMO','beAAfterCareMO')


@admin.register(ServiceMO)
class ServiceMOAdmin(admin.ModelAdmin):
    list_display = ('serviceMOName', 'licenseNoMO')


@admin.register(TechsMO)
class TechsMOAdmin(admin.ModelAdmin):
    list_display = ('techMOName', 'classTechMO')


@admin.register(SecondServicesMO)
class SecondServicesMOAdmin(admin.ModelAdmin):
    list_display = ('secondServicesMOCode', 'secondServicesMOName', 'inDate')


@admin.register(BranchesMO)
class BranchesMOAdmin(admin.ModelAdmin):
    list_display = ('branchesMOCode', 'branchesMOshortName', 'inDate')

@admin.register(HeadsMO)
class HeadsMOAdmin(admin.ModelAdmin):
    list_display = ('user', 'titleMO', 'phoneHeadMO','emailHeadMO')

