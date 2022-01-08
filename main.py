from fastapi import FastAPI, File, UploadFile, Response, status
import pandas as pd
from io import StringIO

app = FastAPI()


@app.post("/file_upload/")
async def get_max_rating_from_csv(
    response: Response = 200, file: UploadFile = File(...)
):
    """Reads csv file containing products' ratings uploaded from the client and return the highest product's rating
    Args:
        file (File): the file containing product' ratings
        response: (Response, optional)
    Returns:
        if the file is valid, the highest product's rating will be return in a JSON format
        if the file is invalid, an
    """
    # check that the file uploaded must be CSV
    if file.content_type != "text/csv":
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": "File must be CSV!"}
    uploaded_csv = pd.read_csv(StringIO(str(file.file.read(), "utf-8")))
    highest_rating = uploaded_csv.loc[uploaded_csv["customer_avrage_rating"].idxmax()]
    highest_rating_json = highest_rating.to_json()
    response.status_code = status.HTTP_200_OK
    return highest_rating_json
