from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Blog


class PostList(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
