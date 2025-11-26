import codecs
from solider.solider import Solider

from fastapi import FastAPI, HTTPException, UploadFile, File
import csv
import uvicorn

app=FastAPI()
def create_solider(soliderCsv):
    soliders=[]
    for i in list(soliderCsv):
        soilder=Solider(i['מספר אישי'], i['שם פרטי'], i['שם משפחה'], i['מין'], i['עיר מגורים'], i['מרחק מהבסיס'])
        soliders.append(soilder)
    return soliders
def order_by_far(solider_list):
    solider=create_solider(solider_list)
    solider.sorted(solider[far_from_base])
    return solider
@app.get("/")
def main_page():
    return {"massage":"welcome to base Shibulim room meaning "}
@app.post("/assignWithCsv")
async def assign_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    return order_by_far(list(csvReader))

