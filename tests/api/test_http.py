import pytest
import requests


# Test request and printing response
@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

# Make assertion of specified response elements
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server']  == 'GitHub.com'

# Check status code
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    
    assert r.status_code == 404