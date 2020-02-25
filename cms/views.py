from django.shortcuts import render, get_object_or_404, redirect
from cms.models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from cms import test_function

# Create your views here.
def home(request):

    ############ getting username who is logged in ###############
    
    username = None
    username = request.user
    print(username)

    ##############################################################

    ############## testing external py file's function in views #####################

    r = test_function.addition(5,6)
    print("the value of r is: ", r)

    ################# testing external py file's class based function on views #############

    p1 = test_function.sajid(30, 40)
    s = p1.add()
    print("the value of s from the class based function is: ", s)

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

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name','email','phone','info','gender','image']
    success_url = '/'

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name','email','phone','info','gender','image']
    
    def form_valid(self, form):
        instance = form.save()
        return redirect('detail', instance.pk)

# class ContactDeleteView(DeleteView):
#     model = Contact
#     template_name = 'delete.html'
#     success_url = '/'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = '/'



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


def Delete(request, id):
    contact_information = Contact.objects.get(pk = id)
    contact_information.delete()
    return redirect('home')
