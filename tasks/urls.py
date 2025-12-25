from django.urls import path,include
from .views import TaskList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskList)

urlpatterns = [
    path('', include(router.urls)),
]

