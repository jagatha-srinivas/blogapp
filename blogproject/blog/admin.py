from django.contrib import admin

# Register your models here.

from blog.models import Post,Comment



class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','publish')

    prepopulated_fields={'slug':('title',)}
    search_fileds=('title','body')


class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fileds=('name','email','body')




admin.site.register(Post,PostAdmin)

admin.site.register(Comment,CommentAdmin)
