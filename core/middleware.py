from .models import customer

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("middle ware called")
        if request.user.is_authenticated  and not hasattr(request.user,'customer'):
            customer.objects.create(user=request.user)
            print("user authenticated")
        else:
            print("customer exists")    
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response