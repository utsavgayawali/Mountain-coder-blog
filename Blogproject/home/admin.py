from django.contrib import admin
from home.models import Blog
from home.models import Carousel,Contact


class BlogAdmin(admin.ModelAdmin):
     class Media:
         css ={
             "all":('css/admin.css',)
         }
         
         js= ("js/blog.js",)

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Carousel,BlogAdmin)


