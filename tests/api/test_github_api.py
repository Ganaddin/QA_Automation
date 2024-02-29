import pytest


# Test to check if user exists
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('Ganaddin')
    assert user['login'] == 'Ganaddin'
    

# Test to check if user not exists
@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


# Finding all repoes with specified name
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 55
    assert 'become-qa-auto' in r['items'][0]['name']


# Checking unexistent repo
@pytest.mark.api 
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


# Finding repo with the single character in name
@pytest.mark.api 
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0    


# Authorization validation when posting emails
@pytest.mark.api
def test_auth_validation(github_api):
    r = github_api.email_post('{"emails":["octocat@github.com","mona@github.com","octocat@octocat.org"]}')
    
    assert r['message'] == 'Validation Failed'
    
    
