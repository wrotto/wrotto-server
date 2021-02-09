from django.shortcuts import render
from .models import *
from .serializers import EntrySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import django_filters
from rest_framework import generics
from rest_framework.decorators import api_view
from datetime import datetime

class JournalEntryView(generics.ListAPIView):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = JournalEntry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title',]
    ordering_fields = ['date',]

@api_view(['POST'])
def BackupEntriesAPIView(request):
    if request.method == "POST":

        for entry in request.data:
            # datetime.fromtimestamp(float(sys.argv[1])/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            entry['date'] = datetime.fromtimestamp(entry['date']/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
            entry['lastModified'] = datetime.fromtimestamp(entry['lastModified']/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
            medias = entry['medias'].split(",")
            tags = entry['tags'].split(",")
            serializer = EntrySerializer(data=entry)
            serializer.is_valid(raise_exception=True)
            entry = serializer.save()

            for tag in tags:
                if(tag!=''):
                    tag, created = Tag.objects.get_or_create(name=tag)
                    EntryTag.objects.create(entry=entry,tag=tag )

            for media in medias:
                if(media!=''):
                    Media.objects.create(entry=entry, mediaType=MediaType.picture,filePath=media,name="")

        return Response("", status=201,)
    else:
        return Response("", status=404)
