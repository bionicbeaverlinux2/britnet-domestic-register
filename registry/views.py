import random
from django.shortcuts import render, redirect
from .models import Resource
from django.http import HttpResponse

BULLETINS = [
    "Directive 003 remains in force.",
    "The Domestic Register has been updated.",
    "Queue processing rates remain satisfactory.",
    "Citizens are reminded to retain permit documentation.",
    "Registry integrity verified.",
    "Administrative backlog within acceptable limits.",
    "Tea reserves remain adequate.",
    "Long live Britnet.",
]

def registry_home(request):
    query = request.GET.get('q')
    if query:
        resources = Resource.objects.filter(
            classification__in=['CLASS_A', 'CLASS_B'],
            name__icontains=query
        ) | Resource.objects.filter(
            classification__in=['CLASS_A', 'CLASS_B'],
            domain__icontains=query
        )
    else:
        resources = Resource.objects.filter(classification__in=['CLASS_A', 'CLASS_B'])
        
    bulletin = random.choice(BULLETINS)
    return render(request, 'registry/home.html', {
        'resources': resources,
        'bulletin': bulletin,
        'query': query,
    })


def submit_resource(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        domain = request.POST.get('domain')
        # Generate a fictional reference number
        ref_num = f"BRT-{random.randint(100000, 999999)}"
        
        Resource.objects.create(
            name=name,
            domain=domain,
            classification='CLASS_C',
            status='PENDING',
            reference_number=ref_num,
            administrative_notes="Citizen application submitted. Awaiting review."
        )
        return render(request, 'registry/success.html', {'ref_num': ref_num})
        
    return render(request, 'registry/submit.html')
