from django import forms
from .models import Form133, Form133Next
from datetime import date
from django.utils import timezone

class Form133Form(forms.ModelForm):
    class Meta:
        model = Form133
        fields = ['incident_nr', 'incident_naam', 'datum', 'locatie']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
            'incident_nr': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datum'].initial = date.today()

class Form133NextForm(forms.ModelForm):
    class Meta:
        model = Form133Next
        fields = ['incident_nr', 'incident_naam', 'locatie', 'datum', 'tijd', 'team', 'bericht']

        widgets = {
            'datum': forms.HiddenInput(),
            'tijd': forms.TimeInput(format='%H:%M:%S', attrs={'type': 'time'}),
            'incident_nr': forms.HiddenInput(),
            'incident_naam': forms.HiddenInput(),
            'locatie': forms.HiddenInput(),
            'bericht': forms.TextInput(attrs={'style': 'width: 500px;'}),
            'team': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datum'].initial = timezone.localdate()
        self.fields['tijd'].initial = timezone.localtime().strftime("%H:%M")
        try:
            laatste = Form133Next.objects.latest('id')
            self.fields['incident_naam'].initial = laatste.incident_naam
            self.fields['locatie'].initial = laatste.locatie
        except Form133Next.DoesNotExist:
            pass

    