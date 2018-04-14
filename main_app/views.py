from django.shortcuts import render


def main(request):
    page = 'main'
    return render(request, 'index.html', {'page': page})


