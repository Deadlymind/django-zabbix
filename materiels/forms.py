from django import forms
from .models import Materiel


class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = '__all__'  # Inclut tous les champs du modèle
        widgets = {
            'type_d_ordinateur': forms.Select(choices=Materiel.CONDITION_CHOICES),
        }
    labels = {
      'References': 'References',
      'type_d_ordinateur': 'Type d`ordinateur',
      'Modele': 'Modele',
      'Processeur': 'Processeur',
      'Mémoire_RAM': 'Mémoire RAM (Go)',
      'Taille_du_Disque_Dur': 'Taille du Disque Dur (GO)',
      'Adresse_IP': 'Adresse IP'
    }
    widgets = {
      'References': forms.TextInput(attrs={'class': 'form-control'}),
      'type_d_ordinateur': forms.TextInput(attrs={'class': 'form-control'}),
      'Modele': forms.TextInput(attrs={'class': 'form-control'}),
      'Processeur': forms.TextInput(attrs={'class': 'form-control'}),
      'Mémoire_RAM': forms.TextInput(attrs={'class': 'form-control'}),
      'Taille_du_Disque_Dur': forms.TextInput(attrs={'class': 'form-control'}),
      'Adresse_IP': forms.TextInput(attrs={'class': 'form-control'}),
    }
def __init__(self, *args, **kwargs):
        super(MaterielForm, self).__init__(*args, **kwargs)
        # Initialiser les choix pour type_d_ordinateur à partir du modèle
        self.fields['type_d_ordinateur'].choices = Materiel.CONDITION_CHOICES