from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class Women(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default=' ')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(unidecode(self.title))
    #     super(Women, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
