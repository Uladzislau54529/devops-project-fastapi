from main import main

def test_movies():
    client = main.test_client()
    response = client.get("/")
    assert response.status_code == 200