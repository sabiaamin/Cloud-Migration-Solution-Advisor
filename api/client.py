import httpx


API_URL = "http://127.0.0.1:8000"


def assess_application(data):
    response = httpx.post(
        f"{API_URL}/assessment",
        json=data
    )

    response.raise_for_status()

    return response.json()