import requests

def spotify_authorisation(client_id, response_type, redirect_uri, state, scope, show_dialog)
    print(client_id)


if __name__ == "__main__":
    response = requests.get("https://accounts.spotify.com/authorize")
    print(response.status_code)
