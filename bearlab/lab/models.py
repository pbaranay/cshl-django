from django.db import models


class Staff(models.Model):
    # id is added implicitly
    name = models.CharField(max_length=127)
    position = models.CharField(max_length=127)
    date_joined = models.DateField()
    # blank makes it optional in forms and validation;
    # null makes it optional in the database
    date_left = models.DateField(blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} ({self.id})'
