from rest_framework import generics
from rest_framework.response import Response
from dashboard.models import Dashboards
from dashboard.serializers.DashBoardSerializer import DashBoardSerializer




class DashBoardView(generics.GenericAPIView):
    """
        This file is used manage dashboard data
    """

    def get(self, request):
        """
            Fetch all dashboards
        """
        try:
            dashboards =  Dashboards.objects.all()
            serializedData = DashBoardSerializer(dashboards, many=True)
            return Response(serializedData.data)
        except Exception:
            return Response({'error': 'something went wrong'}, status=500)
        