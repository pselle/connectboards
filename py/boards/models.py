from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField
    cards = ManytoManyField(CardPosition)
    tags = ManytoManyField(Tag)

class CardPosition(models.Model):
    card = models.ForeignKey(Card)
    locationData = models.IntegerField()

class Card(models.Model):
    locations = ManyToManyField(CardPosition)
    # image
    source = models.CharField(max_length=500)
    tags = ManytoManyField(Tag)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    boards = ManytoManyField(Board)
    cards = ManytoManyField(Card)
