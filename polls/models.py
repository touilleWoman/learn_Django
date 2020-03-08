import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # Foreignkey: A many-to-one relationship. 
    # Requires a positional argument: the class to which the model is related.
    # each Choice is related to a single Question.
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default=0) 
    def __str__(self):
        return self.choice_text       


''' python manage.py migrate
migrate convert object model to table

pk is short for primary key
by default, id is set to be primary key

Un queryset est une liste d'objets d'un modèle donné.

'''