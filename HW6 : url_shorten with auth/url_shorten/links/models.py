from django.db import models
import random
import string

class Link(models.Model):
    link = models.URLField()

    @classmethod
    def get_all_links(cls):
        return [link.link for link in Link.objects.all()]

    def get_key(self):
        return self.key.key


class Key(models.Model):
    key = models.CharField(max_length=5)
    link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    redirect_count = models.IntegerField()

    @classmethod
    def get_all_keys(cls):
        return [key.key for key in Key.objects.all()]

    @classmethod
    def create_key(cls):
        new_key = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        while new_key in cls.get_all_keys():
            new_key = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        return new_key

    def get_link(self):
        return self.link.link

    def add_redirect(self):
        self.redirect_count += 1

