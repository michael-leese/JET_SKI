from ninja import Router, Schema
from django.utils import timezone
from core.models import Experience, Booking

router = Router()

class ExperienceOut(Schema):
    id: int; name: str; description: str; duration_min: int; base_price: int

@router.get("/experiences", response=list[ExperienceOut])
def list_experiences(request):
    qs = Experience.objects.filter(active=True).order_by("name")
    return [ExperienceOut(**{
        "id": e.id, "name": e.name, "description": e.description,
        "duration_min": e.duration_min, "base_price": e.base_price
    }) for e in qs]

class BookingIn(Schema):
    name: str; email: str; experience_id: int; start_time: str

class BookingOut(Schema):
    booking_id: int; status: str; payment_required: bool

@router.post("/bookings/create", response=BookingOut)
def create_booking(request, payload: BookingIn):
    exp = Experience.objects.get(id=payload.experience_id)
    start = timezone.datetime.fromisoformat(payload.start_time)
    b = Booking.objects.create(
        name=payload.name, email=payload.email, experience=exp, start_time=start
    )
    return {"booking_id": b.id, "status": b.status, "payment_required": True}
