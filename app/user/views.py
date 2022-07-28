"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    # ObtainAuthToken doesn't support UI view hence below setting
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes= [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
        authentication.BasicAuthentication
        ]
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    """
    get_object function below:
    Gets the object for the http get request or any request made to this api
    Retireves the user object and run it through our serializer before returning
    the user as the result (request.user)
    """
    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

# from .serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import GenericAPIView


# Create your views here.

# class CreateUserAPIView(GenericAPIView):

#     serializer_class = UserSerializer

#     def post(self,request):
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status =status.HTTP_201_CREATED)
#             # return JsonResponse(serializer.data, status = 201)

#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GetUserAPIView(GenericAPIView):

#     serializer_class = UserSerializer

#     def get(self,request):
#         if request.method == 'GET':
#             user = request.user
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
