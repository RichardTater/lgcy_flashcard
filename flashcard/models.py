from django.db import models

# Create your models here.
class Questions(models.Model):
    topic = models.CharField(max_length=100, default="LGCY")
    question_text = models.CharField(max_length=300)
    answer_text = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.question_text

