from django.db.models import Q
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from root.models import Friend
from root.serializer import UserRegistrationSerializer, FriendInviteSerializer, FriendSerializer


# Create your views here.

class UserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        friends = Friend.objects.all().filter(
            (Q(from_user=user_id) or Q(to_user=user_id)) and Q(status=1))
        return friends


class FriendInviteView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = FriendInviteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        friends = Friend.objects.all().filter(
            (Q(from_user=user_id) or Q(to_user=user_id)) and Q(status=1))
        return friends


class FriendViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FriendSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        friends = Friend.objects.all().filter(
            (Q(from_user=user_id) or Q(to_user=user_id)) and Q(status=3))
        return friends

