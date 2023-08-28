from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly



class PostList(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]

    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
