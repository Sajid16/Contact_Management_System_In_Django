from django.shortcuts import render, get_object_or_404
from cms.models import Contact

# Create your views here.
def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'index.html', context)


def detail(request, id):
    context = {
        'contacts': get_object_or_404(Contact, pk=id)
        # 'contact': COntact.objects.get(pk=id)
    }
    return render(request, 'detail.html', context)


def search(request):
    return render(request, 'search.html')
