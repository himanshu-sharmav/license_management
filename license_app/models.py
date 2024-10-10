from django.db import models
from django.contrib.auth.models import User

class License(models.Model):
    license_key = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_key


class LicenseRevocation(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    revoked_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"{self.license} revoked on {self.revoked_at}"
