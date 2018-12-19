from django.shortcuts import render

##
## ROTAS LIBERADAS
##

def cover(request):
    return render(request, 'cover.html')

def sobre(request):
    return render(request, 'sobre.html')


##
## ROTAS PROTEGIDAS
##

def home(request):
    return render(request, 'home.html')
