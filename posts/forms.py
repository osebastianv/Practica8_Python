from django.template.defaultfilters import filesizeformat
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from posts.models import Post


class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner']

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url is not None:
            content_type = url.content_type.split('/')[0]
            if content_type not in settings.CONTENT_TYPES:
                raise ValidationError('El archivo no es válido, solo permite imágenes o videos')
            if url.size > int(settings.MAX_UPLOAD_SIZE):
                raise ValidationError('Por favor, conserve el tamaño del archivo por debajo %(value)s. '
                                      'Tamaño actual: %(value2)s',
                          params={'value': filesizeformat(settings.MAX_UPLOAD_SIZE),
                                  'value2': filesizeformat(url.size)})
        return url
