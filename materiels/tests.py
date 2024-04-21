import random
from django.test import TestCase
from .models import Materiel


class MaterielModelUnitTestCase(TestCase):
    def setUp(self):
        self.materiel = Materiel.objects.create(
            References='Ref01',
            type_d_ordinateur='aa',
            Modele='Bob',
            Marque='Smith',
            Mémoire_RAM='bob.smith@test.com',
            Taille_du_Disque_Dur='Computer Science',
            Adresse_IP='127.0.0.1'
        )

    def test_materiel_model(self):
        data = self.materiel
        self.assertIsInstance(data, Materiel)
