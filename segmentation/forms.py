#from django import forms
from .models import Data
from django import forms


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['Company','industry', 'location', 'size', 'founded', 'ResponsiveOrNot', 'SSL_TLS', 'Expiry_status', 'Count_contact', 'Count_records','Count_Analytics']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Company'].label = 'Company Name or Website'
        self.fields['industry'].label = 'Industry'
        self.fields['location'].label = 'Location or region'
        self.fields['size'].label = 'How many employees?'
        self.fields['founded'].label = 'when was the company founded?'
        self.fields['ResponsiveOrNot'].label = 'Is your website Responsive? '
        self.fields['SSL_TLS'].label = 'Do You have SSL or TLS enabled?'
        self.fields['Expiry_status'].label = 'Is it expired?'
        self.fields['Count_contact'].label = 'How many contact panels are listed in the website ( including Email, phone number, Linkedin...) '
        self.fields['Count_records'].label = 'do you  have SPF or Dmarc records'
        self.fields['Count_Analytics'].label = 'do you  have Google Analytics ID or AdSense ID or Meta ID ...'
        for field in self.fields.values():
            field.required = False