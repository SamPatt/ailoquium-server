from django.shortcuts import render
from .models import Score
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer, AIMessageSerializer
from .openai_api import send_message_to_openai, modify_openai_response
from .utilities import check_for_secret_phrase

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class AIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AIMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            secret_phrase = serializer.validated_data.get('secret_phrase')
            is_first_message = serializer.validated_data.get('is_first_message')

            message_history = request.session.get('message_history', [])

            if is_first_message:
                message_history = [
                    {"role": "system", "content": "You are running a game where the human user is playing a doctor treating AI patients, with the help of a nurse. You will respond as the patient or as the nurse depending on the request."}
                ]
            
            # Send message and history to OpenAI
            response_from_openai = send_message_to_openai(user_message, message_history)
            message_check = check_for_secret_phrase(response_from_openai, secret_phrase)

            # Update message history in the session
            request.session['message_history'] = message_history
            print("IS FIRST MESSAGE: ", is_first_message)
            print(message_history)

            if message_check:
                return Response({'response': response_from_openai, 'success': True})
            else:
                return Response({'response': response_from_openai, 'success': False})
        return Response(serializer.errors, status=400)
