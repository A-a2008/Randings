from django.urls import path
from .views import *

randbored = Randbored()

urlpatterns = [
    path("", home, name="index"),
    path("randeveryday/", randeveryday, name="randeveryday"),
    path("randbored/", randbored.choose, name="randbored"),
    path("randbored/math/", randbored.math, name="randbored_math"),
    path("randbored/comprehension/", randbored.comprehension, name="comprehension")
]