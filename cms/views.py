from django.shortcuts import render
from cms.models import Contact

# Create your views here.
def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'index.html', context)


def detail(request):
    return render(request, 'detail.html')


def search(request):
    return render(request, 'search.html')
