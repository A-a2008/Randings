from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="index"),
    path("randeveryday/", randeveryday, name="randeveryday"),
    path("randbored/", choose, name="randbored"),
    path("randbored/math/", math, name="randbored_math"),
    path("randbored/comprehension/", comprehension, name="comprehension"),
    path("randbored/exercise/", exercise, name="exercise"),
    path("ask/", asked, name="ask"),
    path("sendemail/", email_send, name="sendemail")
]