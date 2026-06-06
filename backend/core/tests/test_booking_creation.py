import pytest
from django.utils import timezone
from core.models import Experience, Booking

@pytest.mark.django_db
def test_create_pending_booking():
    e = Experience.objects.create(slug="taormina", name="Taormina Jet Ski", description="", duration_min=60, base_price=15000)
    b = Booking.objects.create(name="Test User", email="test@example.com", experience=e, start_time=timezone.now())
    assert b.status == "pending"
