from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    first_part = models.CharField(max_length=30, null=True, blank=True)
    second_part = models.CharField(max_length=30, null=True, blank=True)
    is_archive = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class Information(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    yt_link = models.CharField(max_length=255, null=True, blank=True)
    useful_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.sub_title


class CountTake(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    exam_count = models.IntegerField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam_count
