from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    banner = models.FileField(upload_to='media/img_post')
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True)
    auth = models.ForeignKey(User, default=User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    resume = models.TextField(max_length=499, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    img_post = models.FileField(upload_to='media/post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


