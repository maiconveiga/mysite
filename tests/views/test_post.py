import pytest
from django.urls import reverse

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    # import pdb; pdb.set_trace()

    assert response.content == b'Ola, mundo'