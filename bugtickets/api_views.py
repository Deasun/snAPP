from rest_framework import generics
from .models import BugTicket
from .serializers import BugTicketSerializer
import datetime

class BugTicketViewSet(generics.ListAPIView):
    """
    Filter data to GET active bugtickets over the last week
    """
    queryset = BugTicket.objects.all()
    serializer_class = BugTicketSerializer
    print(BugTicket.qs_30_day_active_bugs())
    print(BugTicket.qs_7_day_active_bugs())
    print(BugTicket.qs_today_active_bugs())
    print(BugTicket.qs_today_complete_bugs())
    print(BugTicket.qs_7_day_complete_bugs())
    print(BugTicket.qs_30_day_complete_bugs())
   
