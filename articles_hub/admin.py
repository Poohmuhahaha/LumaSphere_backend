# Register your models here.
from django.contrib import admin
from .models import Article, Category, Tag, Author

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
