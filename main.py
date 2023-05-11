from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
import datetime
import json

app = FastAPI()

salary_file = open('salario.json')
data_smmlv = json.load(salary_file)

@app.get('/salary-per-year', tags=["Salary per year"],  status_code=200)
def salary_per_year(year: Optional[int] = datetime.date.today().year):
  """ Method to fetch smmlv per year in Colombian.
  """
  smmlv_value = data_smmlv.copy()
  value = list(filter(lambda salary: salary["year"] == year, smmlv_value["smmlv"]))
  if (len(value) == 0):
    smmlv_value["smmlv"] = [{"error": "year not found."}]
    return JSONResponse(status_code=404, content=smmlv_value)

  smmlv_value["smmlv"] = value
  return JSONResponse(status_code=200, content=smmlv_value)

@app.get('/salaries', tags=["historical salary"],  status_code=200)
def salaries():
  """ Method to fetch all smmlv in Colombian.
  """
  # Devolver los valores obtenidos
  return JSONResponse(status_code=200, content=data_smmlv)
