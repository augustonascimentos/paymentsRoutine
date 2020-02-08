import pytest
from app.web import create_app
from dotenv import load_dotenv

load_dotenv(verbose=True)


@pytest.fixture
def client():
    app = create_app({
        'TESTING': True
    })

    client = app.test_client()

    yield client
