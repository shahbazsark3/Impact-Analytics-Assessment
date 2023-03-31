import traceback
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.services.analytics_services import GraduationAttendanceMissingDays


class AttendanceClassInfoView(APIView):
    def __init__(self):
        super().__init__()
        self.graduation_service = GraduationAttendanceMissingDays()

    def get(self, request):
        try:
            no_of_days = request.GET.get('no_of_days')
            if int(no_of_days)>3:
                calling_assessment_services = self.graduation_service.reformat_the_logic_and_response(int(no_of_days))
                return Response({"data": calling_assessment_services, "message": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": None, "message": "Check the params you have passed it should be above 4 days"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.format_exc()
            return Response({"data": None, "message": "Check the Exception Case due to " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
