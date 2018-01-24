import pytest
import _environment

def pytest_addoption(parser):
    parser.addoption("--env", default='uat')

@pytest.fixture
def environment(request):
    env = request.config.getoption('--env')
    environment = _environment.environments[env]
    return environment