from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if not all(char.isalpha() or char == '.' or char == ' ' for char in value):
            raise serializers.ValidationError("Поле name должно состоять только из букв, точек и пробелов.")
        return value

    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not all(char.isalnum() or char == ' ' for char in value):
            raise serializers.ValidationError("Поле title должно состоять только из букв, цифр и пробелов.")
        return value

    authors = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Author.objects.all(),
        many=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']

