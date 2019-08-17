from django.forms import ModelForm
from myblog.models import Post

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']
