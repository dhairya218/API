# serializers.py
from rest_framework import serializers
from .models import Webtoon, Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'role', 'description']

class WebtoonSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)  # Nested serializer for related characters

    class Meta:
        model = Webtoon
        fields = ['id', 'title', 'summary', 'characters']  # 'characters' will show the nested character data
