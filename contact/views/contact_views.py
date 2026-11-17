from django.shortcuts import render
from contact.models import Contact

# A função que utilizar render é utilizada para
# renderizar um template
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )