
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Genero, Pais, Director, Protagonista, Pelicula

def inicio(request):
    return render(request, 'inicio.html') 

def listadoGeneros(request):
    generos = Genero.objects.all()  
    return render(request, 'genero/listadoGenero.html', {'generos': generos})

def nuevoGenero(request):
    return render(request, 'genero/nuevoGenero.html')

def guardarGenero(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        genero = Genero(
            nombre=nombre,
        )
        genero.save()  
        return redirect('listadoGeneros')

def editarGenero(request, id):
    genero = get_object_or_404(Genero, id=id)

    if request.method == 'POST':
        genero.nombre = request.POST['nombre']
        genero.save()

        messages.success(request, "Género actualizado exitosamente.")
        return redirect('listadoGeneros')

    return render(request, 'genero/editarGenero.html', {'genero': genero})

def procesoActualizarGenero(request, id):
    if request.method == 'POST':
        genero = get_object_or_404(Genero, id=id)
        nombre = request.POST.get('nombre')
        genero.nombre = nombre
        genero.save()

        messages.success(request, "Género actualizado exitosamente.")
        return redirect('listadoGeneros')

def eliminarGenero(request, id):
    genero = get_object_or_404(Genero, id=id)
    genero.delete()
    messages.success(request, "Género eliminado exitosamente.")
    return redirect('listadoGeneros')

def listadoPaises(request):
    paises = Pais.objects.all()
    return render(request, 'pais/listadoPais.html', {'paises': paises})

def nuevoPais(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        bandera = request.FILES.get('bandera')

        if not nombre:
            messages.error(request, "El nombre del país es obligatorio.")
            return render(request, 'pais/nuevoPais.html')

        if bandera and not (bandera.name.endswith('.png') or bandera.name.endswith('.jpg') or bandera.name.endswith('.jpeg')):
            messages.error(request, "La imagen debe ser en formato PNG, JPG o JPEG.")
            return render(request, 'pais/nuevoPais.html')

        pais = Pais(nombre=nombre, bandera=bandera)
        pais.save()
        messages.success(request, "País agregado exitosamente.")
        return redirect('listadoPaises')

    return render(request, 'pais/nuevoPais.html')

def editarPais(request, id):
    pais = get_object_or_404(Pais, id=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        bandera = request.FILES.get('bandera')

        if not nombre:
            messages.error(request, "El nombre del país es obligatorio.")
            return render(request, 'pais/editarPais.html', {'pais': pais})

        if bandera and not (bandera.name.endswith('.png') or bandera.name.endswith('.jpg') or bandera.name.endswith('.jpeg')):
            messages.error(request, "La imagen debe ser en formato PNG, JPG o JPEG.")
            return render(request, 'pais/editarPais.html', {'pais': pais})

        pais.nombre = nombre
        if bandera:
            pais.bandera = bandera
        pais.save()
        messages.success(request, "País actualizado exitosamente.")
        return redirect('listadoPaises')

    return render(request, 'pais/editarPais.html', {'pais': pais})

def eliminarPais(request, id):
    pais = get_object_or_404(Pais, id=id)
    pais.delete()
    messages.success(request, "País eliminado exitosamente.")
    return redirect('listadoPaises')

def procesoActualizarPais(request, id):
    if request.method == 'POST':
        pais = get_object_or_404(Pais, id=id)
        nombre = request.POST.get('nombre')
        bandera = request.FILES.get('bandera')

        if not nombre:
            messages.error(request, "El nombre del país es obligatorio.")
            return redirect('editarPais', id=id)

        if bandera and not (bandera.name.endswith('.png') or bandera.name.endswith('.jpg') or bandera.name.endswith('.jpeg')):
            messages.error(request, "La imagen debe ser en formato PNG, JPG o JPEG.")
            return redirect('editarPais', id=id)

        pais.nombre = nombre
        if bandera:
            pais.bandera = bandera
        pais.save()
        messages.success(request, "País actualizado exitosamente.")
        return redirect('listadoPaises')

    return redirect('listadoPaises')

def guardarPais(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        bandera = request.FILES.get('bandera')

        # Validaciones (si es necesario)
        if not nombre:
            messages.error(request, "El nombre del país es obligatorio.")
            return render(request, 'pais/nuevoPais.html')

        if bandera and not (bandera.name.endswith('.png') or bandera.name.endswith('.jpg') or bandera.name.endswith('.jpeg')):
            messages.error(request, "La imagen debe ser en formato PNG, JPG o JPEG.")
            return render(request, 'pais/nuevoPais.html')

        pais = Pais(nombre=nombre, bandera=bandera)
        pais.save()
        messages.success(request, "País agregado exitosamente.")
        return redirect('listadoPaises')

    return render(request, 'pais/nuevoPais.html')

def listadoDirectores(request):
    directores = Director.objects.all()
    return render(request, 'director/listadoDirector.html', {'directores': directores})

def nuevoDirector(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        foto = request.FILES.get('foto')
        pais_id = request.POST['pais']
        pais = get_object_or_404(Pais, id=pais_id)

        director = Director(
            nombre=nombre,
            email=email,
            foto=foto,
            pais=pais
        )
        director.save()
        messages.success(request, "Director creado exitosamente.")
        return redirect('listadoDirectores')
    
    paises = Pais.objects.all()
    return render(request, 'director/nuevoDirector.html', {'paises': paises})


def guardarDirector(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        pais_id = request.POST.get('pais')
        foto = request.FILES.get('foto')

        if Director.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe un director con ese correo electrónico.')
            return redirect('nuevoDirector')

        try:
            pais = Pais.objects.get(id=pais_id)
        except Pais.DoesNotExist:
            pais = None

        director = Director(nombre=nombre, email=email, pais=pais, foto=foto)
        director.save()

        messages.success(request, 'Director guardado exitosamente.')
        return redirect('listadoDirectores')

    return redirect('nuevoDirector')


def editarDirector(request, id):
    director = get_object_or_404(Director, id=id)
    
    if request.method == 'POST':
        director.nombre = request.POST['nombre']
        director.email = request.POST['email']
        
        # Solo actualiza la foto si se proporciona una nueva
        if 'foto' in request.FILES:
            director.foto = request.FILES['foto']
        
        pais_id = request.POST['pais']
        pais = get_object_or_404(Pais, id=pais_id)
        director.pais = pais
        
        director.save()
        messages.success(request, "Director actualizado exitosamente.")
        return redirect('listadoDirectores')

    paises = Pais.objects.all()
    return render(request, 'director/editarDirector.html', {'director': director, 'paises': paises})

def procesoActualizarDirector(request, id):
    return editarDirector(request, id)  # Redirige a la función editarDirector

def eliminarDirector(request, id):
    director = get_object_or_404(Director, id=id)
    director.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Protagonista, Pais

def listadoProtagonistas(request):
    protagonistas = Protagonista.objects.all()
    return render(request, 'protagonista/listadoProtagonista.html', {'protagonistas': protagonistas})

def nuevoProtagonista(request):
    paises = Pais.objects.all()
    return render(request, 'protagonista/nuevoProtagonista.html', {'paises': paises})

def guardarProtagonista(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre', '').strip()
        pais_id = request.POST.get('pais')
        foto = request.FILES.get('foto')

        if not nombre or not nombre.replace(" ", "").isalnum():
            messages.error(request, "El nombre solo debe contener letras y números.")
            return redirect('nuevoProtagonista')

        if foto and not foto.name.lower().endswith(('png', 'jpg', 'jpeg')):
            messages.error(request, "Formato de imagen no permitido. Use PNG, JPG o JPEG.")
            return redirect('nuevoProtagonista')

        pais = get_object_or_404(Pais, id=pais_id)
        protagonista = Protagonista(nombre=nombre, pais=pais, foto=foto)
        protagonista.save()

        messages.success(request, "Protagonista guardado correctamente.")
        return redirect('listadoProtagonistas')

def editarProtagonista(request, id):
    protagonista = get_object_or_404(Protagonista, id=id)
    paises = Pais.objects.all()
    return render(request, 'protagonista/editarProtagonista.html', {'protagonista': protagonista, 'paises': paises})

def procesoActualizarProtagonista(request, id):
    protagonista = get_object_or_404(Protagonista, id=id)

    if request.method == "POST":
        nombre = request.POST.get('nombre', '').strip()
        pais_id = request.POST.get('pais')
        foto = request.FILES.get('foto')

        if not nombre or not nombre.replace(" ", "").isalnum():
            messages.error(request, "El nombre solo debe contener letras y números.")
            return redirect(reverse('editarProtagonista', args=[id]))

        if foto and not foto.name.lower().endswith(('png', 'jpg', 'jpeg')):
            messages.error(request, "Formato de imagen no permitido. Use PNG, JPG o JPEG.")
            return redirect(reverse('editarProtagonista', args=[id]))

        protagonista.nombre = nombre
        protagonista.pais = get_object_or_404(Pais, id=pais_id)

        if foto:  # Si hay una nueva imagen, se actualiza
            protagonista.foto = foto

        protagonista.save()
        messages.success(request, "Protagonista actualizado correctamente.")
        
        return redirect(reverse('listadoProtagonistas'))


def eliminarProtagonista(request, id):
    protagonista = get_object_or_404(Protagonista, id=id)
    protagonista.delete()
    messages.success(request, "Protagonista eliminado correctamente.")
    return redirect('listadoProtagonistas')




def listadoPeliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'pelicula/listadoPelicula.html', {'peliculas': peliculas})

def nuevoPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    protagonistas = Protagonista.objects.all()  # Obtén los protagonistas

    if request.method == "POST":
        # Obtén los datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        genero_id = request.POST.get('genero')
        director_id = request.POST.get('director')
        pais_origen_id = request.POST.get('pais_origen')

        # Crear la película
        pelicula = Pelicula(
            titulo=titulo,
            descripcion=descripcion,
            genero_id=genero_id,
            director_id=director_id,
            pais_origen_id=pais_origen_id
        )

        # Subir la portada si existe
        if 'portada' in request.FILES:
            pelicula.portada = request.FILES['portada']

        # Subir el trailer si existe
        if 'trailer' in request.FILES:
            pelicula.trailer = request.FILES['trailer']

        # Guardar la película
        pelicula.save()

        # Guardar los protagonistas seleccionados
        protagonistas_ids = request.POST.getlist('protagonistas')
        for protagonista_id in protagonistas_ids:
            protagonista = get_object_or_404(Protagonista, id=protagonista_id)
            pelicula.protagonistas.add(protagonista)

        # Guardar los cambios en la película
        pelicula.save()

        # Mensaje de éxito
        messages.success(request, "Película creada correctamente.")
        return redirect('listadoPeliculas')

    return render(request, 'pelicula/nuevoPelicula.html', {
        'generos': generos,
        'directores': directores,
        'paises': paises,
        'protagonistas': protagonistas  # Asegúrate de pasar los protagonistas al contexto
    })

def guardarPelicula(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo').strip()
        descripcion = request.POST.get('descripcion').strip()
        fecha_estreno = request.POST.get('fecha_estreno')
        genero_id = request.POST.get('genero')
        director_id = request.POST.get('director')
        pais_origen_id = request.POST.get('pais_origen')
        portada = request.FILES.get('portada')
        trailer = request.FILES.get('trailer')

        # Validaciones
        if not titulo or not descripcion:
            messages.error(request, "El título y la descripción son campos obligatorios.")
            return redirect('nuevoPelicula')

        if portada and not portada.name.lower().endswith(('png', 'jpg', 'jpeg')):
            messages.error(request, "El formato de la portada no es válido. Usa PNG, JPG o JPEG.")
            return redirect('nuevoPelicula')

        if trailer and not trailer.name.lower().endswith(('pdf', 'doc', 'docx')):
            messages.error(request, "El formato del trailer no es válido. Usa PDF o DOC/DOCX.")
            return redirect('nuevoPelicula')

        # Obtener las relaciones de claves foráneas
        genero = get_object_or_404(Genero, id=genero_id)
        director = get_object_or_404(Director, id=director_id) if director_id else None
        pais_origen = get_object_or_404(Pais, id=pais_origen_id)

        # Crear la película
        pelicula = Pelicula(
            titulo=titulo,
            descripcion=descripcion,
            fecha_estreno=fecha_estreno,
            genero=genero,
            director=director,
            pais_origen=pais_origen,
            portada=portada,
            trailer=trailer
        )
        pelicula.save()

        # Guardar protagonistas si se seleccionaron
        protagonistas_ids = request.POST.getlist('protagonistas')
        for protagonista_id in protagonistas_ids:
            protagonista = get_object_or_404(Protagonista, id=protagonista_id)
            pelicula.protagonistas.add(protagonista)

        pelicula.save()

        messages.success(request, "Película guardada correctamente.")
        return redirect('listadoPeliculas')
    else:
        return redirect('nuevoPelicula')

def editarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    protagonistas = Protagonista.objects.all()

    if request.method == "POST":
        pelicula.titulo = request.POST.get('titulo')
        pelicula.descripcion = request.POST.get('descripcion')
        pelicula.fecha_estreno = request.POST.get('fecha_estreno')
        pelicula.genero_id = request.POST.get('genero')
        pelicula.director_id = request.POST.get('director')
        pelicula.pais_origen_id = request.POST.get('pais_origen')

        # Asignación de los protagonistas seleccionados
        protagonistas_ids = request.POST.getlist('protagonistas')
        pelicula.protagonistas.set(Protagonista.objects.filter(id__in=protagonistas_ids))

        if 'portada' in request.FILES:
            pelicula.portada = request.FILES['portada']
        
        if 'trailer' in request.FILES:
            pelicula.trailer = request.FILES['trailer']
        
        pelicula.save()
        messages.success(request, "Película actualizada correctamente.")
        return redirect('listadoPeliculas')

    return render(request, 'pelicula/editarPelicula.html', {
        'pelicula': pelicula,
        'generos': generos,
        'directores': directores,
        'paises': paises,
        'protagonistas': protagonistas
    })


def procesoActualizarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)

    if request.method == "POST":
        pelicula.titulo = request.POST.get('titulo')
        pelicula.descripcion = request.POST.get('descripcion')
        pelicula.fecha_estreno = request.POST.get('fecha_estreno')
        pelicula.genero_id = request.POST.get('genero')
        pelicula.director_id = request.POST.get('director')
        pelicula.pais_origen_id = request.POST.get('pais_origen')

        if 'portada' in request.FILES:
            pelicula.portada = request.FILES['portada']
        
        if 'trailer' in request.FILES:
            pelicula.trailer = request.FILES['trailer']
        
        pelicula.save()
        messages.success(request, "Película actualizada correctamente.")
        return redirect('listadoPeliculas')

    return render(request, 'pelicula/editarPelicula.html', {'pelicula': pelicula})



def eliminarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    messages.success(request, "Película eliminada correctamente.")
    return redirect('listadoPeliculas')

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Director

def enviar_correo_director(request, id):
    try:
        director = get_object_or_404(Director, id=id)
        
        if not director.email:
            messages.error(request, 'Este director no tiene un correo electrónico asociado.')
            return redirect('listadoDirectores')
        
        # Preparar el contenido del correo
        context = {
            'director': director,
            'BASE_URL': request.build_absolute_uri('/')[:-1]
        }
        
        # Renderizar el template HTML
        html_message = render_to_string('email_template_director.html', context)
        plain_message = strip_tags(html_message)
        
        # Enviar el correo
        send_mail(
            subject=f"Nuevo Director: {director.nombre}",
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[director.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        messages.success(request, f'Correo enviado exitosamente a {director.email}')
    except Exception as e:
        messages.error(request, f'Error al enviar el correo: {str(e)}')
    
    return redirect('listadoDirectores')

import csv
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Pelicula

def exportar_csv(request):
    peliculas = Pelicula.objects.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="peliculas.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Título', 'Género', 'Director', 'Protagonistas', 'Fecha de Estreno'])
    
    for pelicula in peliculas:
        writer.writerow([pelicula.id, pelicula.titulo, pelicula.genero.nombre,
                         pelicula.director.nombre if pelicula.director else 'No disponible',
                         ', '.join([protagonista.nombre for protagonista in pelicula.protagonistas.all()]),
                         pelicula.fecha_estreno.strftime('%Y-%m-%d')])
    
    return response

def exportar_excel(request):
    peliculas = Pelicula.objects.all()
    
    wb = Workbook()
    ws = wb.active
    ws.title = 'Películas'
    
    ws.append(['ID', 'Título', 'Género', 'Director', 'Protagonistas', 'Fecha de Estreno'])
    
    for pelicula in peliculas:
        ws.append([pelicula.id, pelicula.titulo, pelicula.genero.nombre,
                   pelicula.director.nombre if pelicula.director else 'No disponible',
                   ', '.join([protagonista.nombre for protagonista in pelicula.protagonistas.all()]),
                   pelicula.fecha_estreno.strftime('%Y-%m-%d')])
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="peliculas.xlsx"'
    
    wb.save(response)
    return response
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # Importa correctamente
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from .models import Pelicula

def exportar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="peliculas_listado.pdf"'

    # Usamos SimpleDocTemplate para una mejor estructura de documento
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))

    # Estilos para el documento
    styles = getSampleStyleSheet()  # Asegúrate de que esta función esté importada correctamente
    style_title = ParagraphStyle(
        name='Title',
        fontSize=18,
        alignment=1,  # Centrado
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )
    
    # Crear el título
    title = 'Listado de Películas'

    # Crear la tabla con las cabeceras
    data = [
        ['ID', 'Título', 'Género', 'Director', 'Protagonistas', 'Fecha de Estreno'],
    ]

    peliculas = Pelicula.objects.all()
    for pelicula in peliculas:
        # Extraer los datos de cada película
        protagonistas = ", ".join([protagonista.nombre for protagonista in pelicula.protagonistas.all()])
        data.append([
            pelicula.id,
            pelicula.titulo,
            pelicula.genero.nombre,
            pelicula.director.nombre if pelicula.director else "No disponible",
            protagonistas,
            pelicula.fecha_estreno.strftime("%Y-%m-%d")
        ])

    # Crear la tabla
    table = Table(data)
    
    # Definir estilo de la tabla
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ]))

    # Crear un documento con los elementos
    elements = []

    # Añadir el título
    elements.append(Paragraph(title, style_title))
    
    # Añadir la tabla
    elements.append(table)

    # Construir el documento
    doc.build(elements)

    return response
