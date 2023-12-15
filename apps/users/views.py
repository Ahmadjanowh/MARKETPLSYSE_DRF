from rest_framework .generics import ListCreateAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from apps.users.models import User
from apps.users.serializers import  UserRegisterSerializer,UserSerializer

# Create your views here.
class UserListCrateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer