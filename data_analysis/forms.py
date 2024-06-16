from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    handling_choice = forms.ChoiceField(
        choices=[
            ('remove', 'Remove Rows with Missing Values'),
            ('mean', 'Fill with Mean'),
            ('median', 'Fill with Median')
        ],
        widget=forms.RadioSelect,
        initial='remove'
    )
