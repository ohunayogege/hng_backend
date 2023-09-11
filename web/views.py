from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Person
from .serializers import PersonSerializer
import pytz


class slackFirstTask(APIView):
    def get(self, request):
        # Get the current date and time
        current_datetime = datetime.now()
        # Get the current UTC time
        current_utc_time = datetime.now(pytz.utc)

        current_utc_time = datetime.now(pytz.utc)

        # Format the UTC time in the desired format
        formatted_utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
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
            "utc_time": formatted_utc_time,
            "track": track,
            "github_file_url": "https://github.com/ohunayogege/hng_backend/blob/master/web/views.py",
            "github_repo_url": "https://github.com/ohunayogege/hng_backend",
            "status_code": status.HTTP_200_OK
        }
        return Response(data, status=status.HTTP_200_OK)


# Let's Start the CRU Operation
class CreatePerson(APIView):

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"status": False, "message": "Name must not be empty."}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the 'name' field is a string
        if not isinstance(name, str):
            return Response({"status": False, "message": "Name must be a string."}, status=status.HTTP_400_BAD_REQUEST)
        obj = Person.objects.create(name=name.title())
        data = {
            "user_id": obj.pk,
            "name": obj.name,
            "created_on_date": obj.added.date(),
            "create_on_time": obj.added.time()
        }
        return Response({"status": True, "message": "Person data added.", "data": data}, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        if not pk:
            return Response({"status": False, "message": "Please provide user_id you want to fetch."},
                            status=status.HTTP_400_BAD_REQUEST)
        check_if_user_exists = Person.objects.filter(pk=pk).exists()
        if not check_if_user_exists:
            return Response({"status": False, "message": f"The user_id {pk} does not exists."},
                            status=status.HTTP_400_BAD_REQUEST)
        user = Person.objects.get(pk=pk)
        data = {
            "user_id": user.pk,
            "name": user.name,
            "created_on_date": user.added.date(),
            "create_on_time": user.added.time()
        }
        return Response({"status": True, "message": "Person data added.", "data": data}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        queryset = Person.objects.all()
        serializer_class = PersonSerializer
        user_id = kwargs.get('pk')

        # Check if the person exists
        try:
            person = Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return Response({"status": False, "message": f"The user with user_id {user_id} does not exist."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = serializer_class(person, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": f"Person with user_id {user_id} updated successfully."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": False, "message": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        try:
            person = Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return Response({"status": False, "message": f"The user with user_id {user_id} does not exist."},
                            status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response({"status": True, "message": f"Person with user_id {user_id} has been deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
