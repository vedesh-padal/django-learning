from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_chai, name="all_chai"),
    path("<int:chai_id>/", views.chai_detail, name='chai_detail'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("chai_stores/", views.chai_store_view, name='chai_stores'),
]
