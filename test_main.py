from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)


    
def test_get_items():
    response = client.get("/items/123")
    assert response.status_code == 200
    assert response.json() == {"fetch": "Fetched 1 of 123"}

    response_with_count = client.get("/items/123?count=5")
    assert response_with_count.status_code == 200
    assert response_with_count.json() == {"fetch": "Fetched 5 of 123"}