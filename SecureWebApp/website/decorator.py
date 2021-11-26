from django.shortcuts import redirect


def seller_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Customer':
            return redirect('rock-home')
        if group == 'Seller':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def customer_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Seller':
            return redirect('rock-home')
        if group == 'Customer':
            return view_func(request, *args, **kwargs)

    return wrapper_function
