from django.db import models

# Create your models here.
question_choices=(
    ("select","select"),
    ("task","task"),
    ("problem","problem"),
    ("question","question"),
)
ticket_choices=(
    ("high","high"),
    ("low","low"),
    ("medium","medium"),
)

class Ticket(models.Model):
    title=models.CharField(max_length=20)
    content = models.TextField(max_length=250, blank=True)
    question_type=models.CharField(max_length=25,choices=question_choices,default="select")
    ticket_priority=models.CharField(max_length=25,choices=ticket_choices,default=None)