from django.contrib import admin
from django.contrib.admin import register

from datetime import datetime
from posts.models import Category, Post

admin.site.register(Category)
#admin.site.register(Post)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        #obj.published_on = request.user

        published = form.cleaned_data['published']

        url = form.cleaned_data['url']

        if published == True:
            if obj.published_on == None:
                obj.published_on = datetime.now()
        else:
            obj.published_on = None

        super(PostAdmin, self).save_model(request, obj, form, change)
