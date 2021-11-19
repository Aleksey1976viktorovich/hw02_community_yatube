from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True,
    # verbose_name="URL")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey('Group', blank=True, null=True,
                              on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #    return reverse('group_posts', kwargs={'group_slug', self.slug})


class Group(models.Model):
    # Имя(title) — название группы. CharField(max_length=None, **options)
    title = models.CharField(max_length=200)
    # Адрес(slug) — уникальный адрес группы.
    # SlugField(max_length=50, **options).
    slug = models.SlugField(max_length=255, unique=True, db_index=False,
                            verbose_name="URL")
    # Описание(description) — текст, описывающий сообщество.Этот текст будет
    # отображаться на странице сообщества.
    description = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #    return reverse('group_posts', kwargs={'group_slug', self.slug})

