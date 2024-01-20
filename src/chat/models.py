from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.CharField(max_length=2048)
    source = models.CharField(max_length=2048, default="")

    def __str__(self):return self.nick

class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    channel_id = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    message_content = models.CharField(max_length=2048)
    author_nick = models.CharField(max_length=20)

    def __str__(self):return self.message_content
