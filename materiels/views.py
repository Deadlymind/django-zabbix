from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Materiel
from .forms import MaterielForm

def index(request):
  return render(request, 'materiels/index.html', {
    'materiels': Materiel.objects.all()
  })


def view_materiel(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = MaterielForm(request.POST)
    if form.is_valid():
      new_References = form.cleaned_data['References']
      new_type_d_ordinateur = form.cleaned_data['type_d_ordinateur']
      new_Modele = form.cleaned_data['Modele']
      new_Processeur = form.cleaned_data['Processeur']
      new_Mémoire_RAM = form.cleaned_data['Mémoire_RAM']
      new_Taille_du_Disque_Dur = form.cleaned_data['Taille_du_Disque_Dur']
      new_Adresse_IP = form.cleaned_data['Adresse_IP']

      new_materiel = Materiel(
        References=new_References,
        type_d_ordinateur=new_type_d_ordinateur,
        Modele=new_Modele,
        Processeur=new_Processeur,
        Mémoire_RAM=new_Mémoire_RAM,
        Taille_du_Disque_Dur=new_Taille_du_Disque_Dur,
        Adresse_IP=new_Adresse_IP
      )
      new_materiel.save()
      return render(request, 'materiels/add.html', {
        'form': MaterielForm(),
        'success': True
      })
  else:
     form = MaterielForm()
  return render(request, 'materiels/add.html', {
    'form': MaterielForm()
  })


def edit(request, id):
  if request.method == 'POST':
    materiel = Materiel.objects.get(pk=id)
    form = MaterielForm(request.POST, instance=materiel)
    if form.is_valid():
      form.save()
      return render(request, 'materiels/edit.html', {
        'form': form,
        'success': True
      })
  else:
    materiel = Materiel.objects.get(pk=id)
    form = MaterielForm(instance=materiel)
  return render(request, 'materiels/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    materiel = Materiel.objects.get(pk=id)
    materiel.delete()
  return HttpResponseRedirect(reverse('index'))
def bon(request):
    bon_materiels = Materiel.objects.filter(type_d_ordinateur='good_condition')
    return render(request, 'bon.html', {'materiels': bon_materiels})
def diagnostique(request):
    diagnostique_materiels = Materiel.objects.filter(type_d_ordinateur='diagnostic')  # replace 'status' with the actual field name
    return render(request, 'diagnostique.html', {'materiels': diagnostique_materiels})

def panne(request):
    panne_materiels = Materiel.objects.filter(type_d_ordinateur='broken')
    return render(request, 'panne.html', {'materiels': panne_materiels})

