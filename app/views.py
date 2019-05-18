from django.shortcuts import render, redirect

# Create your views here.
from app.forms import MascotaForm


def home(request):
    return render(request, 'index.html')


def crear_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
        else:
            form = MascotaForm()
        return render(request, 'app/crear_mascota.html', {'form': form})
