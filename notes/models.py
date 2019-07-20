from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    favourite = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        default="Note",
        on_delete=models.CASCADE,
    )


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])

    class Meta:
        ordering = ["-publish", "-updated"]
