from rest_framework.routers import DefaultRouter
from django.urls import path

from main.apps import MainConfig
from main.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from users.views import UserViewSet, PaymentsListAPIView, PaymentsRetrieveAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', UserViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_view'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('moto/delite/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delite'),

    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments_get'),
] + router.urls
