from rest_framework import generics
from ..models import UserInfo
from .serializers import UserInfoSerializer
class UserInfoListView(generics.ListAPIView): 
    queryset = UserInfo.objects.all() 
    serializer_class = UserInfoSerializer
class UserInfoDetailView(generics.RetrieveAPIView): 
    queryset = UserInfo.objects.all() 
    serializer_class = UserInfoSerializer
