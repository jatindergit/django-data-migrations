from django.db import models


class Author(models.Model):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=200, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
