from django import forms


class messezentrenForm(forms.ModelForm):
    flug_extra_1 = forms.CharField(max_length=100,required=False)
    flug_extra_2 = forms.CharField(max_length=100,required=False)
    flug_extra_3 = forms.CharField(max_length=100,required=False)
    flug_extra_4 = forms.CharField(max_length=100,required=False)
    flug_extra_5 = forms.CharField(max_length=100,required=False)
    flug_extra_6 = forms.CharField(max_length=100,required=False)
    flug_extra_7 = forms.CharField(max_length=100,required=False)
    flug_save_1 = forms.BooleanField(required=False)
    flug_save_2 = forms.BooleanField(required=False)
    flug_save_3 = forms.BooleanField(required=False)
    flug_save_4 = forms.BooleanField(required=False)
    flug_save_5 = forms.BooleanField(required=False)
    flug_save_6 = forms.BooleanField(required=False)
    flug_save_7 = forms.BooleanField(required=False)
    verkehr_extra_1 = forms.CharField(max_length=100,required=False)
    verkehr_extra_2 = forms.CharField(max_length=100,required=False)
    verkehr_extra_3 = forms.CharField(max_length=100,required=False)
    verkehr_extra_4 = forms.CharField(max_length=100,required=False)
    verkehr_extra_5 = forms.CharField(max_length=100,required=False)

