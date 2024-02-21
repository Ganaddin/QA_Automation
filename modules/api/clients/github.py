import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        
        return body
        
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    # add http methods (post, put, get, delete) 4 methods - 1 test

    # def add_email(self):
    #     r = requests.post('https://api.github.com/user/emails', 
    #         params={"emails":"octocat@github.com"}
    #     )
    #     body = r.json()

    #     return body
        