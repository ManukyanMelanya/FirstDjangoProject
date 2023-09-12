from django.contrib import admin

from .models import Question
from .models import Choice, JacobUser,NewModel, Questioner,Responder

# admin.site.register(Question)
# admin.site.register(Choice)
# models=(Question, Choice)
# admin.site.register(models)


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


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

class NewModelAdmin(admin.ModelAdmin):
    list_display=["id","question","field3"]
    list_filter =["question"]

class JacobUserAdmin(admin.ModelAdmin):
    list_display=["user_info", "country", "city", "age","gender"]
    list_filter = ["gender"]

    def user_info(self,obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)
    user_info.short_description = "Full name" 

admin.site.register(Question, QuestionAdmin)
admin.site.register((Choice,Responder,Questioner))

admin.site.register(JacobUser, JacobUserAdmin)
admin.site.register(NewModel, NewModelAdmin)






