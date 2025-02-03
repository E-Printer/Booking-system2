from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date


class Session(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    duration = models.IntegerField(
        help_text="Duration in minutes",
        validators=[MinValueValidator(1)],  # Ensure positive duration
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        help_text="Price",
        validators=[MinValueValidator(0)],  # Ensure non-negative price
    )
    max_occupancy = models.IntegerField(
        default=30,
        validators=[
            MinValueValidator(1),  # Minimum occupancy is 1
            MaxValueValidator(30),  # Maximum occupancy is 30
        ],
        help_text="Maximum number of participants (1-30)",
    )

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["-created_on"]
        constraints = []

    def __str__(self):
        return (
            f"Booking for {self.customer.username}, "
            f"doing {self.session.name} at {self.time.strftime('%H:%M')} on {self.date}."
        )

    def clean(self):
        """
        Ensure that the booking date is not in the past.
        """
        if self.date < date.today():
            raise ValidationError("The booking date cannot be in the past.")
        
        super().clean()

