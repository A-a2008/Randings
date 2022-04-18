from django.db import models
from django.db.models import Model

# Create your models here.


class Randeveryday(Model):
    username = models.CharField(max_length=256)
    all_options = [
        "Do 10 bottle flips",
        "Make a new friend on Discord",
        "Do not use your phone for 2 hours (Excluding sleeping time and attend important calls only)",
        "Sleep at 9PM and wake up at 6AM (Your timezone)",
        "Drink chilled water after waking up",
        "Drink 4 litres of water today",
        "Jog 30 mins in the morning and 30 mins in the evening",
        "Do not watch the television for 4 hours and instead read a book",
        "Make paper planes and fly them",
        "Write an essay on \"The Sun\"",
        "Stich out a design on a waste fabric",
        "Clean up the wardrobe",
        "Replace batteries of old remotes of A.Cs, fans, etc",
        "Play an instrument",
        "Learn the lyrics and sing the song",
        "Write a letter to anyone, not by e-mail",
        "Change the bedsheet and pillow covers",
        "Go to the store room of your house, pick a random item and clean it",
        "Delete unnecessary screenshots and go down the memory lane",
        "Cut your nails (if male). Paint your nails (if female)",
        "Walk down a street and find a homeless person and give 5 units of your currency (Eg. $5, ₹5, etc)"
    ]
    every_option = ""
    for option in all_options:
        every_option += f"{option}; "
    options = models.CharField(max_length=1000, default=every_option)


class Asked(Model):
    username = models.CharField(max_length=256)
    asked = models.BooleanField(default=False)

class EmailSending(Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
