from django.db import models
from passport.models import passportMO
# Create your models here.
class BuildingMO(models.Model):

    fencingBuildMO = models.BooleanField(verbose_name="Ограждение территории", default=True)
    bodyguardMO = models.BooleanField(verbose_name="Наличие охраны", default=True)
    metalDoorMO = models.BooleanField(verbose_name="Наличие металлических входных дверей в здание", default=True)
    videoSurvMO = models.BooleanField(verbose_name="Видеонаблюдение территорий и помещений для здания", default=True)
    accommodationMO = models.BooleanField(verbose_name="Проживание сопровождающих лиц", default=False)
    forDisabilitiesMO = models.BooleanField(verbose_name="Приспособленность территории для пациентов с ограниченными возможностями", default=True)
    latitudeMO = models.DecimalField(verbose_name="Координаты: Широта",max_digits=4,decimal_places=2)
    longitudeMO = models.DecimalField(verbose_name="Координаты: Долгота", max_digits=4, decimal_places=2)

    bldgMOName = models.CharField(verbose_name="Общепринятое наименование корпуса", max_length=80, blank=True,
                                       null=True)
    bldgNoMO = models.CharField(verbose_name="Номер корпуса", max_length=16, blank=True,
                                    null=True)
    bldgTypeMO = models.CharField(verbose_name="тип лечебного корпуса", max_length=16, blank=True,
                                    null=True)
    bldgPurposeMO = models.CharField(verbose_name="назначение здания", max_length=16, blank=True,
                                    null=True)
    bldgYearMO = models.IntegerField(verbose_name="Год постройки ", blank=True,     null=True)
    bldgSquareMO = models.DecimalField(verbose_name="Общая площадь", max_digits=6, decimal_places=2,                                  null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.bldgMOName


    class Meta:
        verbose_name = 'Здание МО'
        verbose_name_plural = 'Здания МО'

class InfrastructureMO(models.Model):

    infrastructureName = models.CharField(verbose_name="Наименование объекта", max_length=80, blank=True,
                                       null=True)
    infrastructureCountMO = models.IntegerField(verbose_name="Количество объектов", blank=True,
                                    null=True)
    infrastructureNoMO = models.CharField(verbose_name="Идентификатор участка", max_length=16, blank=True,
                                    null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.infrastructureName


    class Meta:
        verbose_name = 'Объекты инфраструктуры'
        verbose_name_plural = 'Объекты инфраструктуры'