from django.shortcuts import render
from .models import Score
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer
from .serializers import AIMessageSerializer


class ScoreViewSet(viewsets.ModelViewSet):

    queryset = Score.objects.all()

    serializer_class = ScoreSerializer

class AIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AIMessageSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']
            # Process the message, send it to OpenAI API, modify the response
            # For example:
            # response_from_openai = send_message_to_openai(user_message)
            # modified_response = modify_openai_response(response_from_openai)

            return Response({'response': 'AIresponse' }) # modified_response
        return Response(serializer.errors, status=400)

# # Create your views here.
# def home(request):
#   # Include an .html file extension - unlike when rendering EJS templates
#   return render(request, 'index.html')

# def about(request):
#   return render(request, 'index.html')