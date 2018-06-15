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

        """
        Casos de uso del campo url (FileField)
        1. Insert Empty, update empty to empty: url = None
        2. Insert Image, update empty to Image, update Imag to other Image: url.content_type = "image/...", "video/..."
        3. Clear Image (Image to empty): url = False. Para detectar este caso compruebo si existe url.name
        """
        url = form.cleaned_data['url']
        if url == None:
            # No exists image / video
            obj.url = None
            obj.content_type = None
        else:
            # Exists image / video
            name_exits = hasattr(url, 'name')
            if name_exits == True:
                # Exists image / video
                content_type_exits = hasattr(url, 'content_type')
                if content_type_exits == True:
                    # Image is changed
                    # Updated content_type
                    obj.content_type = url.content_type
            else:
                # Clear image / video
                obj.url = None
                obj.content_type = None

        """
        Si se publica se incluye la fecha de publicación
        """
        published = form.cleaned_data['published']

        if published == True:
            if obj.published_on == None:
                obj.published_on = datetime.now()
        else:
            obj.published_on = None

        super(PostAdmin, self).save_model(request, obj, form, change)
