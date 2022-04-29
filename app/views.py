from ssl import ALERT_DESCRIPTION_RECORD_OVERFLOW
from django.shortcuts import render

# Create your views here.

def contacto(request):
    return render(request, 'app/contacto.html')

def index(request):
    return render(request, 'app/index.html')

def iniciarsesion(request):
    return render(request, 'app/iniciar-sesion.html')

def quienessomos(request):
    return render(request, 'app/quienes-somos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

            # MI-CUENTA

def carritocompras(request):
    return render(request, 'app/mi-cuenta/carrito-compras.html')

def finalizarcompra(request):
    return render(request, 'app/mi-cuenta/finalizar.compra.html')
    
def historialcompras(request):
    return render(request, 'app/mi-cuenta/historial-compras.html')

def menuingresado(request):
    return render(request, 'app/mi-cuenta/menu-ingresado.html')

def miscompras(request):
    return render(request, 'app/mi-cuenta/mis-compras.html')

def misdirecciones(request):
    return render(request, 'app/mi-cuenta/mis-direcciones.html')

def modificardatos(request):
    return render(request, 'app/mi-cuenta/modificar-datos.html')

def registro(request):
    return render(request, 'app/mi-cuenta/registro.html')


                #TIENDA

def arbustos(request):
    return render(request, 'app/tienda/arbustos.html')

def flores(request):
    return render(request, 'app/tienda/flores.html')

def maceteros(request):
    return render(request, 'app/tienda/maceteros.html')

def tierradehoja(request):
    return render(request, 'app/tienda/tierra-de-hoja.html')
