from django.db import models
from django.utils import timezone
from slugify import slugify
from authors.models import Author
from categories.models import Category


class Post(models.Model):
    STATUS_PUBLISHED = "published"
    STATUS_DRAFT = "draft"
    STATUS_CHOICES = [(STATUS_PUBLISHED, STATUS_PUBLISHED), (STATUS_DRAFT, STATUS_DRAFT)]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == self.STATUS_PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title