from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


class PostList(ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
