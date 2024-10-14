# admin.py
from django.contrib import admin
from .models import Webtoon, Character

class CharacterInline(admin.TabularInline):
    model = Character
    extra = 1  # Allows adding new character directly in the webtoon admin page

class WebtoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')  # Display these fields in the list view
    search_fields = ('title',)  # Add a search bar for the title
    inlines = [CharacterInline]  # Allow inline editing of characters in Webtoon

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'description', 'webtoon')  # Show character fields, including the ForeignKey to Webtoon
    search_fields = ('name', 'role')  # Add search options for characters

admin.site.register(Webtoon, WebtoonAdmin)
admin.site.register(Character, CharacterAdmin)
