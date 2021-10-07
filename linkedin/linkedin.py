import sys
import os.path
import json
import requests

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))


class LinkedIn():

    def __init__(self) -> None:
        pass

    def get_token_from_file(self, file_name: str):
        with open(os.path.abspath(os.path.join(
                os.path.dirname(__file__), os.path.pardir)) + file_name) as file:
            linkedin_auth = json.load(file)
            self.access_token = linkedin_auth['access_token']
        print(linkedin_auth)

    def get_my_informtion(self) -> dict:
        response = requests.get('https://api.linkedin.com/v2/me',
                                params={'projection': '(id,firstName,lastName)', },
                                headers={'Authorization': 'Bearer ' +
                                         self.access_token, }
                                ).json()
        print(response)


if __name__ == '__main__':
    link = LinkedIn()
    link.get_token_from_file('\\do_not_publish\\linkedin_auth.json')
    link.get_my_informtion()
