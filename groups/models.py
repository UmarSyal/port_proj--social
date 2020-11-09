from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, default='')
    members = models.ManyToManyField(User, through=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:group_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Group, self).save(*args, **kwargs)    
