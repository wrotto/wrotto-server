from django.contrib import admin
from .models import *
from django import forms

class TagInline(admin.TabularInline):
    model = EntryTag
    fields = ['tag',]
    show_change_link = True

class EntryInline(admin.TabularInline):
    model = EntryTag
    fields = ['entry',]
    show_change_link = True


class MediaInline(admin.TabularInline):
    model = Media
    fields = ['name','filePath', 'mediaType', 'entry' ]
    show_change_link = True

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    inlines = [TagInline, MediaInline]
    search_fields = ('title','text', 'date', 'mood', 'longitude', 'latitude')
    list_display = ('title','text', 'date', 'mood', 'longitude', 'latitude')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    search_fields = ('name','filePath', 'mediaType', 'entry')
    list_display = ('name','filePath', 'mediaType', 'entry')