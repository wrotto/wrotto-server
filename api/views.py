from django.shortcuts import render
from .models import *
from .serializers import EntrySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import django_filters
from rest_framework import generics

class JournalEntryView(generics.ListAPIView):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = JournalEntry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title',]
    ordering_fields = ['date',]