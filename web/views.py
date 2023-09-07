from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz


class slackFirstTask(APIView):
    def get(self, request):
        # Get the current date and time
        current_datetime = datetime.now()
        # Get the current UTC time
        current_utc_time = datetime.now(pytz.utc)
        # For example, if you want to convert it to New York time:
        lagos_timezone = pytz.timezone('Africa/Lagos')
        current_lagos_time = current_utc_time.astimezone(lagos_timezone)
        # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, etc.)
        day_of_week = current_lagos_time.weekday()

        # You can convert it to a string if needed
        day_name = current_lagos_time.strftime('%A')

        slack_name = request.GET.get("slack_name", "")
        track = request.GET.get("track", "")
        if slack_name == "":
            return Response({"message": "slack_name must not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        if track == "":
            return Response({"message": "track must not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "slack_name": slack_name,
            "current_day": day_name,
            "utc_time": current_lagos_time,
            "track": track,
            "github_file_url": "https://github.com/ohunayogege/hng_backend/blob/master/web/views.py",
            "github_repo_url": "https://github.com/ohunayogege/hng_backend",
            "status_code": status.HTTP_200_OK
        }
        return Response(data, status=status.HTTP_200_OK)
