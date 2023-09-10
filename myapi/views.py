from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .models import MyData
from .serializers import MyDataSerializer


class MyApiView(APIView):
    def get(self, request):
        slack_name = "Ayomide Francis-Akinlolu"  # Replace with your actual Slack name
        track = "backend"
        current_day = datetime.now().strftime('%A')
        utc_time = datetime.utcnow().isoformat() + 'Z'
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
