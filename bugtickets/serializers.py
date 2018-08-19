from rest_framework import serializers
from .models import BugTicket

# Select fileds to be included in API
class BugTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugTicket
        fields = ('title', 'date_created', 'status', 'bug_type')
    
    
    

