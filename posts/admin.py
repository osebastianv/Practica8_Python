from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from datetime import datetime
from posts.models import Category, Post

admin.site.register(Category)
#admin.site.register(Post)

@register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['title', 'owner_name', 'published', 'published_on', 'url_html', 'get_categories']
    list_filter = ['owner', 'published', 'categories']
    search_fields = ['title', 'owner__first_name', 'owner__last_name', 'owner__username']

    def owner_name(self, post):
        return '{0} {1}'.format(post.owner.first_name, post.owner.last_name)

    def get_categories(self, post):
        return "\n".join([c.name for c in post.categories.all()])

    owner_name.short_description = 'Owner\'s name'
    owner_name.admin_order_field = 'owner__first_name'

    def url_html(self, post):
        if post.content_type != None:
            if 'video' in post.content_type:
                return mark_safe('<video width="100" controls><source src="{0}" type="{1}"></video>'
                                 .format(post.url.url, post.content_type))
            else:
                return mark_safe('<img src="{0}" alt="{1}" title="{2}" width="100">'
                                 .format(post.url.url, post.title, post.title))
        else:
            return "No file"

    url_html.short_description = 'URL'
    url_html.admin_order_field = 'url'

    get_categories.short_description = 'CATEGORIES'

    readonly_fields = ['content_type', 'published_on', 'created_on', 'modified_on', 'url_html']

    fieldsets = [
        ['Author', {
            'fields': ['owner']
        }],
        ['Post', {
            'fields': ['title', 'intro', 'body']
        }],
        ['Attributtes', {
            'fields': ['url', 'content_type', 'published', 'published_on']
        }],
        ['Important dates', {
            'fields': ['created_on', 'modified_on', 'url_html']
        }]
    ]

    def save_model(self, request, obj, form, change):
        """
        Casos de uso del campo url (FileField)
        1. Insert Empty, update empty to empty: url = None
        2. Insert Image, update empty to Image, update Image to other Image: url.content_type = "image/...", "video/..."
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
