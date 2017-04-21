from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from rate.models import Student


def needs_login(request):
    return request.path not in [reverse('login')]


def has_frankiz_rights(request):
    return 'ratemyclass' in request.session['attributes']['brMemberOf']


class LoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if needs_login(request):
            if not request.user.is_authenticated():
                return redirect(reverse('login'))
            attributes = request.session['attributes']
            try:
                student = Student.objects.get(user=request.user)
            except Student.DoesNotExist:
                # For the first connection, we create a student
                student = Student.objects.create(
                    user=request.user,
                    first_name=attributes['first_name'],
                    last_name=attributes['last_name'],
                    name=attributes['name'],
                    promotion=attributes['promo']
                    )
            if has_frankiz_rights(request):
                # Update rights when necessary
                request.user.is_superuser = True
                # TODO: Give only staff power and change permissions accordingly
                request.user.is_staff = True
                request.user.save()
                print("Saved")
        return self.get_response(request)
