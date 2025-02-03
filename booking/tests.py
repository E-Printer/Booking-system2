from django.test import TestCase
from django.contrib.auth.models import User
from booking.models import Booking, Session
from datetime import date, time, timedelta
from django.core.exceptions import ValidationError


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



