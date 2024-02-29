import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Oleg'
        self.second_name = 'Kolesnyk'

    def remove(self):
        self.name = ''
        self.second_name = ''   

# Fixture for api and fixtures tests    
@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


# Fixture for github_api tests
@pytest.fixture
def github_api():
    api = GitHub()
    yield api


# Fixture for database tests
@pytest.fixture
def database():
    db = Database()
    yield db
