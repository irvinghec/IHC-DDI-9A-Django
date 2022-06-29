from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
#modelo vista controlador= MVC Acciones (Metodos)
#modelo vista template = MVT Acciones (Metodos)
layout = """
    <h1> Bienvenido a la pagina de inicio </h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">inicio</a>
        </li>
        <li>
            <a href="/hola-django">Hola Django</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    </hr>

"""

def index(request):
    html = """
    """
    year = 2022
    while year <= 2060:
        if year % 2 == 0:
            html+= f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"

    #return HttpResponse(layout+html
    return render(request, 'index.html')
def hola_django(request):
    return render(request, 'hola_django.html')


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto',nombre="irving", apellidos="hernandez")
    return render(request, 'pagina.html')
    
def contacto(request, nombre="", apellidos=""):
    html=""
    if nombre and apellidos:
        html+= "<p> El nombre completo es: </p>"
        html+= f"<h3>{nombre} {apellidos}</p>"
    return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos}</h2>"+html)