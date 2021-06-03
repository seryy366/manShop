from django import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField(label='Введите купон:', widget=forms.TextInput(attrs={
    "class": "form-control again", 
    "placeholder": "Coupon code",
    "autocomplete": "off",
    }))