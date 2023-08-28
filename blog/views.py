from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Blog
from rest_framework import permissions

class PostList(ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated)
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated)
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
