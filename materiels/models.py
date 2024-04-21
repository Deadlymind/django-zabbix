from django.db import models
import random

class Materiel(models.Model):
    CONDITION_CHOICES = [
        ('broken', 'Broken'),
        ('diagnostic', 'Diagnostic'),
        ('good_condition', 'Good Condition'),
    ]

    @staticmethod
    def generate_reference():
        # Generate a random number with 4 digits and return it as a string
        return f'{random.randint(0, 9999):04d}'

    References = models.CharField(max_length=4, unique=True)
    type_d_ordinateur = models.CharField(max_length=100, choices=CONDITION_CHOICES, default='good_condition')
    Modele = models.CharField(max_length=50)
    Processeur = models.CharField(max_length=50)
    Mémoire_RAM = models.CharField(max_length=100, default='8GB')
    Taille_du_Disque_Dur = models.CharField(max_length=100, default='500GB')
    Adresse_IP = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.References:
            self.References = self.generate_reference()
        super(Materiel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.Modele} {self.Processeur}'
