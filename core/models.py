from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


class Housing(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="housings"
    )

    def __str__(self):
        return f"{self.location} - {self.user.full_name}"

