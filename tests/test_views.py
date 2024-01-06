# test_views.py
from django.test import TestCase
from restaurant.models import menu  # korrigierter Import

class MenuViewTest(TestCase):
    def setUp(self):
        # Erstellen Sie einige Testdaten, einschließlich des 'inventory'-Felds
        menu.objects.create(title="Dish1", price=10, inventory=50)
        menu.objects.create(title="Dish2", price=20, inventory=30)

    def test_getall(self):
        # Rufen Sie Ihre View auf (ersetzen Sie '/api/menu/' durch Ihren tatsächlichen Endpunkt)
        response = self.client.get('/restaurant/menu/')

        # Überprüfen Sie den Statuscode
        self.assertEqual(response.status_code, 200)

        # Überprüfen Sie die Anzahl der zurückgegebenen Daten
        data = response.json()
        self.assertEqual(len(data), 2)

        # Überprüfen Sie die Werte der einzelnen Objekte
        self.assertEqual(data[0]['title'], "Dish1")
        self.assertEqual(int(float(data[0]['price'])), 10)
        self.assertEqual(data[0]['inventory'], 50)

        self.assertEqual(data[1]['title'], "Dish2")
        self.assertEqual(int(float(data[1]['price'])), 20)
        self.assertEqual(data[1]['inventory'], 30)
