from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from booking.models import Booking, Session
from datetime import date, time, timedelta
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class BookingModelTest(TestCase):

    def setUp(self):
        """
        Set up test dependencies: create a user and a session.
        """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.session = Session.objects.create(name="Beginner Lesson", duration=60)
        self.future_date = date.today() + timedelta(days=5)
        self.past_date = date.today() - timedelta(days=1)

    def test_create_booking(self):
        """
        Test that a booking can be successfully created.
        """
        booking = Booking.objects.create(
            customer=self.user,
            session=self.session,
            date=self.future_date,
            time=time(10, 0),
            status="confirmed",
        )
        self.assertEqual(str(booking), f"Booking for testuser, doing Beginner Lesson at 10:00 on {self.future_date}.")
        self.assertEqual(booking.customer, self.user)
        self.assertEqual(booking.session, self.session)
        self.assertEqual(booking.status, "confirmed")

    def test_booking_date_cannot_be_in_past(self):
        """
        Test that creating a booking with a past date raises a ValidationError.
        """
        booking = Booking(
            customer=self.user,
            session=self.session,
            date=self.past_date,
            time=time(10, 0),
            status="confirmed",
        )
        with self.assertRaises(ValidationError) as context:
            booking.clean()
        self.assertIn("The booking date cannot be in the past.", str(context.exception))

    def test_booking_default_status_is_pending(self):
        """
        Test that the default status of a booking is 'pending'.
        """
        booking = Booking.objects.create(
            customer=self.user,
            session=self.session,
            date=self.future_date,
            time=time(14, 30),
        )
        self.assertEqual(booking.status, "pending")

    def test_booking_ordering(self):
        """
        Test that bookings are ordered by 'created_on' in descending order.
        """
        booking1 = Booking.objects.create(
            customer=self.user,
            session=self.session,
            date=self.future_date,
            time=time(9, 0),
        )
        booking2 = Booking.objects.create(
            customer=self.user,
            session=self.session,
            date=self.future_date,
            time=time(11, 0),
        )
        bookings = Booking.objects.all()
        self.assertEqual(bookings.first(), booking2)  # Latest created booking should come first
        self.assertEqual(bookings.last(), booking1)

class SessionModelTest(TestCase):
    def setUp(self):
        """Create a valid session instance for testing."""
        self.session = Session.objects.create(
            name="Beginner Lesson",
            description="Beginner Lesson",
            duration=60,
            price=20.00,
            max_occupancy=15
        )

    def test_session_creation(self):
        """Test if a session is created successfully."""
        self.assertEqual(self.session.name, "Beginner Lesson")
        self.assertEqual(self.session.description, "Beginner Lesson")
        self.assertEqual(self.session.duration, 60)
        self.assertEqual(self.session.price, 20.00)
        self.assertEqual(self.session.max_occupancy, 15)

    def test_name_uniqueness(self):
        """Test that session names must be unique."""
        with self.assertRaises(Exception):  # Should raise IntegrityError
            Session.objects.create(
                name="Beginner Lesson",  # Duplicate name
                description="Another Beginner Lesson",
                duration=45,
                price=15.00,
                max_occupancy=10
            )

    def test_duration_cannot_be_negative_or_zero(self):
        """Test that duration must be at least 1 minute."""
        self.session.duration = 0
        with self.assertRaises(ValidationError):
            self.session.full_clean()  # Triggers validation

    def test_price_cannot_be_negative(self):
        """Test that price must be non-negative."""
        self.session.price = -5.00
        with self.assertRaises(ValidationError):
            self.session.full_clean()

    def test_max_occupancy_out_of_range(self):
        """Test max occupancy cannot be less than 1 or greater than 30."""
        self.session.max_occupancy = 0
        with self.assertRaises(ValidationError):
            self.session.full_clean()

        self.session.max_occupancy = 31
        with self.assertRaises(ValidationError):
            self.session.full_clean()
    
    def test_string_representation(self):
        """Test the string representation of the Session model."""
        self.assertEqual(str(self.session), "Beginner Lesson")