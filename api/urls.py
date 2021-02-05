from django.urls import path,include
from .views import *
from .serializers import *

urlpatterns = [
    path('entries/', JournalEntryView.as_view(queryset=JournalEntry.objects.all(), serializer_class=EntrySerializer), name='entry-list')
]
