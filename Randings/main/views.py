from django.shortcuts import render, redirect
from django.apps import apps

Randeveryday = apps.get_model("main", "Randeveryday")
RandboredObject = apps.get_model("main", "Randbored")

# Create your views here.


def home(request):
    return render(request, "home.html")

def randeveryday(request):
    if request.user.is_authenticated:
        user_options = Randeveryday.objects.get(username=request.user.username)
        options_list = str(user_options.options).split("; ")
        options_list = options_list[:-1]
        try:
            today_option = options_list[0]
            options_list = options_list[1:]
            print(today_option)
            print("---------")
            user_options_str = ""
            for option in options_list:
                user_options_str += f"{option}; "
            user_options.options = user_options_str
            user_options.save()
            data = {
                "task": today_option,
            }
            return render(request, "randeveryday.html", data)
        except IndexError:
            user_options = Randeveryday.objects.get(id=int(request.user.id)-1)
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
            user_options.options = every_option
            user_options.save()
            return redirect("/randeveryday")
    else:
        data = {
            "error": "You aren't logged in",
            "error_content": "You cannot access this page since you haven't logged in this site"
        }
        return render(request, "errors.html", data)


class Randbored:
    def choose(self, request):
        return render(request, "randbored/choose.html")

    def math(self, request):
        if request.method == "POST":
            q1_ans = float(request.POST['q1'])
            q2_ans = int(request.POST['q2'])
            q3_ans = float(request.POST['q3'])
            q4_ans = int(request.POST['q4'])
            q5_ans = float(request.POST['q5'])
            q6_ans = int(request.POST['q6'])
            q7_ans = int(request.POST['q7'])
            q8_ans = int(request.POST['q8'])
            q9_ans = int(request.POST['q9'])
            q10i_ans = int(request.POST['q10i'])
            q10ii_ans = int(request.POST['q10ii'])
            q10iii_ans = int(request.POST['q10iii'])

            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10i, q10ii, q10iii = 1.5, 180, 42.90, 30, 3.42, 10, 24, 12, 10, 17, 19, 21
            q1_true, q2_true, q3_true, q4_true, q5_true, q6_true, q7_true, q8_true, q9_true, q10_true = False, False, False, False, False, False, False, False, False, False
            if q1_ans == q1:
                q1_true = True
            if q2_ans == q2:
                q2_true = True
            if q3_ans == q3:
                q3_true = True
            if q4_ans == q4:
                q4_true = True
            if q5_ans == q5:
                q5_true = True
            if q6_ans == q6:
                q6_true = True
            if q7_ans == q7:
                q7_true = True
            if q8_ans == q8:
                q8_true = True
            if q9_ans == q9:
                q9_true = True
            if q10i_ans == q10i and q10ii_ans == q10ii and q10iii_ans == q10iii:
                q10_true = True
            
            results = [q1_true, q2_true, q3_true, q4_true, q5_true, q6_true, q7_true, q8_true, q9_true, q10_true]
            for result in results:
                print(result)
            corrected_results = []
            for result in results:
                if result == True:
                    corrected_results.append("Correct")
                else:
                    corrected_results.append("Wrong")
            correct = results.count(True)
            wrong = 10 - correct
            counter = range(1, 11)
            all_zip = zip(counter, corrected_results)
            data = {
                "zip": all_zip,
                "correct": correct,
                "wrong": wrong
            }

            return render(request, "randbored/math_correction.html", data)
        else:
            return render(request, "randbored/math.html")