from django.test import TestCase
from django.urls import reverse
from app.dbmodels.models import Player  # Import Django model


class AutocompleteViewTest(TestCase):
    def setUp(self):
        # Ensure there are no prior records interfering
        Player.objects.all().delete()

        # Mock the existing data in the database (which you've shown in the screenshot)
        Player.objects.create(player_id=13, name="Barnyard Dawg")
        Player.objects.create(player_id=12, name="Bill Murray")
        Player.objects.create(player_id=3, name="Bugs Bunny")
        Player.objects.create(player_id=1, name="Michael Jordan")  # Included for completeness

    def test_autocomplete_view(self):
        # Call the autocomplete endpoint with the prefix 'b' for case-insensitive search
        response = self.client.get(reverse('autocomplete', kwargs={'query': 'b'}))
        self.assertEqual(response.status_code, 200)

        # Expecting the top 3 players that match 'B' in the response
        expected_response = [
            {"id": 13, "name": "Barnyard Dawg"},
            {"id": 12, "name": "Bill Murray"},
            {"id": 3, "name": "Bugs Bunny"}
        ]
        self.assertJSONEqual(response.content, expected_response)
