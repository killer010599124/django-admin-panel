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
    
    def get_upload_to1(instance, filename):
        tempname = "%s_%s.%s" % ('small', instance.b_id, 'jpg')
        return 'static/sector_images/%d/%s' % (instance.b_id, tempname)
    def get_upload_to2(instance, filename):
        tempname = "%s_%s.%s" % ('large', instance.b_id, 'jpg')
        return 'static/sector_images/%d/%s' % (instance.b_id, tempname)
    class Meta:
        ordering = ["id"]

    title = models.CharField(null=True,max_length=255, default="title name")
    # language = models.ForeignKey(Language, default=1, on_delete=models.DO_NOTHING)
    # category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    # description = models.TextField(null=True,default="This is Description")
    b_id = models.PositiveIntegerField()
    image1 = models.ImageField(null=True, blank=True, upload_to=get_upload_to1)
    image2 = models.ImageField(null=True, blank=True, upload_to=get_upload_to2)

    def __str__(self):
        return self.title
class Branchen(models.Model):
    b_id = models.PositiveIntegerField()
    sprach_id = models.PositiveIntegerField()
    text = models.CharField(max_length=255)
    cnsort = models.CharField(max_length=10, blank=True, null=True)
    messe_text = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True, null=True)
    google = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branchen'