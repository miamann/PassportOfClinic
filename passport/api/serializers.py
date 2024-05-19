
from rest_framework import serializers
from account.models import User
from django.contrib.auth.models import Group
from passport.models import passportMO

class PassportMOSerializer(serializers.ModelSerializer):
    class Meta:
        model = passportMO
        fields = '__all__'

class AddFavoriteBookSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = FavoriteBook
        fields = ['id', 'user', 'book', 'added_on']

    def create(self, validated_data):
        favorite_book, created = FavoriteBook.objects.get_or_create(**validated_data)
        return favorite_book