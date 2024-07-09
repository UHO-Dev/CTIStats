from django.shortcuts import redirect

def admin_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "administrador":
            return redirect('dashboard')
        return function(request, *args, **kwargs)
    
    return wrap

def vice_decano_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "vicedecano":
            return redirect('dashboard')
        return function(request, *args, **kwargs)
    
    return wrap

def vice_rector_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "vicerrector":
            return redirect('dashboard')
        return function(request, *args, **kwargs)
    
    return wrap

