from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Course, Lesson
from users.models import User


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

