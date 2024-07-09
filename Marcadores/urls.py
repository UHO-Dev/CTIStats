from django.contrib.auth.decorators import login_required
from django.urls import path
from .import views
from .views import login_view
from django.contrib.auth.decorators import login_required
from .views import (
        InvestigadorCreate,
        InvestigadorList, 
        UpdatePerfil, 
        InvestigadorDelete, 
        UpdateInvestigador, 
        InvestigadorDetail, 
        Logout, 
        Estadisticas,  
        DatosUsuarios,
      )
from .views import (PubliSeriadaList,
                    PubliSeriadaCreate,
                    PubliSeriadaList,
                    PubliSeriadaUpdate,
                    PubliSeriadaDelete,
                    PubliUnicaDelete,
                    PubliUnicaUpdate,
                    PubliUnicaCreate,
                    PubliUnicaDetail,
                    PubliSeriadaDetail,
                    EventoList,
                    EventoCreate,
                    EventoDelete,
                    EventoDetail,
                    EventoUpdate,
                    PremioCreate,
                    PremioList,
                    PremioUpdate,
                    PremioDetail,
                    PremioDelete,
                    ProyectoList,
                    ProyectoAprovacion,
                    PubliUnicaList,
                    AprobacionPubliSeriadaUpdate,
                    PubliSeriadaPendientes,
                    AprobacionPubliUnicaUpdate,
                    PubliUnicaPendientes,
                    AprobacionEventoUpdate,
                    EventoPendientes,
                    AprobacionPremioUpdate,
                    PremioPendientes,
                    AprobacionProyectoUpdate,
                    ProyectoPendientes,
                    curriculumDetail
                    )

urlpatterns = [
    
 #Templates basicos
    path('',views.dashboardView,name="dashboard"),
    path('',views.pendientes,name="pendientes"),
    path('login/', login_view, name="login"),
    path('Logout/', login_required(Logout.as_view()), name="Logout"),
    path('about/',views.aboutView,name="About"),

#invetstigador placeholder a corregir
    path('InvestigadorCreate/', InvestigadorCreate, name="InvestigadorCreate"),
    path('InvestigadorList/', InvestigadorList, name='InvestigadorList'),
    path('InvestigadorDetail/<int:pk>/', InvestigadorDetail.as_view(), name='InvestigadorDetail'),
    path('UpdatePerfil/<int:pk>/', UpdatePerfil.as_view(), name='UpdatePerfil'),
    path('UpdateInvestigador/<int:pk>/', UpdateInvestigador.as_view(), name='UpdateInvestigador'),
    path('InvestigadorDelete/<int:pk>/', InvestigadorDelete.as_view(), name='InvestigadorDelete'),
    path('curriculumDetail/<int:id>/', curriculumDetail, name="curriculumDetail"),


# URL Estadisticas
    path('Estadisticas/', login_required(Estadisticas), name="Estadisticas"),
    path('DatosUsuarios/', login_required(DatosUsuarios), name="DatosUsuarios"),
    
  # URLs de Proyectos
    path('ProyectoList/', ProyectoList, name='ProyectoList'),

    path('ProyectoCreate/', views.ProyectoCreate.as_view(), name='ProyectoCreate'),

    path('ProyectoDetail/<int:pk>/', views.ProyectoDetail.as_view(), name='ProyectoDetail'),

    path('ProyectoUpdate/<int:pk>/', views.ProyectoUpdate.as_view(), name='ProyectoUpdate'),

    path('ProyectoDelete/<int:pk>/', views.ProyectoDelete.as_view(), name='ProyectoDelete'),
    
    path('ProyectoAprovacion/<int:pk>/', ProyectoAprovacion.as_view(), name='ProyectoAprovacion'),

  # URLs de Eventos

  path('EventoList/', EventoList, name='EventoList'),
 
  path('EventoCreate/', (EventoCreate.as_view()), name="EventoCreate"),
 
  path('EventoDelete/<int:pk>/', (EventoDelete.as_view()), name="EventoDelete"),
 
  path('EventoDetail/<int:pk>/', (EventoDetail.as_view()), name="EventoDetail"),
 
  path('EventoUpdate/<int:pk>/', (EventoUpdate.as_view()), name="EventoUpdate"),

# PubliSeriada

  path('PubliSeriadaCreate/', PubliSeriadaCreate.as_view(), name='PubliSeriadaCreate'),

  path('PubliSeriadaList/', PubliSeriadaList, name='PubliSeriadaList'),

  path('PubliSeriadaUpdate/<int:pk>/', PubliSeriadaUpdate.as_view(), name='PubliSeriadaUpdate'),

  path('PubliSeriadaDelete/<int:pk>/', PubliSeriadaDelete.as_view(), name='PubliSeriadaDelete'),

  path('PubliSeriadaDetail/<int:pk>/', PubliSeriadaDetail.as_view(), name='PubliSeriadaDetail'),
  
    
# PubliUnica

  path('PubliUnicaList/', PubliUnicaList, name='PubliUnicaList'),
    
  path('PubliUnicaDelete/<int:pk>/', PubliUnicaDelete.as_view(), name='PubliUnicaDelete'),
    
  path('PubliUnicaUpdate/<int:pk>/', PubliUnicaUpdate.as_view(), name='PubliUnicaUpdate'),
  
  path('PubliUnicaCreate/', views.PubliUnicaCreate.as_view(), name='PubliUnicaCreate'),

  path('PubliUnicaDetail/<int:pk>/', PubliUnicaDetail.as_view(), name='PubliUnicaDetail'),
  

  

# Premio

  path('PremioCreate/', PremioCreate.as_view(), name='PremioCreate'),

  path('PremioList/', PremioList, name='PremioList'),

  path('PremioUpdate//<int:pk>/', PremioUpdate.as_view(), name='PremioUpdate'),

  path('PremioDelete/<int:pk>/', PremioDelete.as_view(), name='PremioDelete'),

  path('PremioDetail/<int:pk>/', PremioDetail.as_view(), name='PremioDetail'),



  #aprobacion


  path('AprobacionPubliSeriadaUpdate/<int:pk>/', login_required(AprobacionPubliSeriadaUpdate.as_view()), name="AprobacionPubliSeriadaUpdate"),
  path('PubliSeriadaPendientes/', login_required(PubliSeriadaPendientes), name="PubliSeriadaPendientes"),


  #PubliUnica
  
  path('AprobacionPubliUnicaUpdate/<int:pk>/', login_required(AprobacionPubliUnicaUpdate.as_view()), name="AprobacionPubliUnicaUpdate"),
  path('PubliUnicaPendientes/', login_required(PubliUnicaPendientes), name="PubliUnicaPendientes"),



  
  #eEVENTOS


  path('AprobacionEventoUpdate/<int:pk>/', login_required(AprobacionEventoUpdate.as_view()), name="AprobacionEventoUpdate"),
  path('EventoPendientes/', login_required(EventoPendientes), name="EventoPendientes"),
 

  #PREMIOS
  
  path('AprobacionPremioUpdate/<int:pk>/', login_required(AprobacionPremioUpdate.as_view()), name="AprobacionPremioUpdate"),
  path('PremioPendientes/', login_required(PremioPendientes), name="PremioPendientes"),
 
 #PROYECTOSS
  
  path('AprobacionProyectoUpdate/<int:pk>/', login_required(AprobacionProyectoUpdate.as_view()), name="AprobacionProyectoUpdate"),
  path('ProyectoPendientes/', login_required(ProyectoPendientes), name="ProyectoPendientes"),

]

