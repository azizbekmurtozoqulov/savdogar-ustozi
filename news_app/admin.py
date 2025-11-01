from django.contrib import admin
from django import forms
from .models import News, Category, Contact, Resume

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',   'publish_time', 'status', 'category')
    list_filter = ['status','publish_time','created_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ('publish_time','status')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # admin panelda ko‘rinsin
    search_fields = ('name', 'email')

admin.site.register(Resume)