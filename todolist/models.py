from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Tag name")

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(verbose_name="Task description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Deadline")
    is_done = models.BooleanField(default=False, verbose_name="Is complited")
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks", verbose_name="Tags")

    def __str__(self):
        return self.content
