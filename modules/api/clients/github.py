import requests


class GitHub:
   # Finding user by name
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        
        return body
        
    
    # Searching repo by name
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    

    # Account authorization to change user emails
    def auth_validation(self, payload):
        r = requests.post("https://api.github.com/user/emails", data=payload, headers={'Accept': 'application/vnd.github+json', 
        'Authorization': 'Bearer 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'})
         
        return r.json()
