from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Course, Lesson
from users.models import User

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'lesson_description']


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, course):
        return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


