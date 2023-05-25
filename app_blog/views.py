from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .permissions import *

# Create your views here.



# class FixView(ModelViewSet):
#     pass

class BlogCategoryView(ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class BlogPostView(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # we overridden the function at the class blogpostview inherited from
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
    permission_classes = [IsAdminOrReadOnly]
    
class BlogCommentView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]