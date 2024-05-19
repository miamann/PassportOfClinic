from django.contrib import admin
from .models import (typeMO,typeAgeMO,OKOPF,OKDP,OKFS,OKPO,OKVED,ONMSZ,ORGANITION_FORM,
                     GovOrg,BuildingMO,PlaceForm,JobTitle,State,Settlement,District,Region,City)


admin.site.register(typeMO)
admin.site.register(typeAgeMO)
admin.site.register(OKOPF)
admin.site.register(OKDP)
admin.site.register(OKFS)
admin.site.register(OKPO)
admin.site.register(OKVED)
admin.site.register(ORGANITION_FORM)
admin.site.register(GovOrg)
admin.site.register(BuildingMO)
admin.site.register(ONMSZ)
admin.site.register(PlaceForm)
admin.site.register(JobTitle)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Settlement)
admin.site.register(City)

class PlaceFormAdmin(admin.TabularInline):
    model= PlaceForm

class TypeMOAdmin(admin.TabularInline):
    model=typeMO

class TypeAgeMOAdmin(admin.TabularInline):
    model=typeAgeMO

class OKOPFAdmin(admin.TabularInline):
    model=OKOPF

class OKDPAdmin(admin.TabularInline):
    model=OKDP

class OKFSAdmin(admin.TabularInline):
    model=OKFS

class OKPOAdmin(admin.TabularInline):
    model=OKPO

class OKVEDAdmin(admin.TabularInline):
    model=OKVED

class ONMSZAdmin(admin.TabularInline):
    model=ONMSZ

class ORGANITION_FORMAdmin(admin.TabularInline):
    model=ORGANITION_FORM

class GovOrgAdmin(admin.TabularInline):
    model=GovOrg

class BuildingMOAdmin(admin.TabularInline):
    model=BuildingMO

class JobTitleAdmin(admin.TabularInline):
    model=JobTitle
# Register your models here.

class StateAdmin(admin.TabularInline):
    model=State

class CityAdmin(admin.TabularInline):
    model=City

class SettlementAdmin(admin.TabularInline):
    model=Settlement

class DistrictAdmin(admin.TabularInline):
    model=District

class RegionAdmin(admin.TabularInline):
    model=Region