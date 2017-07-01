from django.db import models

from django.utils import timezone
# Create your models here.

class CodeSnippet(models.Model):
    created = models.DateTimeField(default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())
    snippet = models.TextField(blank=False, null=False)

    def __str__(self):
        """ Sensible string representation of a code snippet."""
        return "{0} \n created at: {1} modified at: {2}".format(self.snippet, self.created, 
                self.modified)

    def save(self, *args, **kwargs):
        """ Add created_at and updated_at timestamps. """
        if not self.id:
            self.created = timezone.now()

        self.modified = timezone.now()

        return super(CodeSnippet, self).save(*args, **kwargs)