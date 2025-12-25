from rest_framework import serializers
from .models import Task,Project,Tag

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source  = "owner.username")

    project_details= ProjectSerializer(source='project', read_only = True)
    tag_details = TagSerializer(source='tag', many = True,read_only = True)

    project = serializers.PrimaryKeyRelatedField(
        queryset= Project.objects.all(),
        write_only=True, 
        required=False, 
        allow_null=True
    )

    tags = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many=True, 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'is_completed', 'priority', 
            'owner_name', 
            'project', 'project_details',  
            'tags', 'tag_details',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    