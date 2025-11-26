import codecs

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
    # data = {}
    # for rows in csvReader:
    #     key = rows['מספר אישי']
    #     data[key] = rows
    #
    # file.file.close()
    for i in
    return list(csvReader)


