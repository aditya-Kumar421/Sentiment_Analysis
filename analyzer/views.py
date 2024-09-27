import requests
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from django.http import JsonResponse
from django.conf import settings

from .serializers import FileCheck

AMAZON_REVIEW_API_URL = "https://api-inference.huggingface.co/models/gyesibiney/Sentiment-review-analysis-roberta-3" 
API_TOKEN = settings.HUGGINGFACE_API_KEY  


class SentimentView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        print("Request content type:", request.content_type)
        serializer = FileCheck(data=request.data)

        if serializer.is_valid():
            file = serializer.validated_data['file']
            ext = file.name.split('.')[-1]

            try:
                if ext == 'csv':
                    df = pd.read_csv(file)
                elif ext == 'xlsx':
                    df = pd.read_excel(file)

                if 'Review' not in df.columns:
                    return Response({"error": "No 'Review' column found in the file"}, status=status.HTTP_400_BAD_REQUEST)

                reviews = df['Review'].tolist()
                result = self.review_sentiment(reviews)

                if 'error' in result:
                    return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                return JsonResponse(result)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def review_sentiment(self, reviews):
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        results = {"positive": 0, "negative": 0, "neutral": 0}

        for review in reviews:
            data = {"inputs": review}
            try:
                response = requests.post(AMAZON_REVIEW_API_URL, headers=headers, json=data)
                response_data = response.json()

                if isinstance(response_data, list) and len(response_data) > 0:
                    output = response_data[0]

                    if isinstance(output, list):
                        highest_score = max(output, key=lambda x: x['score'])
                        label = highest_score.get('label', None)
                        score = highest_score.get('score', 0)

                        if label == 'POSITIVE':
                            results["positive"] += score
                        elif label == 'NEGATIVE':
                            results["negative"] += score
                        else:
                            results["neutral"] += score
                    else:
                        return {"error": "Unexpected output format", "details": output}

                else:
                    return {"error": "Unexpected response format", "details": response_data}

            except requests.exceptions.RequestException as e:
                return {"error": "Failed to connect to Review Sentiment Analysis API", "details": str(e)}
        return results