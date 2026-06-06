from django.urls import path
from ninja import NinjaAPI
from core.api.public import router as public_router

api = NinjaAPI(title="Jet Ski API", version="0.1")
api.add_router("/api", public_router)

urlpatterns = [
    path("", api.urls),
]
