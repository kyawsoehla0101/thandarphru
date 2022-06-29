from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from base.models import Category, Post,Gallery, Tag

# Contact
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Gallery)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id','title','slug','author','category',)

admin.site.register(Post, PostAdmin)