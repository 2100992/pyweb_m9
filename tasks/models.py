from django.db import models

# Create your models here.

class TodoItem(models.Model):
    description = models.CharField(max_length=64)
    is_completed = models.BooleanField('выполнено', default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description.lower()
    
    class Meta:
        ordering = ('-created',)