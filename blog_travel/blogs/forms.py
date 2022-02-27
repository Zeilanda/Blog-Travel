import django
from django.core.exceptions import ValidationError
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.forms import ModelForm, BooleanField, ModelMultipleChoiceField, CharField

from blogs.models import Post, Tag
from register import forms


class PostCreateForm(ModelForm):
    tags = CharField()
    # tags = django.forms.models.ModelMultipleChoiceField(label='super post', required=False)

    class Meta:
        model = Post
        fields = ('title', 'body', 'tags')
    #     fields = ('author', 'title', 'text')
        # exclude = ('author',)
    # def is_valid(self):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('user_id in kwargs')
        print(kwargs)
        print('args')
        print(args)
        tags: django.forms.models.ModelMultipleChoiceField = self.fields['tags']
        print(tags)
        print(dir(tags))
        # tags.clean([1])
        # tags.queryset = Tag.objects.all()
        # tags.queryset = Tag.objects.all()
        # kwargs[]["tags"]
    #     tags_string = kwargs['tags']
    #     print(tags_string)
    #     for f_name, f_obj in self.fields.items():
    #         print(f_name, f_obj)
            # f_obj.widget.attrs['class'] = 'form-item'
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
        # print(self.fields['tags'])
        print("cleaned_data:", self.cleaned_data)
        # self.cleaned_data["tags"] = [2]

        # self.cleaned_data["tags"] = Tag.objects.update_or_create(Tag.name)
        res, created = Tag.objects.get_or_create(name=self.cleaned_data["tags"])
        print(res.id)
        # print(res)
        # print(dir(self.fields['tags']))
        # print('save')
        result: Post = super().save(commit=True)
        result.tags.set(res.id, self.cleaned_data["tags"])
        return result
