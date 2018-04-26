from django.shortcuts import render


def main(request):
    page = 'main'
    return render(request, 'index.html', {'page': page})

def services(request):
    page = 'services'
    return render(request, 'services.html', {'page': page})

# def blog(request):
#     page = 'blog'
#     return render(request, 'blog.html', {'page': page})

def reviews(request):
    page = 'reviews'
    return render(request, 'reviews.html', {'page': page})

def contacts(request):
    page = 'contacts'
    return render(request, 'contacts.html', {'page': page})
