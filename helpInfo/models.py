from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class typeMO(models.Model):
    typeMOName=models.CharField(verbose_name="Тип МО",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.typeMOName

    class Meta:
        verbose_name = 'Тип МО'
        verbose_name_plural = 'Тип МО'
class PlaceForm(models.Model):
    PlaceFormName=models.CharField(verbose_name="Территориальный признак",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.PlaceForm

    class Meta:
        verbose_name = 'Территориальный признак'
        verbose_name_plural = 'Территориальный признак'
class typeAgeMO(models.Model):
    typeAgeMOName=models.CharField(verbose_name="Тип МО по возрасту",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.typeAgeMOName

    class Meta:
        verbose_name = 'Тип МО по возрасту'
        verbose_name_plural = 'Тип МО по возрасту'
class OKFS(models.Model):
    OKFSName=models.CharField(verbose_name="ОКФС – код по классификатору форм собственности",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.OKFSName

    class Meta:
        verbose_name = 'ОКФС – код по классификатору форм собственности'
        verbose_name_plural = 'ОКФС – код по классификатору форм собственности'
class OKOPF(models.Model):
    OKOPFName=models.CharField(verbose_name="ОКОПФ – код по классификатору организационно-правовых форм",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.OKOPFName

    class Meta:
        verbose_name = 'ОКОПФ – код по классификатору организационно-правовых форм'
        verbose_name_plural = 'ОКОПФ – код по классификатору организационно-правовых форм'
class OKPO(models.Model):
    OKPOFName=models.CharField(verbose_name="ОКПО – код по классификатору предприятий и организаций",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.OKPOName

    class Meta:
        verbose_name = "ОКПО – код по классификатору предприятий и организаций"
        verbose_name_plural = "ОКПО – код по классификатору предприятий и организаций"

class OKDP(models.Model):
    OKDPName=models.CharField(verbose_name="ОКДП – код по классификатору продукции",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.OKDPName

    class Meta:
        verbose_name = "ОКДП – код по классификатору продукции"
        verbose_name_plural = "ОКДП – код по классификатору продукции"
class OKVED(models.Model):
    OKVEDName=models.CharField(verbose_name="ОКВЭД – код выбирается из справочника классификатор видов экономической деятельности.",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.OKVEDName

    class Meta:
        verbose_name = "ОКВЭД – код выбирается из справочника классификатор видов экономической деятельности."
        verbose_name_plural = "ОКВЭД – код выбирается из справочника классификатор видов экономической деятельности."
". "

class ONMSZ(models.Model):
    ONMSZName=models.CharField(verbose_name="Код ОНМСЗ – код органа, назначающего меры социальной защиты.",max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ONMSZName

    class Meta:
        verbose_name = "Код ОНМСЗ – код органа, назначающего меры социальной защиты."
        verbose_name_plural = "Код ОНМСЗ – код органа, назначающего меры социальной защиты."

class ORGANITION_FORM(models.Model):
    ORGAN_FORMName=models.CharField(verbose_name="Организационная форма",max_length=60, blank=True, null=True)

    def __str__(self):
        return self.ORGANITION_FORMName

    class Meta:
        verbose_name = "Организационная форма."
        verbose_name_plural = "Организационная форма."

class BuildingMO(models.Model):
    BuildingName=models.CharField(verbose_name="Здания МО",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.BuildingName

    class Meta:
        verbose_name = "Здания МО."
        verbose_name_plural = "Здания МО."

class GovOrg(models.Model):
    GovOrgName=models.CharField(verbose_name="Орган, зарегистрировавший юридическое лицо",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.GovOrgName

    class Meta:
        verbose_name = "Орган, зарегистрировавший юридическое лицо"
        verbose_name_plural = "Орган, зарегистрировавший юридическое лицо"

class Organizion(models.Model):
    OrganizionName=models.CharField(verbose_name="Организация",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.OrganizionName

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

class LevelSub(models.Model):
    levelSubName=models.CharField(verbose_name="Уровень подчиненности",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.levelSubName

    class Meta:
        verbose_name = "Уровень подчиненности"
        verbose_name_plural = "Уровень подчиненности"

class LevelMO(models.Model):
    levelMOName=models.CharField(verbose_name="Уровень МО",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.levelMOName

    class Meta:
        verbose_name = "Уровень МО"
        verbose_name_plural = "Уровень МО"


class FRMOlevelMO(models.Model):
    FRMOlevelMOName=models.CharField(verbose_name="ФРМО. Уровень медицинской организации",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.FRMOlevelMOName

    class Meta:
        verbose_name = "ФРМО. Уровень медицинской организации"
        verbose_name_plural = "ФРМО. Уровень медицинской организации"


class MedService(models.Model):
    medServiceName=models.CharField(verbose_name="Медицинские услуги",max_length=60, blank=True, null=True)
    def __str__(self):
        return self.medServiceName

    class Meta:
        verbose_name = "Медицинские услуги"
        verbose_name_plural = "Медицинские услугии"

class JobTitle(models.Model):
    jobTitle = models.CharField(verbose_name="Должность", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.jobTitle

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"

class MedDeviceKind(models.Model):
    medDeviceKindName = models.CharField(verbose_name="Вид МИ", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.medDeviceKindName

    class Meta:
        verbose_name = "Вид МИ"
        verbose_name_plural = "Вид МИ"

class MedDeviceType(models.Model):
    medDeviceTypeName = models.CharField(verbose_name="Вид МИ", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.medDeviceTypeName

    class Meta:
        verbose_name = "Тип МИ"
        verbose_name_plural = "Тип МИ"

class PotentialRisk(models.Model):
    potenRiskName = models.CharField(verbose_name="Класс потенциального риска применения", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.potenRiskName

    class Meta:
        verbose_name = "Тип МИ"
        verbose_name_plural = "Тип МИ"

class MedDeviceCls(models.Model):
    medDeviceClsName = models.CharField(verbose_name="Наименование МИ", max_length=60, blank=True, null=True)
    medDeviceClsModel = models.CharField(verbose_name="Модель", max_length=60, blank=True, null=True)
    medDeviceType=models.ForeignKey(MedDeviceType,on_delete=models.CASCADE)
    medDeviceKind=models.ForeignKey(MedDeviceKind,on_delete=models.CASCADE)
    potentialRisk=models.ForeignKey(PotentialRisk,on_delete=models.CASCADE)
    medDeviceClsFun = models.CharField(verbose_name="Функциональное назначение", max_length=60, blank=True, null=True)
    medDeviceClsArea = models.CharField(verbose_name="Область применения", max_length=60, blank=True, null=True)
    medDeviceClsScope= models.CharField(verbose_name="Сфера применения", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.medDeviceClsName

    class Meta:
        verbose_name = "Класс медицинского изделия"
        verbose_name_plural = "Класс медицинского изделия"

class State(models.Model):
    stateName = models.CharField(verbose_name="Страна", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.stateName

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class Region(models.Model):
    regionName = models.CharField(verbose_name="Область", max_length=60, blank=True, null=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    def __str__(self):
        return self.regionName

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"

class District(models.Model):
    districtName = models.CharField(verbose_name="Область", max_length=60, blank=True, null=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.districtName

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Район"

class City(models.Model):
    cityName = models.CharField(verbose_name="Область", max_length=60, blank=True, null=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.cityName

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Город"

class Settlement(models.Model):
    class Answer(models.IntegerChoices):
        ANAL = 0, _("Городской")
        DIGIT = 1, _("Сельский")
        __empty__ = _("(Пусто)")
    SettlementName = models.CharField(verbose_name="Область", max_length=60, blank=True, null=True)
    settlementType=models.IntegerField(choices=Answer.choices, default=Answer.DIGIT,
                        verbose_name='Тип населенного пункта')
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.SettlementName

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенный пункт"