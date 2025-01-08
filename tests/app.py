import requests

BASE_URL = "http://localhost:8000"

def test_get_version():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime():
    test_cases = [
        (2, True), (3, True), (4, False), (5, True), 
        (10, False), (13, True), (17, True), (19, True), 
        (20, False), (15, False)
    ]
    for number, expected in test_cases:
        response = requests.get(f"{BASE_URL}/check_prime/{number}")
        assert response.status_code == 200
        assert response.json() == {"number": number, "is_prime": expected}
