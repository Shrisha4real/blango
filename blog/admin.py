from django.contrib import admin
from blog.models import Posts , Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)  }
    list_display = ("slug" , 'published_at')


admin.site.register(Tag)
admin.site.register(Posts , PostAdmin)

