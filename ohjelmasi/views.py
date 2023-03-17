from django.shortcuts import render


def etusivu(reguest):
    context = {
        "user": reguest.user,
    }
    return render(reguest, "etusivu.html", context)