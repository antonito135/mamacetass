from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),

    path('index.html', index, name="index"),

    path('contacto.html',contacto, name="contacto"),

    path('iniciar-sesion.html',iniciarsesion, name="iniciarsesion"),

    path('quienes-somos.html',quienessomos, name="quienessomos"),

    path('registrarse.html',registrarse, name="registrarse"),

    path('suscripcion.html',suscripcion, name="suscripcion"),

                    #MI-CUENTA
    path('mi-cuenta/carrito-compras.html',carritocompras, name="carritocompras"),

    path('mi-cuenta/finalizar.compra.html',finalizarcompra, name="finalizarcompra"),

    path('mi-cuenta/historial-compras.html',historialcompras, name="historialcompras"),

    path('mi-cuenta/menu-ingresado.html',menuingresado, name="menuingresado"),

    path('mi-cuenta/mis-compras.html',miscompras, name="miscompras"),

    path('mi-cuenta/mis-direcciones.html',misdirecciones, name="miscompras"),

    path('mi-cuenta/modificar-datos.html',modificardatos, name="modificardatos"),

    path('mi-cuenta/registro.html',registro, name="registro"),

                #TIENDA
    path('tienda/arbustos.html',arbustos, name="arbustos"),

    path('tienda/flores.html',flores, name="flores"),

    path('tienda/maceteros.html',maceteros, name="maceteros"),

    path('tienda/tierra-de-hoja.html',tierradehoja, name="tierradehoja"),
]

