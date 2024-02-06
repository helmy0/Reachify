from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
     
        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    """
    Decorator that checks if the user has the required roles to access the view (Customers, Products and homes).

    Args:
        allowed_roles (list, optional): List of roles allowed to access the view. Defaults to [].

    Returns:
        function: The decorated view function.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    """
    A (duct tape fix) decorator that allows only admin users to access a view function.
    
    Args:
        view_func (function): The view function to be decorated.
    
    Returns:
        function: The wrapper function that checks the user's group and redirects if not admin.
    """
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user-page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func