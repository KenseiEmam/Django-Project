"""
Views for Recipe APIS
"""
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe,Tag
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_class=[TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticate user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
        
    def get_serializer_class(self):
    
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return serializers.RecipeDetailSerializer
        
    def perform_create(self,serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class TagViewSet(mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        """Retrieve tag for authenticate user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
        
    def perform_create(self,serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)