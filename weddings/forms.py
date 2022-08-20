from django.forms import ModelForm
from .models import Wedding
from django import forms


class WeddingForm(ModelForm):
    class Meta:
        model = Wedding
        fields = ['title','featured_image', 'description', 'url_link', 'source_link', 'tags']
        widgets = {

'tags':forms.CheckboxSelectMultiple

}

def __init__(self, *args, **kwargs):

 super(WeddingForm, self).__init__(*args, **kwargs)

 self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add a title'})

def __init__(self, *args, **kwargs):

 super(WeddingForm, self).__init__(*args, **kwargs)

 for label, field in self.fields.items():

  field.widget.attrs.update({'class':'input'})
