from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone

from .models import MyData
from .serializers import MyDataSerializer


class MyApiView(APIView):
    def get(self, request):
        slack_name = "ayomisco"  
        track = "backend"
        # Get current day of the week
        current_day = datetime.now().strftime('%A')

        # Get current UTC time formatted as "2023-09-10T17:04:33Z"
        utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        # Replace with your GitHub file URL
        github_file_url = "https://github.com/Ayomisco/hngx-stage1/blob/main/README.md"
        # Replace with your GitHub repo URL
        github_repo_url = "https://github.com/Ayomisco/hngx-stage1"
        status_code = 200

        data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": status_code
        }

        # Save the data to the database if needed
        MyData.objects.create(**data)

        serializer = MyDataSerializer(data)
        return Response(serializer.data)
