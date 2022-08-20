import uuid
from django.db import models
from users.models import Profile


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)
    def __str__(self):
        return self.name


class Wedding(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    ote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
         ('down', 'Down Vote'),
    )
    Wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return self.value    

