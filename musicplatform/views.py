from django.http import HttpResponse

def index(request):
    return HttpResponse("successfully logged in")