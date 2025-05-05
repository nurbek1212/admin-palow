from django.http import HttpResponse

def home(request):
    return HttpResponse("Salom! Admin Palov loyihasiga xush kelibsiz!")
