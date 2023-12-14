from django.contrib import admin
from .models import Cathegories, Post, Comments, Tags
admin.site.register(Post)
admin.site.register(Cathegories)
admin.site.register(Comments)
admin.site.register(Tags)
# Register your models here.
