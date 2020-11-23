from urlShorteners.models import Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
            'base_url'
        ]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        print(request.user.id)
        if request and hasattr(request, "user"):
            user = request.user.id
        validated_data['user'] = user

        print(request.data.get('suggestion'), validated_data)
        Url.objects.create(
            request.data.get('suggestion'), **validated_data)
        # print('baad', validated_data, request.data.get('suggestion'))
        # return super(UrlSerializer, self).create(validated_data)
