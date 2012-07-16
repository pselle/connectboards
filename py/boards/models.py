from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    cards = ManytoManyField(Card)

class Card(models.Model):
    boards = ManyToManyField(Board)