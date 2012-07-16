from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cards = models.ManyToManyField('CardPosition')
    tags = models.ManyToManyField('Tag')

class CardPosition(models.Model):
    theCard = models.ForeignKey('Card')
    locationData = models.IntegerField()

class Card(models.Model):
    locations = models.ManyToManyField('CardPosition')
    # image
    source = models.CharField(max_length=500)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=200)
    boards = models.ManyToManyField('Board')
    cards = models.ManyToManyField('Card')
