from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from blogs.models import Post


class PostCreateForm(ModelForm):
    # mark_it = BooleanField(label='super post', required=False)

    class Meta:
        model = Post
        # fields = ('author', 'title', 'text')
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('user_id in kwargs')
        print(kwargs)
        print('args')
        print(args)
        for f_name, f_obj in self.fields.items():
            print(f_name, f_obj)
            f_obj.widget.attrs['class'] = 'form-item'
            # if f_name == 'title':
            #     f_obj.widget = HiddenInput()
            # f_obj.widget.attrs['user_id'] = current_user.id
    #
    # def clean_title(self):
    #     value = self.cleaned_data['title']
    #     # if not value or not value[0].isupper():
    #     if not value[0].isupper():
    #         raise ValidationError('title is not title')
    #
    #     return value

    def save(self, commit=True):
        # own logic
        super().save(commit=commit)
