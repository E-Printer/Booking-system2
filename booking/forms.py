from .models import Booking, Session
from django import forms
from django.core.mail import send_mail

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("session", "date", "time")  # Updated field
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Populate the session field with dynamic choices from Session
        self.fields['session'].choices = [
        (session.id, session.name) for session in Session.objects.all()
    ]

    # Add custom attributes for each session (price, duration)
        for session in Session.objects.all():
            self.fields['session'].widget.attrs[f'data-price-{session.id}'] = session.price
            self.fields['session'].widget.attrs[f'data-duration-{session.id}'] = session.duration


