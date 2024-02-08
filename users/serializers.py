from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Course, Lesson
from users.models import User, Payments


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    course_pay = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    lesson_pay = SlugRelatedField(slug_field='name', queryset=Lesson.objects.all())
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Payments
        fields = '__all__'