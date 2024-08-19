from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


APN_CHOICES = [
    ('NB-IoT(IPDD)', 'NB-IoT(IPDD)'),
    # Add more choices here
]

class OnboardingForm(forms.Form):
    customer_name = forms.CharField(label='Customer Name', max_length=100)
    iot_product_type = forms.ChoiceField(label='IoT Product Type', choices=APN_CHOICES)
    num_apns = forms.IntegerField(label='No. of APNs required', min_value=1)

    # Dynamically create fields based on the number of APNs
    def __init__(self, *args, **kwargs):
        num_apns = kwargs.pop('num_apns', 1)
        super(OnboardingForm, self).__init__(*args, **kwargs)
        
        for i in range(1, num_apns + 1):
            self.fields[f'apn_{i}_details'] = forms.CharField(
                label=f'APN {i} Details', max_length=100, required=False
            )
