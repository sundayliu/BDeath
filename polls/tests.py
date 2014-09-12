from django.test import TestCase
from django.utils import timezone
import datetime
# Create your tests here.

from polls.models import Poll

class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(),False)
