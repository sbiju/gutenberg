from rest_framework import serializers
from .models import BooksBook, BooksAuthor, BooksLanguage, BooksSubject, BooksBookshelf, BooksFormat


# class BooksAuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksAuthor
#         fields = ['name', 'birth_year', 'death_year']


# class BooksLanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksLanguage
#         fields = ['code']


# class BooksSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksSubject
#         fields = ['name']


# class BooksBookshelfSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksBookshelf
#         fields = ['name']


# class BooksFormatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksFormat
#         fields = ['mime_type', 'url']


class BooksBookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = BooksBook
        fields = ['title', 'download_count', 'gutenberg_id', 'media_type', 'authors', 'languages', 'subjects', 'bookshelves', 'formats']

    def get_authors(self, obj):
        book_authors = obj.booksbookauthors_set.all()  
        return [{'name': author.author.name, 'birth_year': author.author.birth_year, 'death_year': author.author.death_year}
                for author in book_authors]
    
    def get_languages(self, obj):
        book_languages = obj.booksbooklanguages_set.all()
        return [{'code': language.language.code} for language in book_languages]

    def get_subjects(self, obj):
        book_subjects = obj.booksbooksubjects_set.all()
        return [{'name': subject.subject.name} for subject in book_subjects]

    def get_bookshelves(self, obj):
        book_bookshelves = obj.booksbookbookshelves_set.all()
        return [{'name': bookshelf.bookshelf.name} for bookshelf in book_bookshelves]

    def get_formats(self, obj):
        book_formats = obj.booksformat_set.all()
        return [{'mime_type': format.mime_type, 'url': format.url} for format in book_formats]
    