from django.db import models


# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False , null=False)
    description = models.CharField(max_length=200, default="default desc")
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.file.name