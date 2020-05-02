from django.shortcuts import render

# Create your views here.
def searchll_listar(request):
    return render(request, 'searchll/listar.html')
    # esta es la ruta del template, donde esta el archivo html
