from typing import Union
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import CategoryModel, PostModel

class CategoryModelSitemap(Sitemap):
    def items(self):
        return CategoryModel.objects.all()
    
class PostModelSitemap(Sitemap):
    def items(self):
        return PostModel.objects.filter(status=PostModel.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at