from django import forms

from main.models import Parse_data


class YearSortedForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ("release_year", "Старше"),
            ("-release_year", "Моложе"),
        ),
        required=False,
        label='Год',
    )


class SearchAppsForm(forms.ModelForm):
    class Meta:
        model = Parse_data
        fields = ["name_company"]