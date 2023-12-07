from rest_framework import serializers

from users.models import User


class ProfileSerializers(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('__all__',)

    def get_is_subscribed(self, obj):
        pass