from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings


def main(request):
    page = 'main'
    return render(request, 'index.html', {'page': page})

def services(request):
    page = 'services'
    return render(request, 'services.html', {'page': page})

def prices(request):
    page = 'services'
    return render(request, 'prices.html', {'page': page})

def reviews(request):
    page = 'reviews'
    return render(request, 'reviews.html', {'page': page})

def contacts(request):
    page = 'contacts'
    return render(request, 'contacts.html', {'page': page})

def send_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('phone')
        text = request.POST.get('text')

        subject = 'Вопрос с сайта marina-chernousova.ru'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.MAIN_EMAIL]
        contact_message = '''
                Имя............... {}
                Контакты.......... {}
                ------------------
                {}
                '''.format(name, contact, text)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        return HttpResponseRedirect('/sent/')
    else:
        return render(request, 'index.html')

def sent(request):
    return render(request, 'sent.html')