from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields=['id','title','body','author','created_at']
        model=Blog