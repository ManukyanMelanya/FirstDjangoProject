from django.contrib import admin

from .models import Question
from .models import Choice


# admin.site.register(Question)
# admin.site.register(Choice)
# models=(Question, Choice)
# admin.site.register(models)


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["id","question_text", "pub_date", "was_published_recently"]
    # list_display = ["id", "question_text", "pub_date"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"] #filtrelu hnaravorutyun e talis
    search_fields = ["question_text"] #searchi hamar toxa sarqum


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)




