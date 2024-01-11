from django.shortcuts import render
from .models import Score
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer, AIMessageSerializer
from .openai_api import send_message_to_openai, modify_openai_response  # Import the functions
from .utilities import check_for_prompt_hacking

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class AIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AIMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            
            message_check = check_for_prompt_hacking(user_message)

            if message_check:
                # modified_response = modify_openai_response(response_from_openai)
                response_from_openai = send_message_to_openai(user_message)
                return Response({'response': response_from_openai})
            else:
                return Response({'response': "No prompt hacking"})
        return Response(serializer.errors, status=400)
