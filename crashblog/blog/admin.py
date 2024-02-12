from django.contrib import admin
from .models import PostModel, CommentModel, CategoryModel

# Register your models here.
class CommentItemInline(admin.TabularInline):
    model = CommentModel
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    

admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
