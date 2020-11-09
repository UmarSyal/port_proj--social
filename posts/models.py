from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from groups.models import Group


User = get_user_model()


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')
    message = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message