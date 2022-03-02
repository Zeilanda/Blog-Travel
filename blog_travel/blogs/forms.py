from typing import List, Tuple

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
        # print('user_id in kwargs')
        # print(kwargs)
        # print('args')
        # print(args)
        tags: django.forms.models.ModelMultipleChoiceField = self.fields['tags']
        # print(tags)
        # print(dir(tags))

    def save(self, commit=True):
        # own logic
        list_of_tags = self.cleaned_data['tags'].split(',')
        new_tags_and_id: List[Tuple[str, int]] = []
        for new_tag in list_of_tags:
            data_tag: Tuple[Tag, bool] = Tag.objects.get_or_create(name=new_tag)
            new_tags_and_id.append((data_tag[0].name, data_tag[0].id))

        tags_id = []
        for tuple_of_name_id_tag in new_tags_and_id:
            tags_id.append(tuple_of_name_id_tag[1])

        self.cleaned_data['tags'] = tags_id
        result: Post = super().save(commit=True)
        return result


class PostUpdateForm(ModelForm):
    tags = CharField()

    class Meta:
        model = Post
        fields = ('title', 'body', 'tags')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tags: django.forms.models.ModelMultipleChoiceField = self.fields['tags']

    def save(self, commit=True):
        # own logic
        list_of_tags = self.cleaned_data['tags'].split(',')
        new_tags_and_id: List[Tuple[str, int]] = []
        for new_tag in list_of_tags:
            data_tag: Tuple[Tag, bool] = Tag.objects.get_or_create(name=new_tag)
            new_tags_and_id.append((data_tag[0].name, data_tag[0].id))

        tags_id = []
        for tuple_of_name_id_tag in new_tags_and_id:
            tags_id.append(tuple_of_name_id_tag[1])

        self.cleaned_data['tags'] = tags_id
        result: Post = super().save(commit=True)
        return result
