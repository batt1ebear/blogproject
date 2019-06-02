from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    name = models.ForeignKey(User)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
