from django.db import models
from passport.models import passportMO
from  helpInfo.models import State,District,City,Region,Settlement

# Create your models here.

class PacsMO(models.Model):
    namePacsMO= models.CharField(verbose_name="Наименование", max_length=25,blank=True, null=True)
    modelPacsMO = models.CharField(verbose_name="Модель", max_length=25, blank=True, null=True)
    inventoryPacsMO = models.CharField(verbose_name="инвентарный номер", max_length=25, blank=True, null=True)
    passportMO = models.OneToOneField(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.namePacsMO

    class Meta:
        verbose_name = 'PACS'
        verbose_name_plural = 'PACS'


class TransportMO(models.Model):
    nameTransMO= models.CharField(verbose_name="Наименование", max_length=25,blank=True, null=True)
    modelConsMO = models.CharField(verbose_name="Производитель", max_length=25, blank=True, null=True)
    modelTransMO = models.CharField(verbose_name="Модель", max_length=25, blank=True, null=True)
    dateCons = models.DateField(verbose_name="Дата выпуска", blank=True, null=True)
    dateBuy = models.DateField(verbose_name='Дата приобретения', blank=True, null=True)
    consumerMD = models.CharField(verbose_name="Поставщик", max_length=25, blank=True, null=True)
    regNoMO = models.CharField(verbose_name="Регистрационный номер", max_length=16, blank=True, null=True)
    driveNoMD = models.CharField(verbose_name="Номер двигателя", max_length=14, blank=True,
                               null=True)
    dateUse = models.DateField(verbose_name="Дата ввода в эксплуатацию", blank=True, null=True)
    costTransMO = models.DecimalField(verbose_name="Стоимость приобретения", max_digits=10, decimal_places=2, blank=True,
                                   null=True)
    costLastMO = models.DecimalField(verbose_name="Остаточная стоимость", max_digits=10, decimal_places=2, blank=True,
                                   null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameTransMO

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

class PopulationServedMO(models.Model):

    territoryMO= models.CharField(verbose_name="Территория", max_length=25,blank=True, null=True)
    districtMO = models.ForeignKey(District,on_delete=models.CASCADE,verbose_name="Район", blank=True, null=True)
    cityMO = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="Город", blank=True, null=True)
    settlementMO = models.ForeignKey(Settlement, on_delete=models.CASCADE,verbose_name="Населенный пункт", blank=True, null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.settlementMO.settlementType+' '+self.settlementMO.SettlementName

    class Meta:
        verbose_name = 'Обслуживаемое население'
        verbose_name_plural = 'Обслуживаемое население'

