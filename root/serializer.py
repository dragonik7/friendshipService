from rest_framework import serializers

from root.models import User, Friend


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class FriendInviteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    from_user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    class Meta:
        model = Friend
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('status')
        response_to_friend = Friend.objects.filter(to_user=user.id, from_user=validated_data.get('to_user')).first()
        if response_to_friend:
            response_to_friend.status = 3
            response_to_friend.save()
            return response_to_friend
        else:
            friend = Friend.objects.create(**validated_data, from_user=user)
            return friend

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.save()
        return instance


class FriendSerializer(serializers.ModelSerializer):
    from_user = UserRegistrationSerializer()
    to_user = UserRegistrationSerializer()

    class Meta:
        model = Friend
        fields = '__all__'
