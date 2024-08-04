from django.db import models

class Subscriber(models.Model):
    email= models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.email
        return self.email

class Newsletter(models.Model):
    title = models.CharField(max_length=300);
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject



