
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from .models import Subscriber, Newsletter
from .forms import SubscriberForm, NewsletterForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'system/subscribe_success.html', {'message': 'Subscription successful'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'system/subscribe.html', {'form': SubscriberForm()})

def subscribe_success(request):
    return render(request, 'system/subscribe_success.html')

def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            return JsonResponse({'message': 'Newsletter created successfully', 'newsletter_id': newsletter.id}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'system/create_newsletter.html', {'form': NewsletterForm()})

def send_newsletter(request, newsletter_id):
    newsletter = get_object_or_404(Newsletter, id=newsletter_id)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        send_mail(
            newsletter.subject,
            newsletter.body,
            'your-email@gmail.com',
            [subscriber.email],
            fail_silently=False,
        )
    newsletter.sent = True
    newsletter.save()
    return JsonResponse({'message': 'Newsletter sent successfully'}, status=200)
