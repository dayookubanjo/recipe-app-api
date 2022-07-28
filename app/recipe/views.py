"""
Views for the recipe APIs.
"""
from rest_framework import viewsets, mixins
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication
    )
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe, Tag

from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for managing recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication,
                                SessionAuthentication,
                                BasicAuthentication]
    permission_classes = [IsAuthenticated,]

    #Allows us to filter the queryset for authenticated user
    def get_queryset(self): #This is called when action is list
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self): #This determine the serializer to use
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    #This is called when it's a post request to save record with logged in user.
    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)

# mixins.ListModelMixin, viewsets.GenericViewSet
class TagViewSet(mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication,
                                SessionAuthentication,
                                BasicAuthentication]
    permission_classes = [IsAuthenticated,]

    #Allows us to filter the queryset for authenticated user
    def get_queryset(self): #This is called when action is list
        """Retrieve the tags for the authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')