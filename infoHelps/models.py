from django.utils.translation import gettext_lazy as _
from django.db import models
from passport.models import passportMO
from buildings.models import BuildingMO
from helpInfo.models import LevelSub,LevelMO,FRMOlevelMO,Organizion,MedService,JobTitle
from account.models import User
# Create your models here.


class helpIndosMO(models.Model):
    class LevelInNet(models.TextChoices):
        BASE = "BASE", _("основное"),
        SUB= "SUB", _("подчиненное")

    levelSub= models.ForeignKey(LevelSub, verbose_name="Уровень подчиненности", on_delete=models.CASCADE)
    levelMO= models.ForeignKey(LevelMO, verbose_name="Уровень МО", on_delete=models.CASCADE)
    FRMOlevelMO = models.ForeignKey(FRMOlevelMO, verbose_name="ФРМО. Уровень МО", on_delete=models.CASCADE)
    countVisit = models.IntegerField(verbose_name="Посещений в смену",  blank=True, null=True)
    countBed = models.IntegerField(verbose_name="Число коек", blank=True, null=True)
    levelInNet = models.CharField(max_length=4, choices=LevelInNet.choices, default=LevelInNet.BASE,
                               verbose_name='Уровень учреждения в иерархии сети')
    lab = models.BooleanField(verbose_name='Организация является внешней лабораторией?',default=False)
    capitalEquipment = models.DecimalField(verbose_name="Фондооснащенность на 1 кв.м (сом.)", max_digits=6, decimal_places=2,blank=True, null=True)
    capitalLabor = models.DecimalField(verbose_name="Фондовооруженность на 1 врача (сом.)", max_digits=6, decimal_places=2,  blank=True, null=True)
    organizion = models.ForeignKey(Organizion, verbose_name="Головное учреждение",on_delete=models.CASCADE)
    mustVisit = models.IntegerField(verbose_name="Количество обращений", blank=True, null=True)
    dayVisit = models.IntegerField(verbose_name="за количество дней для включения в регистр", blank=True, null=True)
    dayOutVisit = models.IntegerField(verbose_name="Дней без обращений для снятия статуса", blank=True, null=True)
    passportMO = models.OneToOneField(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.levelInNet

    class Meta:
        verbose_name = 'Справочная информация'
        verbose_name_plural = 'Справочная информация'



class LicensesMO(models.Model):
    licensesNoMO = models.CharField(verbose_name="Номер лицензии", max_length=16, blank=True,
                                       null=True)
    issueDate = models.DateField(verbose_name="Дата выдачи", auto_now=False, auto_now_add=False)
    regNoMO = models.CharField(verbose_name="Регистрационный номер", max_length=16, blank=True,
                                    null=True)
    inDate = models.DateField(verbose_name="Начало действия", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Окончание действия", auto_now=False, auto_now_add=False)
    kindActivity=models.CharField(verbose_name="Вид деятельности", max_length=16, blank=True,
                                    null=True)
    organizion=models.ForeignKey(Organizion,on_delete=models.CASCADE,verbose_name="Выдавшая организация", blank=True,
                                    null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.licensesNoMO

    class Meta:
        verbose_name = 'Лицензии МО'
        verbose_name_plural = 'Лицензии МО'

class CurrentAccountMO(models.Model):
    currentAccountMOName = models.CharField(verbose_name="Наименование", max_length=50, blank=True,
                                       null=True)
    currentAccountMOBank = models.CharField(verbose_name="Банк", max_length=80, blank=True,
                                       null=True)
    accountNoMO = models.CharField(verbose_name="Номер счета", max_length=16, blank=True,
                                    null=True)
    inDate = models.DateField(verbose_name="Дата открытия", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата закрытия", auto_now=False, auto_now_add=False)
    valuta=models.CharField(verbose_name="Валюта", max_length=8, blank=True,
                                    null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)
    def __str__(self):
        return self.currentAccountMOName


    class Meta:
        verbose_name = 'Расчетный счет'
        verbose_name_plural = 'Расчетный счет'

class ISMO(models.Model):

    class Answer(models.IntegerChoices):
        NO = 0, _("Нет")
        YES = 1, _("Да")
        __empty__ = _("(Пусто)")

    nameISMO = models.CharField(verbose_name="Наименование", max_length=50, blank=True,
                                       null=True)
    typeISMOName = models.CharField(verbose_name="Тип ИС", max_length=50, blank=True,
                                null=True)
    developerISMO = models.CharField(verbose_name="Наименование разработчика", max_length=80, blank=True,
                                       null=True)
    inDateISMO = models.DateField(verbose_name="Дата внедрения", auto_now=False, auto_now_add=False)
    costISMO = models.DecimalField(verbose_name="Стоимость ИС", max_digits=6,
                                       decimal_places=2, blank=True, null=True)
    escortISMO = models.IntegerField(verbose_name="Признак сопровождения", choices=Answer.choices,default=Answer.YES)
    costEscortISMO = models.DecimalField(verbose_name="Стоимость сопровождения", max_digits=6,
                                    decimal_places=2, blank=True, null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)
    def __str__(self):
        return self.nameISMO


    class Meta:
        verbose_name = 'Информационная система'
        verbose_name_plural = 'Информационная система'

class spesMO(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, _("Нет")
        YES = 1, _("Да")
        __empty__ = _("(Пусто)")

    codeProfileMO = models.CharField(verbose_name="Код медицинского профиля.", max_length=16, blank=True,
                                       null=True)
    profileMOName = models.CharField(verbose_name="Медицинский профиль.", max_length=50, blank=True,
                                null=True)
    licenseNoMO = models.CharField(verbose_name="Номер лицензии", max_length=80, blank=True,
                                       null=True)
    beAAfterCareMO = models.IntegerField(verbose_name="Наличие отделения долечивания", choices=Answer.choices,default=Answer.YES)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.profileMOName


    class Meta:
        verbose_name = 'Специализация организации'
        verbose_name_plural = 'Специализация организации'


class ServiceMO(models.Model):
    serviceMOName = models.ForeignKey(MedService,verbose_name="Медицинские услуги",on_delete=models.CASCADE)
    licenseNoMO = models.CharField(verbose_name="Номер лицензии на услугу", max_length=16, blank=True,
                                       null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)
    def __str__(self):
        return self.serviceMOName

    class Meta:
        verbose_name = 'Медицинские услуги'
        verbose_name_plural = 'Медицинские услуги'


class TechsMO(models.Model):

    techMOName = models.CharField(verbose_name="Медицинские технологии",max_length=50, blank=True,
                                null=True)
    classTechMO = models.CharField(verbose_name="Класс технологии", max_length=16, blank=True,
                                       null=True)
    buildingMO = models.ForeignKey(BuildingMO,verbose_name="Идентификатор здания", blank=True,
                                       null=True,on_delete=models.CASCADE)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)
    def __str__(self):
        return self.techMOName

    class Meta:
        verbose_name = 'Медицинские технологии'
        verbose_name_plural = 'Медицинские технологии'




class SecondServicesMO(models.Model):
    secondServicesMOCode=models.CharField(verbose_name="Код услуги", max_length=16, blank=True,
                                       null=True)
    secondServicesMOName=models.CharField(verbose_name="Наименование услуги", max_length=50, blank=True,
                                       null=True)
    inDate = models.DateField(verbose_name="Дата начала оказания услуги", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата окончания оказания услуги", auto_now=False, auto_now_add=False)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)


    def __str__(self):
        return self.secondServicesMOName

    class Meta:
        verbose_name = 'Направления оказания медицинской помощи'
        verbose_name_plural = 'Направления оказания медицинской помощи'

class BranchesMO(models.Model):
    branchesMOCode=models.CharField(verbose_name="Код филиала", max_length=16, blank=True,
                                       null=True)
    branchesMOName=models.CharField(verbose_name="Полного наименования филиала МО", max_length=50, blank=True,
                                       null=True)
    branchesMOshortName=models.CharField(verbose_name="Краткое наименование филиала МО", max_length=50, blank=True,
                                       null=True)

    inDate = models.DateField(verbose_name="Даты начала действия филиала", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Даты окончания действия филиала", auto_now=False, auto_now_add=False)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)


    def __str__(self):
        return self.branchesMOName

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class HeadsMO(models.Model):

    titleMO=models.ForeignKey(JobTitle,verbose_name="Должность", on_delete=models.CASCADE)
    phoneHeadMO=models.CharField(verbose_name="Телефон", max_length=16, blank=True, null=True)
    emailHeadMO=models.EmailField(verbose_name="Email", blank=True,  null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)
    user = models.OneToOneField(User, verbose_name="Ф.И.О.",on_delete=models.CASCADE)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.titleMO)


    class Meta:
        verbose_name = 'Руководство МО'
        verbose_name_plural = 'Руководство МО'