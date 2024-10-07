from django.forms import ModelForm, widgets
from .models import Detail,Review
from django import forms

class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = ['company', 'model' ,'year' , 'description' , 'image' , 'variant'] 

        widgets = {
            'variant' : forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args , **kwargs)

        # instead of doing the input fields manaually, we do in for loop

        # self.fields['company'].widget.attrs.update({'class':'input' , 'placeholder': 'Enter Text'})
        # self.fields['model'].widget.attrs.update({'class':'input' , 'placeholder': 'Enter Text'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input' , 'placeholder': 'Enter Text'})

class ReviewForm(ModelForm):   
    class Meta:
        model = Review
        fields = ['body']

        labels = {
            'body' : 'Add you comment',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args , **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input' , 'placeholder': 'Enter Text'})