from django.db import models
from django.conf import settings

class UploadedImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=200, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.uploaded_at}"
