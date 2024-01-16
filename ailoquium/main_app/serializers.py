from rest_framework import serializers

from .models import Score


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Score

        fields = '__all__'

class AIMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    secret_phrase = serializers.CharField()
    is_first_message = serializers.BooleanField()