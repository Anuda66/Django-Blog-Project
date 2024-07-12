from django.contrib import admin
from .models import postModel, comments

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')

admin.site.register(postModel,PostModelAdmin)
admin.site.register(comments)
