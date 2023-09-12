import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    def __str__(self): 
        return self.question_text
    
    # @admin.display(
    #     boolean=True,
    #     ordering="pub_date",
    #     description="Published recently?", )
    
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
class NewModel(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    field1=models.CharField(max_length=200)
    field2 = models.IntegerField(default=0)
    field3 = models.TextField(max_length= 500)
    field4 = models.CharField(max_length=200)
    field5 = models.IntegerField(default=0)
    field6 = models.TextField(max_length= 500)
    field7 = models.CharField(max_length=200)
    field8 = models.IntegerField(default=0)
    field9 = models.TextField(max_length= 500)

class JacobUser(models.Model):
    gender_choice = [(1, "male"), (2,"female"), (3,"unknown")]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    gender = models.PositiveBigIntegerField(choices = gender_choice)

class Questioner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.SmallIntegerField()


class Responder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    gender_choice = [(1, "male"), (2, "female"), (3, "unknown")]
    gender = models.PositiveIntegerField(choices=gender_choice)
