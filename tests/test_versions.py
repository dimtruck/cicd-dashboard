from falcon import testing
import pytest
from app import app


@pytest.fixture()
def client():
    return testing.TestClient(app)


def test_get_root(client):
    resources = [u'/', u'/applications']

    result = client.simulate_get('/')
    assert result.json == resources
