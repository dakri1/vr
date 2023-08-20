from django.contrib import admin
from .models import *


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'time_create', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'time_create', 'text')
    search_fields = ('post', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Programs, ProgramAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentAdmin)

