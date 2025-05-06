from rest_framework import generics
from rest_framework.response import Response
import os
from django.conf import settings
import pandas as pd
from django.conf import settings
import google.generativeai as genai
from utils.FileCache import FileCache


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
file_cache = FileCache(settings.MEDIA_ROOT)

class ChatView(generics.GenericAPIView):
    """
        This view is to get question answer from gemini
    """

    def post(self, request):
        """
            Get question answer for questions on file
        """
        try:
            df = {}
            question = request.data.get("question")

            file_cache.read_from_directory()



            # Define the prompt based on question and file
            prompt = file_cache.construct_prompt(question=question)

            response = model.generate_content(prompt)
            answer = response.text

            return Response({'answer': answer})
        except Exception as exp:
            print(exp)
            return Response({'error': "something went wrong"}, status=500)
    