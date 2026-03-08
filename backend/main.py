from fastapi import FastAPI, UploadFile, File
import shutil
from backend.recommender import recommend
from backend.product_api import search_products

app = FastAPI()

UPLOAD_PATH = "query.jpg"

@app.get("/")
def home():
    return {"message":"FitCast API Running"}

@app.post("/recommend")

async def recommend_fashion(file: UploadFile = File(...)):

    with open(UPLOAD_PATH,"wb") as buffer:

        shutil.copyfileobj(file.file,buffer)

    recommendations = recommend(UPLOAD_PATH)

    products = search_products("fashion")

    return {

        "recommendations":recommendations,

        "products":products

    }