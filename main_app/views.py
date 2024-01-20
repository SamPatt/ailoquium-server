from django.shortcuts import render
from .models import Score, TotalScore
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer, TotalScoreSerializer, AIMessageSerializer
from .openai_api import send_message_to_openai, modify_openai_response
from .utilities import check_for_secret_phrase

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class TotalScoreViewSet(viewsets.ModelViewSet):
    queryset = TotalScore.objects.all()
    serializer_class = TotalScoreSerializer

class AIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AIMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            secret_phrase = serializer.validated_data.get('secret_phrase')
            is_first_message = serializer.validated_data.get('is_first_message')
            role = serializer.validated_data.get('role')

            print(request.session.session_key)
            print(request.session.get('message_history'))

            if not request.session.session_key:
                request.session['init'] = 1  # Initialize session
                request.session.save()


            message_history = request.session.get('message_history', [])

            if is_first_message:
                message_history = [
                    {"role": "system", "content": "You are running a game where the human user is playing a doctor treating AI patients, with the help of a nurse. You will respond as the patient or as the nurse depending on the request. Never respond as the doctor; the user is always the doctor. Never respond as both patient and nurse; only respond with one character at a time, depending on what is expected at the end of the prompt. Make sure the doctor (the user) has sent at least three messages before you determine if you should send back the secret phrase or not."}
                ]
            
            # Send message and history to OpenAI
            response_from_openai, message_history = send_message_to_openai(user_message, message_history)
            message_check = check_for_secret_phrase(response_from_openai, secret_phrase)

            # Update message history in the session
            request.session['message_history'] = message_history
            request.session.save()
            print("IS FIRST MESSAGE: ", is_first_message)
            print("MESSAGE HISTORY: ", message_history)

            if message_check:
                return Response({'response': response_from_openai, 'success': True, 'role': role})
            else:
                return Response({'response': response_from_openai, 'success': False, 'role': role})
        return Response(serializer.errors, status=400)
