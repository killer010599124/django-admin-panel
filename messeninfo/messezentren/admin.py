from django.contrib import admin
from .models import messezentren
from .forms import messezentrenForm


# Register your models here.

@admin.register(messezentren)
class messezentrenClass(admin.ModelAdmin):
    change_form_template = "messezentren_cahngeform.html"

    class Media:
        js = ('custom/js/messezentren.js',)

    form = messezentrenForm
    readonly_fields = (
        'flug1_button', 'flug2_button', 'flug3_button', 'flug4_button', 'flug5_button', 'flug6_button',
        'flug7_button',)

    fieldsets = (
        (None, {
            "fields": (

                ('firma', 'firma_en', 'firma_fr', 'firma_es', 'firma_ru', 'firma_cn', 'synono', 'freim2', 'gesamtm2',
                 'strasse', 'text_en', 'text_de', 'text_fr', 'text_es', 'text_ru', 'text_cn', 'lat', 'lon', 'ort',
                 'plz', 'tel', 'fax', 'url', 'land_id', 'email', 'angelegt', 'hallenm2',
                 ('flug_save_1', 'flug1', 'flug_extra_1', 'flug1_button'), ('flug_save_2', 'flug2', 'flug_extra_2', 'flug2_button'),
                 ('flug_save_3', 'flug3', 'flug_extra_3', 'flug3_button'), ('flug_save_4', 'flug4', 'flug_extra_4', 'flug4_button'),
                 ('flug_save_5', 'flug5', 'flug_extra_5', 'flug5_button'), ('flug_save_6', 'flug6', 'flug_extra_6', 'flug6_button'),
                 ('flug_save_7', 'flug7', 'flug_extra_7', 'flug7_button'), ('verkehr1', 'verkehr_extra_1'),
                 ('verkehr2', 'verkehr_extra_2'), ('verkehr3', 'verkehr_extra_3'), ('verkehr4', 'verkehr_extra_4'),
                 ('verkehr5', 'verkehr_extra_5'),
                 'anfahrt_de', 'anfahrt_en', 'anfahrt_fr', 'anfahrt_es', 'anfahrt_cn', 'anfahrt_ru', 'hallenanzahl')
            ),
        }),
    )
