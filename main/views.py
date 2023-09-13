from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kevin Gilbert Sinaga',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
