from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from base.models import Assignment, Operator
# Create your views here.



def login_view(request):

	if request.method == "POST":
		code = request.POST.get("code")
		username = Operator.objects.filter(code=code)[0].unique_name
		user = authenticate(request, username=username, password=code)
		if user is not None:
			login(request,user)
			assignment_obj = Assignment.objects.filter(operator__unique_name=request.user.username)
			if assignment_obj.exists():
				print("assignment_obj")
				assignment_obj = assignment_obj[0]
				filename = assignment_obj.city.file.name.split('/')[-1]
				response = HttpResponse(assignment_obj.city.file, content_type='text/plain')
				response['Content-Disposition'] = 'attachment; filename=%s' % filename
				return response
			alert = "Login Succesfull"
		else:
		    error = "incorrect user or login code!"

	context = {

	}
	return render(request, 'account/signin.html', context)


def logout_view(request):
    logout(request)

    return redirect('account:login')
