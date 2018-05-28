from rest_framework import serializers
from .models import BugTicket


class BugTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugTicket
        fields = ('title', 'date_created', 'status', 'bug_type')
    
    
    
# figure out method to calculate # 'doing' & # complete by day, week, month
# count method include in json data
