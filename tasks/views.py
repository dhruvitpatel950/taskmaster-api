from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions,throttling,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [throttling.UserRateThrottle]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    
    filterset_fields = ['is_completed', 'priority', 'project']
    search_fields = [
        'title', 
        'description', 
        'owner__username', 
        'project__name',          
        'tag__name'      
    ]
    ordering_fields = ['priority', 'created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner = self.request.user)
        




