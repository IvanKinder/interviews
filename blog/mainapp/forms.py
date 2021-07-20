from django import forms

from mainapp.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'text', 'picture',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
