from django.db import models
from django.db.models.fields import DateField
from account.models import User
from helpInfo.models import typeMO,typeAgeMO,OKOPF,OKDP,OKFS,OKPO,OKVED,ONMSZ,ORGANITION_FORM,GovOrg,BuildingMO,PlaceForm
from helpInfo.models import Organizion

class passportMO(models.Model):
    nameMO = models.CharField(verbose_name="Наименование МО", max_length=29, blank=True, null=True)
    shortNameMO = models.CharField(verbose_name="Краткое наименование МО",max_length=50,blank=True, null=True)
    codeOUZS = models.CharField(verbose_name="Код органа управления здравоохранением субъекта", max_length=13, blank=True, null=True)

    class Meta:
        verbose_name = 'Паспорт МО'
        verbose_name_plural = 'Паспорт МО'
class identificationMO(models.Model):
    govOrg= models.ForeignKey(GovOrg, verbose_name="Орган, зарегистрировавший юридическое лицо", on_delete=models.CASCADE)
    regDate = models.DateField(verbose_name="Дата регистрации ", auto_now=False, auto_now_add=False)
    docName = models.CharField(verbose_name="Наименование регистрационного документа", max_length=50, blank=True, null=True)
    regNo = models.CharField(verbose_name="Номер государственной регистрации.", max_length=13, blank=True, null=True)
    regNoSF = models.CharField(verbose_name="Регистрационный номер в Социальном фонде КР.", max_length=13, blank=True, null=True)
    founder=models.TextField(verbose_name="Учредитель",blank=True, null=True)
    beginDate = models.DateField(verbose_name="Дата начала деятельности", auto_now=False, auto_now_add=False)
    endDate = models.DateField(verbose_name="Дата закрытия", auto_now=False, auto_now_add=False)
    emailMO = models.EmailField(verbose_name="Адрес электронной почты",blank=True, null=True)
    siteMO = models.CharField(verbose_name="Адрес сайта",max_length=50,blank=True, null=True)
    phoneMO = models.CharField(verbose_name="Телефон", max_length=13, blank=True, null=True)
    timeWorkMO = models.CharField(verbose_name="Время работы", max_length=16, blank=True, null=True)
    nameMOLVN = models.CharField(verbose_name="Наименование МО для ЛВН", max_length=29, blank=True, null=True)
    addressMOLVN = models.CharField(verbose_name="Адрес МО для ЛВН", max_length=30, blank=True, null=True)
    typeMO = models.ForeignKey(typeMO, verbose_name="Тип МО", on_delete=models.CASCADE)
    typeAgeMO = models.ForeignKey(typeAgeMO, verbose_name="Тип МО по возрасту", on_delete=models.CASCADE)
    addressRegMO = models.CharField(verbose_name="Юридический адрес ", max_length=50, blank=True, null=True)
    addressRealMO = models.CharField(verbose_name="Фактический адрес", max_length=50, blank=True, null=True)
    okfs = models.ForeignKey(OKFS, verbose_name="ТОКФС", on_delete=models.CASCADE)
    okopf = models.ForeignKey(OKOPF, verbose_name="ОКОПФ", on_delete=models.CASCADE)
    okpo = models.ForeignKey(OKPO, verbose_name="ОКПО", on_delete=models.CASCADE)
    INN = models.CharField(verbose_name="ИНН", max_length=14, blank=True, null=True)
    OGRN = models.CharField(verbose_name="ОГРН – основной государственный регистрационный номер", max_length=14, blank=True, null=True)
    okdp = models.ForeignKey(OKDP, verbose_name="ОКДП", on_delete=models.CASCADE)
    okved= models.ForeignKey(OKVED, verbose_name="ОКВЭД", on_delete=models.CASCADE)
    rayonCoef = models.DecimalField(verbose_name="Районный коэффициент", max_digits=2, decimal_places=1)
    spesStatus = models.DecimalField(verbose_name="Особый статус", max_digits=2, decimal_places=1)
    onmsz = models.ForeignKey(ONMSZ, verbose_name="ОКВЭД", on_delete=models.CASCADE)
    organForm = models.ForeignKey(ORGANITION_FORM, verbose_name="Организационная форма.", on_delete=models.CASCADE)
    placeForm = models.ForeignKey(PlaceForm, verbose_name="Территориальный признак", on_delete=models.CASCADE)
    buildingMO = models.ForeignKey(BuildingMO, verbose_name="Основное здание", on_delete=models.CASCADE)
    passportMO = models.OneToOneField(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameMOLVN

    class Meta:
        verbose_name = 'Идентификация'
        verbose_name_plural = 'Идентификация'



class OmsMO(models.Model):
    inDate = models.DateField(verbose_name="Дата включения", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата исключения", auto_now=False, auto_now_add=False)
    dogovNo = models.CharField(verbose_name="Номер договора", max_length=13, blank=True, null=True)
    regDate = models.DateField(verbose_name="Дата договора ", auto_now=False, auto_now_add=False)
    organizion = models.ForeignKey(Organizion, on_delete=models.CASCADE)
    placeCodeMO = models.CharField(verbose_name="Код территории МО", max_length=6, blank=True, null=True)
    regNo = models.CharField(verbose_name="Регистрационный номер МО", max_length=13, blank=True, null=True)
    comment = models.TextField(verbose_name="Примечание к договору", blank=True, null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.dogovNo

    class Meta:
        verbose_name = 'ОМС(Обязательное медицинское страхование)'
        verbose_name_plural = 'ОМС(Обязательное медицинское страхование)'

class LloMO(models.Model):
    inDate = models.DateField(verbose_name="Дата включения", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата исключения", auto_now=False, auto_now_add=False)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.inDate

    class Meta:
        verbose_name = 'ЛЛО (Льготное лекарственное обеспечение)'
        verbose_name_plural = 'ЛЛО (Льготное лекарственное обеспечение)'




class DmsMO(models.Model):
    inDate = models.DateField(verbose_name="Дата включения", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата исключения", auto_now=False, auto_now_add=False)
    dogovNo = models.CharField(verbose_name="Номер договора", max_length=13, blank=True, null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.dogovNo

    class Meta:
        verbose_name = 'ДМС (Добровольное медицинское страхование)'
        verbose_name_plural = 'ДМС (Добровольное медицинское страхование)'


class UchasSlujbaMO(models.Model):
    inDate = models.DateField(verbose_name="Дата включения", auto_now=False, auto_now_add=False)
    outDate = models.DateField(verbose_name="Дата исключения", auto_now=False, auto_now_add=False)
    typeUshastok = models.CharField(verbose_name="Тип участка ", max_length=13, blank=True, null=True)
    passportMO = models.ForeignKey(passportMO, on_delete=models.CASCADE)

    def __str__(self):
        return self.typeUshastok

    class Meta:
        verbose_name = 'Участковая служба'
        verbose_name_plural = 'Участковая служба'