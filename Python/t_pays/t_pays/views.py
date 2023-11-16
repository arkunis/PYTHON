from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bonjour, j'ai tous mes pays.</h1>")