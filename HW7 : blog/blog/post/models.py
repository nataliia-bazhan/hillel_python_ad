from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40)
    created_by = models.ForeignKey(
                                    User, on_delete=models.CASCADE, related_name="author_post"
                                     )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    def get_author(self):
        return self.created_by.username

    def when_published(self):
        now = timezone.now()
        since = now - self.created_at
        days = since.days
        seconds = since.seconds

        if days == 0:
            if seconds >= 3600:
                hours = int(seconds / 3600)
                if hours == 1:
                    return f"{hours} hour ago"
                else:
                    return f"{hours} hours ago"
            else:
                minutes = int(seconds / 60)
                if minutes == 1:
                    return f"{minutes} minute ago"
                else:
                    return f"{minutes} minutes ago"
        elif days == 1:
            return f"{days} day ago"
        else:
            return f"{days} days ago"

    def get_absolute_url(self):
        return reverse('post:post', args=[self.id])

