from django.db import models


class Language(models.Model):
    language_name = models.CharField(max_length=255)

    def __str__(self):
        return self.language_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class TradeFair(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=255, default="title name")
    language = models.ForeignKey(Language, default=1, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    description = models.TextField(default="delicious")
    image1 = models.ImageField(null=True, blank=True, upload_to="images/large")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/small")

    def __str__(self):
        return self.title
