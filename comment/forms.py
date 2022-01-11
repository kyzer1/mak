from django import forms
from django.forms.widgets import Widget
from .models import Comment
from product.models import Product
from customer_profile.models import CustomerProfile

class CommentForm(forms.Form):
    rate_choices = [
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****')
    ]
    rate = forms.ChoiceField(choices = rate_choices)
    comment = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control" , "id":"textarea-form" , "rows":"6" ,"placeholder":"نظر شما *"}),label="" )
    # product = forms.ModelChoiceField(queryset=Product.objects.all())
    # customer =forms.ModelChoiceField(queryset=CustomerProfile.objects.all())

    
        


