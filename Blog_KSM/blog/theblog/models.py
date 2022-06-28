from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
       return self.title
    #   return self.title + ' | ' + str(self.author)

class ImagePost(models.Model):
    post_title = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    post_images = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
       return self.title + ' . '



