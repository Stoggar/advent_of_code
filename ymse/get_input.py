import requests

class HttpError(Exception):
    pass
    

def get_input(day, year=2021):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    url = 'https://adventofcode.com/2021/day/5'
    r = requests.get(url)
    if not r.status_code == 200:
        raise HttpError(f'request error, status code: {r.status_code}\nrequest url: {url}')
    return r.content


if __name__ == '__main__':
    print(get_input(5))


