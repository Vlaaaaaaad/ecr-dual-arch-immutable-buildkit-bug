import pytest
from src import create_app

@pytest.fixture
def app():
    return create_app()
