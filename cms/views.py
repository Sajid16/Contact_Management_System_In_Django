from django.shortcuts import render, get_object_or_404
from cms.models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'index.html', context)

#################### creating class based view #########################

class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

class DetailPageView(DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contacts'

####################### class based view end #########################


def detail(request, id):
    context = {
        # 'contacts': get_object_or_404(Contact, pk=id)
        'contacts': Contact.objects.get(pk=id)
    }
    return render(request, 'detail.html', context)


def search(request):
    if request.POST:
        search_term = request.POST['search_term']
        # search_result = Contact.objects.filter(name__icontains = search_term) | Contact.objects.filter(phone__icontains = search_term)
        # search_result = Contact.objects.filter(name__contains = search_term)
        search_result = Contact.objects.filter(Q(name__icontains = search_term) | 
                                               Q(phone__iexact = search_term) |
                                               Q(info__icontains = search_term) |
                                               Q(email__iexact = search_term))
        context = {
            'search_term': search_term,
            'contacts': search_result
        }

    return render(request, 'search.html', context)
