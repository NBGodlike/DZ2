from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label='Name',required=False)
    duration = forms.CharField(label='Duration',required=False)
    teacher = forms.CharField(label='Teacher', required=False)
    value = forms.CharField(label='Value', required=False)
    picture = forms.ImageField(label='Picture', required=False)

