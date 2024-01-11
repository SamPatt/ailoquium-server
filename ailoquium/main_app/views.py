from django.shortcuts import render
from .models import Score
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer, AIMessageSerializer
from .openai_api import send_message_to_openai, modify_openai_response  # Import the functions

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class AIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AIMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            
            response_from_openai = send_message_to_openai(user_message)
            # modified_response = modify_openai_response(response_from_openai)

            return Response({'response': response_from_openai})
        return Response(serializer.errors, status=400)
