from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'due_back', 'status')
admin.site.register(BookInstance, BookInstanceAdmin)
    


admin.site.register(Genre)
admin.site.register(Language)

