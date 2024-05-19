from django.contrib import admin
from .models import passportMO,identificationMO,OmsMO,LloMO,DmsMO,UchasSlujbaMO

# from .models import typeMO,typeAgeMO,OKOPF,OKDP,OKFS,OKPO,OKVED,ONMSZ,ORGANITION_FORM,GovOrg,BuildingMO,PlaceForm

@admin.register(passportMO)
class PassportMOAdmin(admin.ModelAdmin):
    list_display = ('nameMO', 'shortNameMO', 'codeOUZS')


@admin.register(identificationMO)
class identificationMOAdmin(admin.ModelAdmin):
    list_display = ('nameMOLVN', 'addressMOLVN', 'phoneMO')
    # search_fields = ('name',)
    # list_filter = (JenreFilter,)

@admin.register(UchasSlujbaMO)
class UchasSlujbaMOAdmin(admin.ModelAdmin):
    list_display = ('inDate', 'outDate', 'typeUshastok')

@admin.register(OmsMO)
class OmsMOAdmin(admin.ModelAdmin):
    list_display = ('inDate', 'outDate', 'dogovNo')


@admin.register(LloMO)
class LloMOAdmin(admin.ModelAdmin):
    list_display = ('inDate', 'outDate')

@admin.register(DmsMO)
class DmsMOAdmin(admin.ModelAdmin):
    list_display = ('inDate', 'outDate', 'dogovNo')


