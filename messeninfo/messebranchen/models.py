from django.db import models
from django.forms import ImageField


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
    image1 = models.ImageField(null=True, blank=True, upload_to="static/small")
    image2 = models.ImageField(null=True, blank=True, upload_to="static/large")

    def __str__(self):
        return self.title
  
        super().save(*args, **kwargs)

        if self.image1:
           img1 = Image.open(self.image1.path)
           if img1.height > 1500 or img1.width > 1500:
              output_size = (1500, 1500)
              img1.thumbnail(output_size)
              img1.save(self.image1.path)
    
        if self.image2:
           img2 = ImageField.open(self.image2.path)
           if img2.height > 1500 or img2.width > 1500:
              output_size = (1500, 1500)
              img2.thumbnail(output_size)
              img2.save(self.image2.path)