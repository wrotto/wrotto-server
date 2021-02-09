from rest_framework import serializers
from .models import *

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ('pk','title', 'text', 'date', 'mood', 'longitude', 'latitude','locationDisplayName','synchronised',  'lastModified')