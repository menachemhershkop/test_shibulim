import codecs

from solider.create_solider import create_solider
from solider.order_solider import order_by_far
from solider.solider import Solider

from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
import uvicorn

app=FastAPI()

@app.get("/")
def main_page():
    return {"massage":"welcome to base Shibulim room meaning "}
@app.post("/assignWithCsv")
async def assign_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    solider_list=create_solider(list(csvReader))
    solider_order=order_by_far(solider_list)
    return solider_order

