from main import app
from fastapi.testclient import TestClient

# create a client instance, so we can make calls to the server
client = TestClient(app)


def test_upload_csv_main():
    """Test uploading a CSV file for the products reviews and return a JSON response containing the highest rating product
    The function contains both valid and invalid uploads and valid and invalid responses from the server.
    """
    # make a post request and upload the input.csv
    valid_resonse = client.post(
        "/file_upload",
        files={"file": ("filename", open("./input.csv", "rb"), "text/csv")},
    )
    # the request must return OK, and a JSON response that is equal to the following
    assert valid_resonse.status_code == 200
    assert valid_resonse.json() == {
        "id": 132,
        "product_name": "Massoub gift card",
        "customer_avrage_rating": 5.0,
    }

    invalid_response = client.post(
        "/file_upload",
        files={
            "file": ("filename", open("./bad_input.json", "rb"), "application/json")
        },
    )
    assert invalid_response.status_code == 406
    assert invalid_response.json() == {"message": "File must be CSV!"}
