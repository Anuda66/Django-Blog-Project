from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class postModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def commnet_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.title 

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(postModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
    



