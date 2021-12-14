from django.db.models import fields
from rest_framework import serializers
from .models import Book, Author
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Author
        fields = '__all__'
        


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
        
    def get_author_name(self, obj):
        return obj.author.full_name
    
    