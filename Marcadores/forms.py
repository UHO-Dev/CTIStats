from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from .models import Proyecto, Evento, Programa, PubliSeriada, PubliUnica, Premio, Investigador



class InvestigadorForm(UserCreationForm):
    
    class Meta:
        model = Investigador
        fields = [
            'username',
            'email',
            'rol',
            'area',
            'password1',
            'password2',
            'ci',
            'orci',
            'categoria_docente',
            'categoria_cientifica',
            'facultad'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Ejemplo: @nombreapellidofecha'}),
            'rol': forms.Select(attrs={'class':'form-control','id':'rol'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'email','type':'email','placeholder':'Ingrese su correo coorporativo'}),
            'area': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su Area'}),
            'ci' :forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese su Carnet de Identidad'}),
            'orci':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese su Orci'}),
            'categoria_cientifica': forms.Select(attrs={'class': 'form-control'}), 
            'categoria_docente': forms.Select(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}), 
        }
        

class PerfilForms(forms.ModelForm):
    class Meta:
        model = Investigador
        fields = ['first_name', 'last_name', 'categoria_cientifica', 'categoria_docente','perfil_google', 'perfil_researchgate', 'orci', 'facultad']

        widgets = { 
            'first_name': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'Ingrese los apellidos del usuario'}),
            'categoria_cientifica': forms.Select(attrs={'class': 'form-control'}), 
            'categoria_docente': forms.Select(attrs={'class': 'form-control'}),
            'perfil_google': forms.URLInput(attrs={'class': 'form-control'}),
            'perfil_researchgate': forms.URLInput(attrs={'class': 'form-control'}),
            'orci': forms.NumberInput(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}), 
            
        }

class CambioForm(PasswordChangeForm):
    
    class Meta:
        model = Investigador
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]
        

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control"
            }
        )
    )





class PremioForm(forms.ModelForm):
    class Meta:
        model = Premio
        fields = ['titulo',
                    'fecha',
                    'facultad',
                    'autores',
                    'url',
                    'tipo',
                    'caracter_premio'
                    ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'facultad': forms.Select(attrs={'class': 'form-select'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'caracter_premio': forms.Select(attrs={'class': 'form-select'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),

        }

class ProyectoForm(forms.ModelForm):
    class Meta:

        jefe_proyecto = forms.ModelMultipleChoiceField(
        queryset=Investigador.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'mdb-select'})

        )

        model = Proyecto
        fields = [
            'codigo_proyecto',
            'nombre_proyecto',
            'jefe_proyecto',
            'area_uho',
            'departamento',
            'tipo_proyecto',
            'subtipo_proyecto',
            'entidades_participantes',
            'sector_estrategico',
            'linea_investigacion',
            'fecha_inicio',
            'fecha_cierre',
            'estado_proyecto',
            'cantidad_participantes',
            'cantidad_participantes_uho',
            'cantidad_estudiantes',
            'cantidad_participantes_otras_entidades',
            'cantidad_colaboradores',
            'cantidad_colaboradores_uho',
            'cantidad_estudiantes_gce',
            'cantidad_colaboradores_otras_entidades',
            'cantidad_estudiantes_segundo_ano',
            'cantidad_cuadros_uho',
            'presupuesto_planificado',
        
        ]

        widgets = {
            'codigo_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'jefe_proyecto': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'area_uho': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_proyecto': forms.Select(attrs={'class': 'form-control'}),
            'subtipo_proyecto': forms.Select(attrs={'class': 'form-control'}),
            'entidades_participantes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sector_estrategico': forms.Select(attrs={'class': 'form-control'}),
            'linea_investigacion': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_proyecto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_participantes': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_participantes_uho': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_estudiantes': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_participantes_otras_entidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_colaboradores': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_colaboradores_uho': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_estudiantes_gce': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_colaboradores_otras_entidades': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_estudiantes_segundo_ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_cuadros_uho': forms.NumberInput(attrs={'class': 'form-control'}),
            'presupuesto_planificado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            }
			
#Formulario de Pogramas con Jefe a Partir de los ueuarios

class ProgramaForm(forms.ModelForm):
    class Meta:
        director_programa = forms.ModelMultipleChoiceField(
        queryset=Investigador.objects.all(),
          widget=forms.SelectMultiple(attrs={'class': 'mdb-select'})
        )

        model = Programa
        fields = [
            'codigo_programa',
            'nombre_programa',
            'director_programa',
            'facultad',
            'departamento',
            'tipo_programa',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'estado_programa',
            'presupuesto_asignado',
            'presupuesto_utilizado',
            
        ]
        widgets = {
            'codigo_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'director_programa': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_programa': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_programa': forms.Select(attrs={'class': 'form-control'}),
            'presupuesto_asignado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'presupuesto_utilizado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
 }

#Formulario de Eventos

class EventoForm(forms.ModelForm):

  class Meta:
         autores = forms.ModelMultipleChoiceField(
        queryset=Investigador.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'mdb-select'})
        
         )

         model = Evento
         fields = ['caracter', 'tipo', 'titulo', 'autores', 'isbn', 'publicacion', 'fecha', 'certificado', 'facultad', 'presencialidad']
       
         widgets = {
            'caracter': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Introduzca el caracter del Evento'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Introduzca el tipo de Evento'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca el titulo del Evento'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca ISBN del Evento'}),
            'publicacion': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca la publicaion asociada al Evento'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Introduzca la fecha del Evento'}),
            'certificado': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca el certificado del Evento'}),
            'presencialidad': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Introduzca la presencialidad del Evento'}),
            'facultad': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Introduzca la facultad del Evento'}),
           
            
        }

       
class PubliSeriadaForm(forms.ModelForm):

    autores = forms.ModelMultipleChoiceField(
    queryset=Investigador.objects.all(),
    widget=forms.SelectMultiple(attrs={'class': 'mdb-select'})
    )
    class Meta:
        model = PubliSeriada
        fields = ['titulo',
                'facultad', 
                'departamento', 
                'issn', 
                'fecha_creacion', 
                'autores',
                'categoriaCientifica',
                'doi',
                'pais',
                'editorial']
   

        widgets = {
 
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'issn': forms.TextInput(attrs={'class': 'form-control'}),
            'doi': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoriaCientifica': forms.Select(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class PubliUnicaForm(forms.ModelForm):
    autores = forms.ModelMultipleChoiceField(
        queryset=Investigador.objects.all(),
         widget=forms.SelectMultiple(attrs={'class': 'mdb-select'})
    )
    class Meta:
            model = PubliUnica
            fields = ['titulo', 
                      'facultad', 
                      'departamento', 
                      'isbn', 
                      'fecha_creacion', 
                      'autores',
                      'categoriaCientifica',
                      'capitulo',
                      'volumen',
                      'pais',
                      'editorial']
          
            widgets = {
                        'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
                        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                        'isbn': forms.TextInput(attrs={'class': 'form-control'}),
                        'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                        'categoriaCientifica': forms.Select(attrs={'class': 'form-control'}),
                        'departamento': forms.Select(attrs={'class': 'form-control'}),
                        'facultad': forms.Select(attrs={'class': 'form-control'}),
                        'volumen' : forms.TextInput(attrs={'class': 'form-control'}),
                        'capitulo': forms.TextInput(attrs={'class': 'form-control'}),
                        'pais': forms.Select(attrs={'class': 'form-control'}),
                        'editorial': forms.TextInput(attrs={'class': 'form-control'}),
                    }
        


class AprobacionPremioForm(forms.ModelForm):
    
    class Meta:
        model = Premio
        fields = {
			'aprobacion',
		}
        widgets = {
           'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }
        

class AprobacionPubliUnicaForm(forms.ModelForm):
    
    
    class Meta:
        model = PubliUnica
        fields = {
			'aprobacion',
		}
        widgets = {
            'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }
        

class AprobacionPubliSeriadaForm(forms.ModelForm):
    
    class Meta:
        model = PubliSeriada
        fields = {
			'aprobacion',
		}
        widgets = {
          'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }
        

class AprobacionEventoForm(forms.ModelForm):
    
    class Meta:
        model = Evento
        fields = {
			'aprobacion',
		}
        widgets = {
           'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }



class AprobacionProyectoForm(forms.ModelForm):
    
    class Meta:
        model = Proyecto
        fields = {
			'aprobacion',
		}
        widgets = {
          'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }


        
class AprobacionProgramaForm(forms.ModelForm):
    
    class Meta:
        model = Programa
        fields = {
			'aprobacion',
		}
        widgets = {
           'aprobacion': forms.Select(attrs={'class':'form-control','id':'aprobacion'}),
        }
