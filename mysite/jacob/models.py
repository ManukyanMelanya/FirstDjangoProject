import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    def __str__(self): 
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?", )
    
    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
# ete models file chunenq ed depqum makemigration anelis mtnum e app-i mej man e galis bolor classnery voronq jarangvum e Model-ic 
# inqy mez petq e hamakargvac ashxatanqi hamar
# djangoi pahanjn e amen inch lini hamakargvac.
# djangon mez hstak asum e ete inch vor temayov nyut es stexcum ed nuyn anunov file baci u gorcd heshtacru. 

# url-y mer pythonakan funkciayi erkrord anunn e hatuk nshannerov vor browsery, artaqin ashxarhy haskana


