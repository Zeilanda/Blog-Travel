import logging
from typing import List, Tuple

import django
from django.core.exceptions import ValidationError
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.forms import ModelForm, BooleanField, ModelMultipleChoiceField, CharField, TextInput, Textarea, \
    model_to_dict

from blogs.models import Post, Tag, Comment
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
        list_of_clean_tags = []
        for tag in list_of_tags:
            clean_tag = tag.strip()
            list_of_clean_tags.append(clean_tag)
        new_tags_and_id: List[Tuple[str, int]] = []
        for new_tag in list_of_clean_tags:
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
        # opts = self._meta
        # instance = kwargs["instance"]
        # object_data = model_to_dict(instance, opts.fields, opts.exclude)
        # print("object_data", repr(object_data))
        # kwargs["initial"]["tags"] = "some"
        super().__init__(*args, **kwargs)
        # tags: django.forms.models.ModelMultipleChoiceField = self.fields['tags']
        # print('user_id in kwargs')
        # print(kwargs)
        print("initial", self.initial)
        res = self.initial["tags"]
        res = [repr(tag) for tag in res]
        tags_string = ', '.join(res)
        self.initial["tags"] = tags_string
        # print('args')
        # print(self.fields)
        # print(self.fields.values())
        # print(self.as_table().split('\n')[3])
        # self.fields['tags'].value = 'name'
        # print(self.as_table().split('\n')[3])

    def save(self, commit=True):
        # own logic
        list_of_tags = self.cleaned_data['tags'].split(',')
        # print(self.fields.values())
        list_of_clean_tags = []
        for tag in list_of_tags:
            clean_tag = tag.strip()
            list_of_clean_tags.append(clean_tag)
        # print(list_of_clean_tags)

        new_tags_and_id: List[Tuple[str, int]] = []
        for new_tag in list_of_clean_tags:
            data_tag: Tuple[Tag, bool] = Tag.objects.get_or_create(name=new_tag)
            new_tags_and_id.append((data_tag[0].name, data_tag[0].id))

        tags_id = []
        for tuple_of_name_id_tag in new_tags_and_id:
            tags_id.append(tuple_of_name_id_tag[1])

        self.cleaned_data['tags'] = tags_id
        result: Post = super().save(commit=True)
        return result


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

    widgets = {
        'name': TextInput(attrs={'class': 'form-control'}),
        'body': Textarea(attrs={'class': 'form-control'})
    }