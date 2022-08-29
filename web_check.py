import requests

def get_url_status():
    '''getting the url status'''
    response = requests.get('https://www.google.bg/', verify=False)
    print(response.status_code)
    return response.status_code == 200


def is_google_working():
    '''Checking if the website is working'''
    if get_url_status():
        print('Work')
    else:
        print('not')

is_google_working()
