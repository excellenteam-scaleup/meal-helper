import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_random_joke():
    response = requests.get(f'{BASE_URL}/random')
    print('Random Joke:', response.text)


def save_new_joke(joke):
    response = requests.post(f'{BASE_URL}/save', data=joke)
    print('Save Response:', response.text)


def get_joke_by_id(joke_id):
    response = requests.get(f'{BASE_URL}/joke/{joke_id}')
    if response.status_code == 200:
        print(f'Joke #{joke_id}:', response.json()['joke'])
    else:
        print(f'Joke #{joke_id} not found.')


def delete_joke_by_id(joke_id):
    response = requests.delete(f'{BASE_URL}/joke/{joke_id}')
    if response.status_code == 200:
        print(f'Deleted Joke #{joke_id}:', response.json()['joke'])
    else:
        print(f'Could not delete joke #{joke_id}.')


if __name__ == '__main__':
    get_random_joke()

    new_joke = "Why don't skeletons fight each other? They don't have the guts."
    save_new_joke(new_joke)

    get_joke_by_id(2)  # assuming this is the new one
    delete_joke_by_id(2)
    get_joke_by_id(2)
