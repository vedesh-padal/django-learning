from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=ChaiVariety.objects.all(),
        label="Select Chai Variety",
        empty_label="Choose a variety...",
        widget=forms.Select(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg bg-white text-gray-700 focus:outline-none focus:ring-2 focus:ring-amber-500"
            }
        ),
    )
