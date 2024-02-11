from django import forms
from django.core.exceptions import ValidationError


class IndexForms(forms.Form):
    entry_time = forms.TimeField(
        label='زمان ورود',
        initial='08:30:00',
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    holidays = forms.IntegerField(
        label='تعداد روزهای تعطیل هفته',
        initial=0,
    )

    two_days_weekend = forms.ChoiceField(
        label='پنجشنبه میای ؟',
        choices=(
            (0, 'آره'),
            (1, 'نه'),
        ),
        widget=forms.Select(),
    )

    def clean_holidays(self):
        holidays = self.cleaned_data['holidays']
        if holidays >= 0:
            return holidays
        raise ValidationError("wrong input")
