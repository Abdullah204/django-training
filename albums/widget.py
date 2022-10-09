from django import forms

class MyDateTimeInput(forms.DateTimeInput):
        input_type = 'datetime-local'