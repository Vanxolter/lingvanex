from django import forms


class YearFilterForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ("-release_year", "Старше"),
            ("release_year", "Моложе"),
        ),
        required=False,
    )