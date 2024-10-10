from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import License, LicenseRevocation
from django.contrib.auth import login
from .forms import RegisterForm
from django.core.exceptions import PermissionDenied

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('create_license')  # Redirect to the license view after successful registration
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_license(request):
    if request.method == "POST":
        license_key = request.POST.get('license_key')
        license = License.objects.create(license_key=license_key, owner=request.user)
        return redirect('view_licenses')
    return render(request, 'registration/create_license.html')

@login_required
def view_licenses(request):
    licenses = License.objects.filter(owner=request.user)
    return render(request, 'registration/view_licenses.html', {'licenses': licenses})

@login_required
def revoke_license(request, license_id):
   if request.user.is_superuser: 
    license = License.objects.get(id=license_id)
    LicenseRevocation.objects.create(license=license)
    license.is_active = False
    license.save()
    return redirect('view_licenses')
   else:
      raise PermissionDenied
