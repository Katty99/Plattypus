from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Notes(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sent_notes')
    recipient = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='received_notes')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result
