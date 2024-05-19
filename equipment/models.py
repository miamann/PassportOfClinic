from django.utils.translation import gettext_lazy as _
from django.db import models
from passport.models import passportMO
from infoHelps.models import BranchesMO
from helpInfo.models import MedDeviceCls,Organizion

# Create your models here.

class MedicalDeviceCardMO(models.Model):
    class Answer(models.IntegerChoices):
        ANAL = 0, _("Аналоговый")
        DIGIT= 1, _("Цифровой")
        __empty__ = _("(Пусто)")
    medDeviceCls=models.ForeignKey(MedDeviceCls,on_delete=models.CASCADE)
    inventoryNo = models.CharField(verbose_name="Инвентарный номер", max_length=10, blank=True, null=True)
    serialNo = models.CharField(verbose_name="Серийный номер", max_length=10, blank=True, null=True)
    regNo = models.CharField(verbose_name="Регистрационный знак (для автомобилей)", max_length=10, blank=True, null=True)
    boardNo = models.CharField(verbose_name="Бортовой номер", max_length=10, blank=True,
                             null=True)
    phone = models.CharField(verbose_name="Телефон", max_length=14, blank=True,
                             null=True)
    subdivision = models.ForeignKey(BranchesMO, verbose_name="Подразделение", blank=True,
                             null=True,on_delete=models.CASCADE)
    suppliers = models.ForeignKey(Organizion, verbose_name="Поставщик", blank=True,
                             null=True,on_delete=models.CASCADE)
    dateIssue=models.DateField(verbose_name="Дата выпуска",blank=True, null=True)
    termMD=models.IntegerField(verbose_name="Срок использования",blank=True, null=True)
    principleMD = models.IntegerField(choices=Answer.choices, default=Answer.DIGIT,
                               verbose_name='Принцип работы')
    dateReg = models.DateField(verbose_name="Дата регистрационного удостоверения", blank=True, null=True)
    dateOutRegMD = models.DateFieldField(verbose_name='Срок действия рег. удостоверения')
    regNoMD = models.CharField(verbose_name="Номер регистрационного удостоверения", max_length=14, blank=True,
                             null=True)
    orderNoMD = models.CharField(verbose_name="Номер приказа о регистрации медицинского изделия", max_length=14, blank=True,
                             null=True)
    nameRegMD = models.CharField(verbose_name="Наименование МИ по регистрационным документам", max_length=14, blank=True,
                             null=True)
    holderIDMD = models.CharField(verbose_name="Держатель удостоверения", max_length=14, blank=True,
                             null=True)
    declarantMD = models.CharField(verbose_name="Декларант в таможенном учреждении", max_length=14, blank=True,
                             null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.medDeviceCls.medDeviceClsName,self.medDeviceCls.medDeviceClsModel)

    class Meta:
        verbose_name = 'Карточка медицинского изделия'
        verbose_name_plural = 'Карточка медицинского изделия'

class ConsumablesMDMO(models.Model):
    consumables = models.TextField(verbose_name="Комплектация", max_length=10, blank=True, null=True)
    other = models.CharField(verbose_name="Регистрационный знак (для автомобилей)", max_length=10, blank=True, null=True)
    medicalDeviceCardMO = models.ForeignKey(MedicalDeviceCardMO, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.consumables[:10])

    class Meta:
        verbose_name = 'Комплектация/Расходные материалы'
        verbose_name_plural = 'Комплектация/Расходные материалы'


class AccountingMDMO(models.Model):
    dateBuy = models.DateField(verbose_name="Дата приобретения", blank=True, null=True)
    dateExplotion = models.DateField(verbose_name="Дата ввода в эксплуатацию", blank=True, null=True)
    dateInAccounting = models.DateField(verbose_name="Дата принятия на учет", blank=True, null=True)
    dateOutAccounting = models.DateField(verbose_name="Дата списания с учета", blank=True, null=True)
    contractNo = models.CharField(verbose_name="Номер гос. контракта ", max_length=10, blank=True, null=True)
    dateContract = models.DateField(verbose_name="Дата заключения контракта ", blank=True, null=True)
    costMDMO = models.DecimalField(verbose_name="Стоимость приобретения", max_digits=10,decimal_places=2, blank=True, null=True)
    priceMDMO = models.DecimalField(verbose_name="Цена производителя", max_digits=10,decimal_places=2, blank=True, null=True)
    consumeTypeNo = models.CharField(verbose_name="Тип поставки", max_length=10, blank=True, null=True)
    ownerTypeNo = models.CharField(verbose_name="Форма владения", max_length=10, blank=True, null=True)
    medicalDeviceCardMO = models.ForeignKey(MedicalDeviceCardMO, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.medDeviceCls.medDeviceClsName,self.medDeviceCls.medDeviceClsModel,self.costMDMO)

    class Meta:
        verbose_name = 'Бухгалтерский учет медицинского изделия'
        verbose_name_plural = 'Бухгалтерский учет медицинского изделия'


class DeviceCardMO(models.Model):
    nameDeviceMD = models.CharField(verbose_name="Наименование ", max_length=50,
                                    blank=True,null=True)
    suppliers=models.CharField(verbose_name="Производитель", max_length=50, blank=True,
                                     null=True)
    dateIssue = models.DateField(verbose_name="Дата выпуска", blank=True, null=True)
    dateBuy = models.DateField(verbose_name='Дата приобретения', blank=True, null=True)
    modelTransMO = models.CharField(verbose_name="Модель", max_length=25, blank=True, null=True)
    inventoryNo = models.CharField(verbose_name="Инвентарный номер", max_length=10, blank=True, null=True)
    serialNo = models.CharField(verbose_name="Серийный номер", max_length=10, blank=True, null=True)
    dateUse = models.DateField(verbose_name="Дата ввода в эксплуатацию", blank=True, null=True)
    amontNo = models.DecimalField(verbose_name="% износа", max_length=10, blank=True, null=True)
    dateReg = models.DateField(verbose_name="Дата заключения о пригодности аппарата", blank=True, null=True)
    costTransMO = models.DecimalField(verbose_name="Стоимость приобретения", max_digits=10, decimal_places=2,
                                      blank=True, null=True)
    costLastMO = models.DecimalField(verbose_name="Остаточная стоимость", max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameDeviceMD

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'