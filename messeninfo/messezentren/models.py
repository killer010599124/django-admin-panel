from django.db import models, connection
from django.utils.html import format_html


# Create your models here.


class messezentren(models.Model):

    def items():
        cursor = connection.cursor()
        cursor.execute('''SELECT id, de FROM `staedte`''')
        columns = [col[0] for col in cursor.description]
        items = cursor.fetchall()
        return items

    def flug1_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_1">Suchen</a>')

    flug1_button.allow_tags = True
    flug1_button.short_description = ""

    def flug2_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_2">Suchen</a>')

    flug2_button.allow_tags = True
    flug2_button.short_description = ""

    def flug3_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_3">Suchen</a>')

    flug3_button.allow_tags = True
    flug3_button.short_description = ""

    def flug4_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_4">Suchen</a>')

    flug4_button.allow_tags = True
    flug4_button.short_description = ""

    def flug5_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_5">Suchen</a>')

    flug5_button.allow_tags = True
    flug5_button.short_description = ""

    def flug6_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_6">Suchen</a>')

    flug6_button.allow_tags = True
    flug6_button.short_description = ""

    def flug7_button(self):
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="flug_button_7">Suchen</a>')

    flug7_button.allow_tags = True
    flug7_button.short_description = ""

    zentren_id = models.IntegerField(primary_key=True)
    firma = models.CharField(max_length=30)
    firma_en = models.CharField(max_length=30)
    firma_fr = models.CharField(max_length=30)
    firma_es = models.CharField(max_length=30)
    firma_ru = models.CharField(max_length=30)
    firma_cn = models.CharField(max_length=30)
    strasse = models.CharField(max_length=30)
    synono = models.TextField(
        max_length=300, null=True, blank=True)  # name synonym
    # hallem2 = models.TextField(max_length=300,null=True,blank=True)
    freim2 = models.TextField(
        max_length=300, null=True, blank=True)  # m2 of ground
    gesamtm2 = models.TextField(
        max_length=300, null=True, blank=True)  # m2 overall
    hallenanzahl = models.TextField(
        max_length=300, null=True, blank=True)  # Quantity of halls
    text_de = models.TextField(max_length=300)
    text_en = models.TextField(max_length=300)
    text_fr = models.TextField(max_length=300)
    text_es = models.TextField(max_length=300)
    text_ru = models.TextField(max_length=300)
    text_cn = models.TextField(max_length=300)
    ort = models.IntegerField(choices=items())
    plz = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    lat = models.CharField(max_length=11)
    lon = models.CharField(max_length=11)
    land_id = models.IntegerField()
    email = models.CharField(max_length=30)
    angelegt = models.DateField()
    hallenm2 = models.IntegerField(null=True, blank=True)  # m2 of ground
    parkplatzanzahl = models.IntegerField(
        null=True, blank=True)  # Quantity of parking
    flug1 = models.IntegerField(null=True, blank=True)  # id table airports
    flug2 = models.IntegerField(null=True, blank=True)  # id table airports
    flug3 = models.IntegerField(null=True, blank=True)  # id table airports
    flug4 = models.IntegerField(null=True, blank=True)  # id table airports
    flug5 = models.IntegerField(null=True, blank=True)  # id table airports
    flug6 = models.IntegerField(null=True, blank=True)  # id table airports
    flug7 = models.IntegerField(null=True, blank=True)  # id table airports
    verkehr1 = models.IntegerField(null=True, default=0)  # bus connection cc
    verkehr2 = models.IntegerField(null=True, default=0)  # transfer parking
    verkehr3 = models.IntegerField(null=True, default=0)  # train station
    verkehr4 = models.IntegerField(null=True, default=0)  # underground
    verkehr5 = models.IntegerField(null=True, default=0)  # suburban train
    anfahrt_de = models.TextField(null=True, blank=True)  # directions
    anfahrt_en = models.TextField(null=True, blank=True)
    anfahrt_fr = models.TextField(null=True, blank=True)
    anfahrt_es = models.TextField(null=True, blank=True)
    anfahrt_cn = models.TextField(null=True, blank=True)
    entfernung_innenstadt = models.IntegerField(blank=True, null=True)
    art_id = models.PositiveIntegerField(blank=True, null=True)
    hotelsuche = models.IntegerField(blank=True, null=True)
    anfahrt_ru = models.TextField(null=True, blank=True)
    hallenanzahl = models.IntegerField(null=True, blank=True)  # m2 of ground
    # hallenazahl = models.IntegerField(null=True, blank=True)  # m2 of ground

    class Meta:
        db_table = "messezentren"
        managed = True

    def __str__(self):
        return self.firma
