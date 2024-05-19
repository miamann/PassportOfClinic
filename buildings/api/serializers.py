from rest_framework import serializers
from account.models import User
from django.contrib.auth.models import Group
from buildings.models import BuildingMO,InfrastructureMO
from passport.api.serializers import PassportMOSerializer


class BuildingMOSerializer(serializers.ModelSerializer):
    passportMO = PassportMOSerializer(many=True, read_only=True)
    author = AuthorSerializer(many=True, read_only=True)
    jenres = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    class Meta:
        model = BuildingMO
        fields = '__all__'







class (serializers.Serializer):
    
    fencingBuildMO = serializers.BooleanField(label="Ограждение территории", default=True)
    bodyguardMO = serializers.BooleanField(label="Наличие охраны", default=True)
    metalDoorMO = serializers.BooleanField(label="Наличие металлических входных дверей в здание", default=True)
    videoSurvMO = serializers.BooleanField(label="Видеонаблюдение территорий и помещений для здания", default=True)
    accommodationMO = serializers.BooleanField(label="Проживание сопровождающих лиц", default=False)
    forDisabilitiesMO = serializers.BooleanField(
        label="Приспособленность территории для пациентов с ограниченными возможностями", default=True)
    latitudeMO = serializers.DecimalField(label="Координаты: Широта", max_digits=4, decimal_places=2)
    longitudeMO = serializers.DecimalField(label="Координаты: Долгота", max_digits=4, decimal_places=2)

    bldgMOName = serializers.CharField(label="Общепринятое наименование корпуса", max_length=80, blank=True,
                                  null=True)
    bldgNoMO = serializers.CharField(label="Номер корпуса", max_length=16, blank=True,
                                null=True)
    bldgTypeMO = serializers.CharField(label="тип лечебного корпуса", max_length=16, blank=True,
                                  null=True)
    bldgPurposeMO = serializers.CharField(label="назначение здания", max_length=16, blank=True,
                                     null=True)
    bldgYearMO = serializers.IntegerField(label="Год постройки ", required=False)
    bldgSquareMO = serializers.DecimalField(label="Общая площадь", max_digits=6, decimal_places=2, null=True)
    passportMO = serializers.ForeignKey(passportMO, on_delete=serializers.CASCADE)
    

    username=serializers.CharField(label='Username:')
    first_name=serializers.CharField(label='First name:')
    last_name=serializers.CharField(label='Last name:', required=False)
    password = serializers.CharField(label='Password:',style={'input_type': 'password'}, write_only=True,min_length=8,
    help_text="Your password must contain at least 8 characters and should not be entirely numeric."
    )
    password2=serializers.CharField(label='Confirm password:',style={'input_type': 'password'},  write_only=True)
    

    
    def validate_username(self, username):
        username_exists=User.objects.filter(username__iexact=username)
        if username_exists:
            raise serializers.ValidationError({'username':'This username already exists'})
        return username

        
    def validate_password(self, password):
        if password.isdigit():
            raise serializers.ValidationError('Your password should contain letters!')
        return password  

 

    def validate(self, data):
        password=data.get('password')
        password2=data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        return data


    def create(self, validated_data):
        user= User.objects.create(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                status=False
            )
        user.set_password(validated_data['password'])
        user.save()
        group_doctor, created = Group.objects.get_or_create(name='doctor')
        group_doctor.user_set.add(user)
        return user

class doctorProfileSerializer(serializers.Serializer):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'
    department=serializers.ChoiceField(label='Department:', choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ])
    address= serializers.CharField(label="Address:")
    mobile=serializers.CharField(label="Mobile Number:", max_length=20)


    def validate_mobile(self, mobile):
        if mobile.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return mobile
    
    def create(self, validated_data):
        new_doctor= doctor.objects.create(
            department=validated_data['department'],
            address=validated_data['address'],
            mobile=validated_data['mobile'],
            user=validated_data['user']
        )
        return new_doctor
    
    def update(self, instance, validated_data):
        instance.department=validated_data.get('department', instance.department)
        instance.address=validated_data.get('address', instance.address)
        instance.mobile=validated_data.get('mobile', instance.mobile)
        instance.save()
        return instance



class patientHistorySerializerDoctorView(serializers.Serializer):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'
    admit_date=serializers.DateField(label="Admit Date:", read_only=True)
    symptomps=serializers.CharField(label="Symptomps:", style={'base_template': 'textarea.html'})
    department=serializers.CharField(label='Department: ')
    #required=False; if this field is not required to be present during deserialization.
    release_date=serializers.DateField(label="Release Date:", required=False)
    assigned_doctor=serializers.StringRelatedField(label='Assigned Doctor:')
    


class doctorAppointmentSerializer(serializers.Serializer):
    patient_name=serializers.SerializerMethodField('related_patient_name')
    patient_age=serializers.SerializerMethodField('related_patient_age')
    appointment_date=serializers.DateField(label="Appointment Date:",)
    appointment_time=serializers.TimeField(label="Appointment Time:")
    patient_history=patientHistorySerializerDoctorView(label='patient History:')
    

    def related_patient_name(self, obj):
        return obj.patient_history.patient.get_name
    
    def related_patient_age(self, obj):
        return obj.patient_history.patient.age








