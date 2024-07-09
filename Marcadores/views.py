
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Proyecto, Evento, PubliSeriada, PubliUnica, Premio, Investigador, Programa
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import LoginForm
from django.db.models import Count
from .decorators import vice_rector_required, admin_required, vice_decano_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import ( 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
    )

from .forms import (ProyectoForm,
                    EventoForm, 
                    PubliSeriadaForm, 
                    PubliUnicaForm,
                    PremioForm, 
                    AprobacionEventoForm, 
                    InvestigadorForm,
                    ProgramaForm, 
                    PerfilForms, 
                    CambioForm, 
                    AprobacionPubliSeriadaForm,
                    AprobacionPubliUnicaForm,
                    AprobacionPremioForm,
                    AprobacionProyectoForm,
                    AprobacionProgramaForm
                    )
from django.views.generic import (ListView, 
                                  CreateView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView
                                  )


#Login y logout

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                msg = 'Credenciales Inválidas.'
        else:
            msg = 'Error en la Validación del Formulario.'
    return render(request, "registration/login.html", {
        'form':form,
        'msg':msg,
        }
    )


class Logout(LogoutView):
    template_name = 'registration/Logout.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Logout, self).dispatch(request, *args, **kwargs)
    
#mostar datos de los usuarios
def mostrar_datos_usuarios(request):
    return render(request, 'Estadisticas/DatosUsuarios.html')

#vista principal
@login_required()
def dashboardView(request):
  usuario = request.user
  publi = PubliSeriada.objects.filter(autores = usuario).count()
  revista = PubliSeriada.objects.filter(autores = usuario).count()
  evento = Evento.objects.filter(autores = usuario).count()
  proyecto = Proyecto.objects.filter(jefe_proyecto = usuario).count()
  premio = Premio.objects.filter(autores = usuario).count()
   
    
  context = {
        'section': 'Info',
        'revista': revista,
        'publi': publi,
        'evento': evento,
        'proyecto': proyecto,
        'premio': premio,
         }
 

  return render(request,'dashboard.html', context)

@login_required()
def Listados(request):
    return render(request,'Listas.html')



def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Saving form user data in the model
            username = form.cleaned_data.get('username')
            message_to_show = f'User {username} created sucessfully!'
            messages.success(request, message_to_show.format(username))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form':form })



def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})




def aboutView(request:HttpRequest):
    return render(request,'about.html')


#vista pendientes
@login_required()
def pendientes(request):
    return render(request,'pendientes.html')
# -----------Cambiar Contraseña---------------
class PasswordChange(PasswordChangeView):
    form_class = CambioForm
    template_name = "password/password_change/passwordChange.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PasswordChange, self).dispatch(request, *args, **kwargs)
    
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "password/password_change/passwordChangeDone.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PasswordChangeDone, self).dispatch(request, *args, **kwargs)
  



# -----------Password Reset---------------
class PasswordReset(PasswordResetView):
    email_template_name = "password/password_reset/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset/password_reset_form.html"
    
class PasswordResetDone(PasswordResetDoneView):
    template_name = "password/password_reset/password_reset_done.html"
    
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "password/password_reset/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")
    
class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "password/password_reset/password_reset_complete.html"


#Estadisticas, PLACEHOLDER, MAS A AÑDIR

@login_required
def DatosUsuarios(request):
     
    usuario = request.user
    if usuario.rol == 'vicerrector':
        evento_count = Evento.objects.filter
    elif usuario.rol == 'vicedecano':
        evento_count = Evento.objects.filter(facultad=usuario.facultad,)
    else:
        evento_count = Evento.objects.filter(autores=usuario)    

    usuario = request.user
    if usuario.rol == 'vicerrector':
        premio_count = Premio.objects.filter
    elif usuario.rol == 'vicedecano':
        premio_count = Premio.objects.filter(facultad=usuario.facultad,)
    else:
        premio_count = Premio.objects.filter(autores=usuario)    

    usuario = request.user
    if usuario.rol == 'vicerrector':
        proyecto_count = Proyecto.objects.filter
    elif usuario.rol == 'vicedecano':
        proyecto_count = Proyecto.objects.filter(facultad=usuario.facultad,)
    else:
        proyecto_count = Proyecto.objects.filter(jefe_proyecto=usuario)  

    usuario = request.user
    if usuario.rol == 'vicerrector':
        programa_count = Programa.objects.filter
    elif usuario.rol == 'vicedecano':
        programa_count = Programa.objects.filter(facultad=usuario.facultad,)
    else:
        programa_count = Programa.objects.filter(director_programa=usuario)       

    usuario = request.user
    if usuario.rol == 'vicerrector':
        publi_seriada_count = PubliSeriada.objects.filter
    elif usuario.rol == 'vicedecano':
        publi_seriada_count = PubliSeriada.objects.filter(facultad=usuario.facultad,)
    else:
        publi_seriada_count = PubliSeriada.objects.filter(autores=usuario)    
            
       

    # ARTICULOS PENDIENTES#
    publi_unica_pendiente = PubliUnica.objects.filter(aprobacion= 'Pendiente').count()
    # PUBLICAIONES PENDIENTES#
    publi_seriada_pendiente = PubliSeriada.objects.filter(aprobacion= 'Pendiente').count()
    #EVENTOS PENDIENSTES#
    evento_pendiente = Evento.objects.filter(aprobacion= 'Pendiente').count()
    # PROYECTOS PENDIENTES
    proyecto_pendiente = Evento.objects.filter(aprobacion= 'Pendiente').count()
    # PROGRAMS PENDIENTES
    programa_pendiente = Evento.objects.filter(aprobacion= 'Pendiente').count()
    # CONTAR EVENTOS
    evento_count = Evento.objects.all().count()
    # CONTAR PROYECTOS #
    proyecto_count = Proyecto.objects.all().count()
    # CONTAR PROGRAMS #
    programa_count = Programa.objects.all().count()
    # CONTAR PUBLICAIONES #
    publi_unica_count = PubliUnica.objects.all().count()
    #CONTAR ARTICULOS#
    publi_seriada_count = PubliSeriada.objects.all().count()
     #CONTAR PREMIOS#
    premio_count = Premio.objects.all().count()
    # Proyecto Entidades
    proyecto_entidades_participantes = Proyecto.objects.values('entidades_participantes')
    # Obtener todos los proyectos
    proyectos = Proyecto.objects.all()
    count_premio_caracter_premio = Premio.objects.values('caracter_premio').annotate(total=Count('caracter_premio'))
    count_premio_facultad = Premio.objects.values('facultad').annotate(total=Count('facultad'))
    count_sector_estrategico = Proyecto.objects.values('sector_estrategico').annotate(total=Count('sector_estrategico'))
    count_estado_proyecto = Proyecto.objects.values('estado_proyecto').annotate(total=Count('estado_proyecto'))
    count_area_uho = Proyecto.objects.values('area_uho').annotate(total=Count('area_uho'))
    count_departamento = Proyecto.objects.values('departamento').annotate(total=Count('departamento'))
    count_publi_seriada_facultad = PubliSeriada.objects.values('facultad').annotate(total=Count('facultad'))
    count_publi_seriada_departamento= PubliSeriada.objects.values('departamento').annotate(total=Count('departamento'))
    context = {
        'section': 'Info',
        'evento_count': evento_count,
        'publi_seriada_pendiente': publi_seriada_pendiente,
        'publi_unica_pendiente': publi_unica_pendiente,
        'publi_seriada_count': publi_seriada_count,
        'publi_unica_pendiente': publi_unica_pendiente,
        'publi_unica_count': publi_unica_count,
        'evento_pendiente': evento_pendiente,
        'proyecto_pendiente': proyecto_pendiente,
        'programa_pendiente': programa_pendiente,
        'programa_count': programa_count,
        'proyecto_count': proyecto_count,
        'premio_count': premio_count,
        'count_sector_estrategico': count_sector_estrategico,
        'count_estado_proyecto': count_estado_proyecto,
        'proyecto_entidades_participantes': proyecto_entidades_participantes,
        'count_area_uho': count_area_uho,
        'count_departamento': count_departamento,
        'count_publi_seriada_facultad': count_publi_seriada_facultad,
        'count_publi_seriada_departamento': count_publi_seriada_departamento,
        'count_premio_facultad': count_premio_facultad,
        'count_premio_caracter_premio': count_premio_caracter_premio
       
   }
    
    return render(request,  'Estadisticas/Informacion.html', context)

 




#usuarios



def Estadisticas(request):
    
    usuario = request.user
    if usuario.rol == 'vicerrector':
        investigador_count = Investigador.objects.filter
    elif usuario.rol == 'vicedecano':
        investigador_count = Investigador.objects.filter(facultad=usuario.facultad,)


    # Usuarios del sistema #
    investigador_count = Investigador.objects.all().count()
    # Usuarios del sistema con licenciatura #
    investigador_li = Investigador.objects.filter(categoria_docente='Licenciado').count()
    # Usuarios del sistema con maestria #
    investigador_mas = Investigador.objects.filter(categoria_docente='Maestria').count()
    # Usuarios del sistema con doctorado #
    investigador_doc = Investigador.objects.filter(categoria_docente='Maestria').count()
   
    count_investigador_categoria_docente = Investigador.objects.values('categoria_docente').annotate(total=Count('categoria_docente'))

    count_investigador_categoria_cientifica = Investigador.objects.values('categoria_cientifica').annotate(total=Count('categoria_cientifica'))

    count_investigador_facultad = Investigador.objects.values('facultad').annotate(total=Count('facultad'))
    context = {
        'section': 'Info',
        'investigador_count': investigador_count,
        'investigador_li': investigador_li,
        'investigador_mas': investigador_mas,
        'investigador_doc': investigador_doc,
        'count_investigador_facultad': count_investigador_facultad,
        'count_investigador_categoria_docente': count_investigador_categoria_docente,
        'count_investigador_categoria_cientifica': count_investigador_categoria_cientifica,
           }
    return render(request, 'Estadisticas/DatosUsuarios.html', context)
#Reaultados


def Datos(request):
      
   usuario = request.user
   publi = PubliSeriada.objects.filter(autores = usuario).count()
   
    
   context = {
        'section': 'Info',
        'publi': publi,
         }
   print
   return render(request,'dashboard.html', context)

@login_required
def PubliUnicaList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        publicaciones = PubliUnica.objects.all()
    elif usuario.rol == 'vicedecano':
        publicaciones = PubliUnica.objects.filter(facultad = usuario.facultad)
    else:
        publicaciones = PubliUnica.objects.filter(autores = usuario)
    context = {
        'publicaciones':publicaciones,
    }
    return render(request, 'PubliUnica/PubliUnicaList.html', context)
#usuarios
@login_required
@vice_rector_required
def InvestigadorCreate(request):
    if request.method == "GET":
        form = InvestigadorForm()
        context = {
            'form':form,
            'section':'User',
        }
    else:
        form = InvestigadorForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('InvestigadorList')
        else:
            msg = "El nombre de usuario coincide con uno registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'User',
            }
    return render(request, 'investigador/InvestigadorCreate.html', context)


@login_required
def InvestigadorList(request):
    
    usuario = request.user
    if usuario.rol == 'vicerrector':
        usuarios = Investigador.objects.all()
    elif usuario.rol == 'vicedecano':
        usuarios = Investigador.objects.filter(facultad=usuario.facultad)
    else:
        usuarios = Investigador.objects.all()

        
    context = {
            'usuarios': usuarios,
    }
    return render(request, 'investigador/InvestigadorList.html', context)


class InvestigadorDelete(DeleteView):
    model = Investigador
    template_name = 'investigador/InvestigadorDelete.html'
    success_url = reverse_lazy('InvestigadorList')

class UpdateInvestigador(UpdateView):
    model = Investigador
    form_class = InvestigadorForm
    template_name = 'investigador/UpdateInvestigador.html'
    success_url = reverse_lazy('InvestigadorList')

class InvestigadorDetail(DetailView):
    model = Investigador
    template_name = 'investigador/InvestigadorDetail.html'
    success_url = reverse_lazy('InvestigadorList')
    
#Perfil

class UpdatePerfil(UpdateView):
    model = Investigador
    form_class = PerfilForms
    template_name = 'investigador/UpdatePerfil.html'
    success_url = reverse_lazy('InvestigadorList')


#,,,,,,, Curriculum
def curriculumDetail(request, id):
    user = request.user.id
  
    investigador = Investigador.objects.all()
    evento = Evento.objects.filter(autores=user)
    premio = Premio.objects.filter(autores=user)
    proyectos = Proyecto.objects.filter(jefe_proyecto=user)
    publicaciones = PubliUnica.objects.filter(autores=user)
    revistas = PubliSeriada.objects.filter(autores=user)
    
    user = request.user
    lista = []
    lista = list(lista)

    for i in evento:
        lista.append(i)
    for i in premio:
        lista.append(i)
    for i in proyectos:
        lista.append(i)
    for i in publicaciones:
        lista.append(i)
    for i in revistas:
        lista.append(i)

    # Crear una lista de diccionarios para almacenar las fechas
    fechas = []

    for item in lista:
        fecha_dict = {}
        
        if isinstance(item, Evento):
            fecha_dict['fecha'] = item.fecha
        elif isinstance(item, Premio):
            fecha_dict['fecha'] = item.fecha
        elif isinstance(item, Proyecto):
            fecha_dict['fecha_inicio'] = item.fecha_inicio
        elif isinstance(item, PubliUnica):
            fecha_dict['fecha_creacion'] = item.fecha_creacion
        elif isinstance(item, PubliSeriada):
            fecha_dict['fecha_creacion'] = item.fecha_creacion
        
        fechas.append(fecha_dict)

    context = {
        'lista': lista,
        'fechas': fechas,
    }

    return render(request, 'Investigador/curriculumDetail.html', context)

#Listar proyectos

@login_required
def ProyectoList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        proyectos = Proyecto.objects.all()
    elif usuario.rol == 'vicedecano':
        proyectos = Proyecto.objects.filter(facultad=usuario.facultad)
    else:
        proyectos = Proyecto.objects.filter(jefe_proyecto=usuario)
    context = {
        'proyectos': proyectos,
    }
    return render(request, 'Proyecto/ProyectoList.html', context)


    
#Borrar proyectos

class ProyectoDelete(DeleteView):
    model = Proyecto
    template_name = 'Proyecto/ProyectoDelete.html'
    success_url = reverse_lazy('ProyectoList')
    extra_context = {'section': 'Proyectos'}

#Editar un proyecto desde el usuario

class ProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'Proyecto/ProyectoUpdate.html'
    extra_context = {'section': 'Proyectos'}

    def get_success_url(self):
        return reverse_lazy('ProyectoList')
    
#Crear un proyecto

class ProyectoCreate(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'Proyecto/ProyectoCreate.html'
    extra_context = {'section': 'Proyectos'}
    
    def get_success_url(self):
        return reverse_lazy('ProyectoList')
    
#Aprobar un Proyecto

class ProyectoAprovacion(UpdateView):
    model = Proyecto
    form_class = AprobacionProyectoForm
    template_name = 'Proyecto/ProyectoAprobacion.html'
    extra_context = {'section': 'Proyectos'}

#Detalles/visualizar Proyecto
class ProyectoDetail(DetailView):
    model = Proyecto
    template_name = 'Proyecto/ProyectoDetail.html'
    extra_context = {'section': 'Proyectos'}







#Listar Programa

@login_required
def ProgramaList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        programa = Programa.objects.all()
    elif usuario.rol == 'vicedecano':
        programa = Programa.objects.filter(facultad=usuario.facultad)
    else:
        programa = Programa.objects.filter(jefe_programa=usuario)
    context = {
        'programa': programa,
    }
    return render(request, 'Programa/ProgramaList.html', context)


    
#Borrar Programa

class ProgramaDelete(DeleteView):
    model = Programa
    template_name = 'Programa/ProgramaDelete.html'
    success_url = reverse_lazy('ProgramaList')
    extra_context = {'section': 'Programa'}

#Editar un Programa desde el usuario

class ProgramaUpdate(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'Programa/ProgramaUpdate.html'

    def get_success_url(self):
        return reverse_lazy('ProgramaList')
    
#Crear un Programa

class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'Programa/Programareate.html'
    extra_context = {'section': 'Programa'}
    
    def get_success_url(self):
        return reverse_lazy('ProgramaList')
    
#Aprobar un Programa

class ProyectoAprovacion(UpdateView):
    model = Proyecto
    form_class = AprobacionProgramaForm
    template_name = 'Programa/ProgramaAprobacion.html'
    extra_context = {'section': 'Programa'}

#Detalles/visualizar Proyecto
class ProgramaDetail(DetailView):
    model = Programa
    template_name = 'Programa/ProgramaDetail.html'
    extra_context = {'section': 'Programa'}





# CREATE Evento
class EventoCreate(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Evento/EventoCreate.html'
    success_url = reverse_lazy('EventoList')


# DETAIL Evento
class EventoDetail(DetailView):
    model = Evento
    template_name = 'Evento/EventoDetail.html'
    

# UPDATE Evento
class EventoUpdate(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Evento/EventoUpdate.html'
    success_url = reverse_lazy('EventoList')
    

# DELETE Evento
class EventoDelete(DeleteView):
    model = Evento
    template_name = 'Evento/EventoDelete.html'
    success_url = reverse_lazy('EventoList')

@login_required
def EventoList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        eventos = Evento.objects.all()
    elif usuario.rol == 'vicedecano':
        eventos = Evento.objects.filter(facultad=usuario.facultad)
    else:
        eventos = Evento.objects.filter(autores=usuario)
    context = {
        'evento': eventos,
    }
    return render(request, 'Evento/EventoList.html', context)

#puli seriada


class PubliSeriadaCreate(CreateView):
    model = PubliSeriada
    form_class = PubliSeriadaForm
    template_name = 'PubliSeriada/PubliSeriadaCreate.html'
    success_url = reverse_lazy('PubliSeriadaList')


class PubliSeriadaUpdate(UpdateView):
    model = PubliSeriada
    form_class = PubliSeriadaForm
    template_name = 'PubliSeriada/PubliSeriadaUpdate.html'
    success_url = reverse_lazy('PubliSeriadaList')

class PubliSeriadaDelete(DeleteView):
    model = PubliSeriada
    template_name = 'PubliSeriada/PubliSeriadaDelete.html'
    success_url = reverse_lazy('PubliSeriadaList')


class PubliSeriadaDetail(DetailView):
    model = PubliSeriada
    template_name = 'PubliSeriada/PubliSeriadaDetail.html'

@login_required
def PubliSeriadaList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        articulo = PubliSeriada.objects.all()
    elif usuario.rol == 'vicedecano':
        articulo = PubliSeriada.objects.filter(facultad=usuario.facultad)
    else:
        articulo = PubliSeriada.objects.filter(autores=usuario)
    context = {
        'articulo': articulo,
    }
    return render(request, 'PubliSeriada/PubliSeriadaList.html', context)


   #Vistas de PubliUnica


@login_required
def PubliUnicaList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        publicaciones = PubliUnica.objects.all()
    elif usuario.rol == 'vicedecano':
        publicaciones = PubliUnica.objects.filter(facultad = usuario.facultad)
    else:
        publicaciones = PubliUnica.objects.filter(autores = usuario)
    context = {
        'publicaciones':publicaciones,
    }
    return render(request, 'PubliUnica/PubliUnicaList.html', context)



class PubliUnicaDelete(DeleteView):
    model = PubliUnica
    template_name = 'PubliUnica/PubliUnicaDelete.html'
    success_url = reverse_lazy('PubliUnicaList')
  


class PubliUnicaUpdate(UpdateView):
    model = PubliUnica
    form_class = PubliUnicaForm
    template_name = 'PubliUnica/PubliUnicaUpdate.html'


    def get_success_url(self):
        return reverse_lazy('PubliUnicaList')

class PubliUnicaCreate(CreateView):
    model = PubliUnica
    form_class = PubliUnicaForm
    template_name = 'PubliUnica/PubliUnicaCreate.html'
    success_url = reverse_lazy('PubliUnicaList')


class PubliUnicaDetail(DetailView):
    model = PubliUnica
    template_name = 'PubliUnica/PubliUnicaDetail.html'

 #Premio#   
 
class PremioCreate(CreateView):
    model = Premio
    form_class = PremioForm
    template_name = 'Premio/PremioCreate.html'
    success_url = reverse_lazy('PremioList')

@login_required
def PremioList(request):
    usuario = request.user
    if usuario.rol == 'vicerrector':
        premio = Premio.objects.all()
    elif usuario.rol == 'vicedecano':
        premio = Premio.objects.filter(facultad = usuario.facultad)
    else:
        premio = Premio.objects.filter(autores = usuario)
    context = {
        'premio':premio,
    }
    return render(request, 'Premio/PremioList.html', context)

class PremioUpdate(UpdateView):
    model = Premio
    form_class = PremioForm
    template_name = 'Premio/PremioUpdate.html'
    success_url = reverse_lazy('PremioList')

class PremioDelete(DeleteView):
    model = Premio
    template_name = 'Premio/PremioDelete.html'
    success_url = reverse_lazy('PremioList')

class PremioDetail(DetailView):
    model = Premio
    template_name = 'Premio/PremioDetail.html'


    
   #PubliUnica Revisadas

@login_required
def PubliUnicaRevisados(request):
    publiunica_revisados = PubliUnica.objects.exclude(aprobacion= 'Pendiente')
    context = {
        'publiunica_revisados':publiunica_revisados,
        'section':[
            'RevisadosPubliUnica', 
            'APROBACION',
        ]
    }
    return render(request, 'Aprobacion/PubliUnicarRevisadosList.html', context)

   #PubliUnica Pendientes

@login_required
def PubliUnicaPendientes(request):
    publiunica_pendientes = PubliUnica.objects.filter(aprobacion= 'Pendiente')
    context = {
        'publiunica_pendientes':publiunica_pendientes,
        'section':[
            'RevisadosPubliUnica', 
            'aprobacion',
        ]

    }
    return render(request, 'Aprobacion/PubliUnica/PubliUnicaPendientesList.html', context)


   #PubliSeriada Revisadas


@login_required
def PubliSeriadaRevisados(request):
    publiseriada_revisados = PubliSeriada.objects.exclude(aprobacion= 'Pendiente')
    context = {
        'publiseriada_revisados':publiseriada_revisados,
        'section':[
            'RevisadosPubliSeriada', 
            'AprobacionPubliSeriada',
        ]
    }
    return render(request, 'Aprobacion/PubliUnicarRevisadosList.html', context)


   #PubliSeriada Pendientes


@login_required
def PubliSeriadaPendientes(request):
    publiseriada_pendientes = PubliSeriada.objects.filter(aprobacion= 'Pendiente')
    context = {
        'publiseriada_pendientes':publiseriada_pendientes,
        'section':[
            'RevisadosPubliSeriada', 
            'AprobacionPubliSeriada',
        ]
    }
    return render(request, 'Aprobacion/PubliSeriada/PubliSeriadaPendientesList.html', context)

       #EventoRevisados

@login_required
def EventosRevisados(request):
    evento_revisados = Evento.objects.exclude(aprobacion= 'Pendiente')
    context = {
        'evento_revisados':evento_revisados,
        'section':[
            'RevisadosEvento', 
            'AprobacionEvento',
        ]
    }
    return render(request, 'Aprobacion/EventoRevisadosList.html', context)


#EventoPendientes


@login_required
def EventoPendientes(request):
    evento_pendientes = Evento.objects.filter(aprobacion= 'Pendiente')
    evento_pendientes = evento_pendientes.exclude(aprobacion= 'No Valido')
    context = {
        'evento_pendientes':evento_pendientes,
        'section':[
            'RevisadosEvento', 
            'AprobacionEvento',
        ]
    }
    return render(request, 'Aprobacion/Evento/EventoPendientesList.html', context)


    
#ProyectoRevisados

@login_required
def ProyectoRevisados(request):
    proyecto_revisados = Proyecto.objects.exclude(aprobacion= 'Pendiente')
    context = {
        'proyecto_revisados':proyecto_revisados,
        'section':[
            'RevisadosProyecto', 
            'AprobacionProyecto',
        ]
    }
    return render(request, 'Aprobacion/ProyectoRevisadosList.html', context)


#ProyectoPendientes


@login_required
def ProyectoPendientes(request):
    proyecto_pendientes = Proyecto.objects.filter(aprobacion= 'Pendiente')
    proyecto_pendientes = proyecto_pendientes.exclude(aprobacion= 'No Valido')
    context = {
        'proyecto_pendientes':proyecto_pendientes,
        'section':[
            'RevisadosProyecto', 
            'AprobacionProyecto',
        ]
    }
    return render(request, 'Aprobacion/Proyecto/ProyectoPendientesList.html', context)




#PremioPendientes


@login_required
def PremioPendientes(request):
    premio_pendientes = Premio.objects.filter(aprobacion= 'Pendiente')
    premio_pendientes = premio_pendientes.exclude(aprobacion= 'No Valido')
    context = {
        'premio_pendientes':premio_pendientes,
        'section':[
            'RevisadosPremio', 
            'AprobacionPremio',
        ]
    }
    return render(request, 'Aprobacion/Premio/PremioPendientesList.html', context)





#######Aprobacion##########
@login_required
def PubliSeriadaAprobacionList(request):
    articulo = PubliSeriada.objects.all()
    context = {
        'recursos': articulo,
        'section': 'aprobacion',
    }
    return render(request, 'PubliSeriadaAprobacionList', context)
    
class AprobacionPubliSeriadaUpdate(UpdateView):
    model = PubliSeriada
    form_class = AprobacionPubliSeriadaForm
    template_name = 'Aprobacion\\PubliSeriada\\AprobacionPubliSeriadaUpdate.html'
    success_url = reverse_lazy('PubliSeridaPendientes')
    extra_context={'section': 'aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionPubliSeriadaUpdate, self).dispatch(request, *args, **kwargs)
    






#######Aprobacion##########
@login_required
def PubliUnicaAprobacionList(request):
    publicacion = PubliUnica.objects.all()
    context = {
        'recursos': publicacion,
        'section': 'aprobacion',
    }
    return render(request, 'PubliUnicaAprobacionList', context)
    
class AprobacionPubliUnicaUpdate(UpdateView):
    model = PubliUnica
    form_class = AprobacionPubliUnicaForm
    template_name = 'Aprobacion\\PubliUnica\\AprobacionPubliUnicaUpdate.html'
    success_url = reverse_lazy('PubliUnicaPendientes')
    extra_context={'section': 'aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionPubliUnicaUpdate, self).dispatch(request, *args, **kwargs)
    





#######Aprobacion##########
@login_required
def EventoAprobacionList(request):
    evento = Evento.objects.all()
    context = {
        'evento': evento,
        'section': 'aprobacion',
    }
    return render(request, 'EventoAprobacionList', context)
    
class AprobacionEventoUpdate(UpdateView):
    model = Evento
    form_class = AprobacionEventoForm
    template_name = 'Aprobacion\\Evento\\AprobacionEventoUpdate.html'
    success_url = reverse_lazy('EventoPendientes')
    extra_context={'section': 'aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionEventoUpdate, self).dispatch(request, *args, **kwargs)
    

    

#######Aprobacion##########
@login_required
def PremioAprobacionList(request):
    premio = Premio.objects.all()
    context = {
        'premio': premio,
        'section': 'aprobacion',
    }
    return render(request, 'PremioAprobacionList', context)
    
class AprobacionPremioUpdate(UpdateView):
    model = Premio
    form_class = AprobacionPremioForm
    template_name = 'Aprobacion\\Premio\\AprobacionPremioUpdate.html'
    success_url = reverse_lazy('PremioPendientes')
    extra_context={'section': 'aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionPremioUpdate, self).dispatch(request, *args, **kwargs)
    



#######Aprobacion##########
@login_required
def ProyectoAprobacionList(request):
    proyecto = Proyecto.objects.all()
    context = {
        'proyecto': proyecto,
        'section': 'aprobacion',
    }
    return render(request, 'ProyectoAprobacionList', context)
    
class AprobacionProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = AprobacionProyectoForm
    template_name = 'Aprobacion\\Proyecto\\AprobacionProyectoUpdate.html'
    success_url = reverse_lazy('ProyectoPendientes')
    extra_context={'section': 'aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionProyectoUpdate, self).dispatch(request, *args, **kwargs)
    