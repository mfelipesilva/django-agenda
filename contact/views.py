from django.shortcuts import render

# A função que utilizar render é utilizada para
# renderizar um template
def index(request):
    return render(
        request,
        'contact/index.html'
    )