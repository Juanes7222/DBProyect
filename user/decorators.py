from django.http import HttpResponseForbidden

def backend_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Agrega aquí tu lógica de autenticación o validación
        if request.user.is_authenticated and request.user.is_backend:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso no permitido")

    return _wrapped_view
