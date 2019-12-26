from pprint import pprint

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, Relationship


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_is_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            if form.cleaned_data['is_main']:
                count_is_main += 1
            pprint(form.cleaned_data)
        print(count_is_main)
        if count_is_main > 1:
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline, ]

