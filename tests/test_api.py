from playwright.sync_api import expect


def test_postcode_lookup_api(page):
    response = page.request.get(
        "https://api.practicesoftwaretesting.com/postcode-lookup",
        params={
            "country": "DE",
            "postcode": "67560",
            "house_number": "1"
        }
    )

    print("Status Code:", response.status)
    print("Response Body:", response.text())

    assert response.status == 200
    data = response.json()

    assert data is not None
    assert isinstance(data, dict)

def test_postcode_lookup_missing_postcode(page):
    response = page.request.get(
        "https://api.practicesoftwaretesting.com/postcode-lookup",
        params={
            "country": "DE",
            "house_number": "1"
        }
    )

    assert response.status == 404