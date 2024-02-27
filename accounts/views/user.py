from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from accounts.serializers.user import UserSerializer
from accounts.filters.user import UserFilter
from accounts.models.user import User


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
