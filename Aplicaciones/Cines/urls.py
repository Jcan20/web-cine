#Urls especificadas de la aplicacion 
from django.urls import path
from . import views
urlpatterns=[

    path('', views.inicio, name='inicio'),
    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<int:id>/', views.editarGenero, name='editarGenero'),  # Corregir URL para aceptar el id
    path('procesoActualizarGenero/<int:id>/', views.procesoActualizarGenero, name='procesoActualizarGenero'),  # Corregir URL para aceptar el id
    path('eliminarGenero/<int:id>/', views.eliminarGenero, name='eliminarGenero'),  # Corregir URL para aceptar el id

    path('listadoPaises/', views.listadoPaises, name='listadoPaises'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<int:id>/', views.editarPais, name='editarPais'),
    path('procesoActualizarPais/<int:id>/', views.procesoActualizarPais, name='procesoActualizarPais'),
    path('eliminarPais/<int:id>/', views.eliminarPais, name='eliminarPais'),

    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/', views.nuevoDirector, name='guardarDirector'),  # Esta URL va a la vista para crear un nuevo director
    path('editarDirector/<int:id>/', views.editarDirector, name='editarDirector'),
    path('procesoActualizarDirector/<int:id>/', views.editarDirector, name='procesoActualizarDirector'),
    path('eliminarDirector/<int:id>/', views.eliminarDirector, name='eliminarDirector'),

    path('listadoProtagonistas/', views.listadoProtagonistas, name='listadoProtagonistas'),
    path('nuevoProtagonista/', views.nuevoProtagonista, name='nuevoProtagonista'),
    path('guardarProtagonista/', views.guardarProtagonista, name='guardarProtagonista'),  # Corregido
    path('editarProtagonista/<int:id>/', views.editarProtagonista, name='editarProtagonista'),
    path('procesoActualizarProtagonista/<int:id>/', views.procesoActualizarProtagonista, name='procesoActualizarProtagonista'),  # Corregido
    path('eliminarProtagonista/<int:id>/', views.eliminarProtagonista, name='eliminarProtagonista'),


    path('listadoPeliculas/', views.listadoPeliculas, name='listadoPeliculas'),
    path('nuevoPelicula/', views.nuevoPelicula, name='nuevoPelicula'),
    path('guardarPelicula/', views.guardarPelicula, name='guardarPelicula'),  # Corregido
path('editarPelicula/<int:id>/', views.editarPelicula, name='editarPelicula'),
    path('procesoActualizarPelicula/<int:id>/', views.procesoActualizarPelicula, name='procesoActualizarPelicula'),
    path('eliminarPelicula/<int:id>/', views.eliminarPelicula, name='eliminarPelicula'),

        path('enviar-correo-director/<int:id>/', views.enviar_correo_director, name='enviarCorreoDirector'),

    path('exportar_csv/', views.exportar_csv, name='exportar_csv'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
]


