from django.test import TestCase
from courbe_de_charge.models import GeographicLP, ElectricityPrice, UsersLP
from django.core.urlresolvers import reverse


class GeographicLPTest(TestCase) :

    def Shapes(self) :
        """
        Test if GeographicLP has the right shapes.
        """
        l1 = 13
        l2 = 8760
        print('debut_de_test')
        self.assertEqual(l1, GeographicLP.objects.all().count())
        
        for i in range(l1) :
            self.assertEqual(l2, len(GeographicLP.objects.all()[i].data))


class LPFormViewTest(TestCase) :

    def LPConstruction(self) :
        """
        Test if the personal the consumption and the load profile
        is calculated and added to UsersLP model.
        """
        data = {
            'location': 'Ile-de-France',
            'power': 9,
            'bill' : 300,
        }

        reponse = self.client.post(reverse('courbe_de_charge.views.LPFormView'), data)
        self.assertNotEqual(UsersLP.objects.filter(Q(location=region) & Q(power=power) & Q(bill=bill))[0].load_profile, GeographicLP.objects.get(region=location).data)
        self.assertNotEqual(UsersLP.objects.filter(Q(location=region) & Q(power=power) & Q(bill=bill))[0].consumption, 0)
        self.assertEqual(type(UsersLP.objects.filter(Q(location=region) & Q(power=power) & Q(bill=bill))[0].load_profile), type(GeographicLP.objects.get(region=location).data))
        self.assertNotEqual(UsersLP.objects.filter(Q(location=region) & Q(power=power) & Q(bill=bill))[0].load_profile, '')
        self.assertEqual(reponse.status_code, 302)

    def LPModification(self) :
        """
        Test if new data are added to the UsersLP model when the user
        modify his personnal informations and if the ancient ones are suppressed.
        """
        data = {
            'location': 'Ile-de-France',
            'power': 9,
            'bill' : 300,
        }

        userLP = UsersLP(user = 'indianapinsard@yahoo.fr', location='Normandie', power=9, bill='400')
        userLP.save()
        request.user.email = 'indianapinsard@yahoo.fr'
        reponse = self.client.post(reverse('courbe_de_charge.views.LPFormView'), data)
        self.assertEqual(UsersLP.objects.all().count(), 1)
