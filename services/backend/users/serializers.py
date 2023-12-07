from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from users.models import User


class ProfileSerializers(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'is_subscribed')

    @extend_schema_field(serializers.BooleanField(read_only=True))
    def get_is_subscribed(self, obj):
        return False