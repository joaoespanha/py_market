from .models import Item
from django import forms

INPUT_CLASS = "w-full py-4 px-6  rounded-xl"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "price", "category", "description", "image", "is_sold")
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASS}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASS}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASS}),
            "is_sold": forms.CheckboxInput(attrs={"class": INPUT_CLASS}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "price", "category", "description", "image", "is_sold")
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASS}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASS}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASS}),
            "is_sold": forms.CheckboxInput(attrs={"class": INPUT_CLASS}),
        }
