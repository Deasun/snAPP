from rest_framework import generics
from .models import BugTicket
from .serializers import BugTicketSerializer
import datetime

class BugTicketViewSet(generics.ListAPIView):
    """
    Filter data for bugticket data - API view
    """
    queryset = BugTicket.objects.all()
    serializer_class = BugTicketSerializer

   
