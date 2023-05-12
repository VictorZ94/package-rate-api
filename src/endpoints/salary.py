from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query
from typing import Optional
import datetime
import json

router = APIRouter(tags=["Salaries"])

with open('fake_data/salario.json') as salary_file:
  data_smmlv = json.load(salary_file)

@router.get('/salary-per-year')
def salary_per_year(year: Optional[int] = Query(default=datetime.date.today().year, ge=1990, le=datetime.date.today().year)):
  """ Method to fetch smmlv per year in Colombian.
  """
  smmlv_value = data_smmlv.copy()
  value = list(filter(lambda salary: salary["year"] == year, smmlv_value["smmlv"]))
  if (len(value) == 0):
    smmlv_value["smmlv"] = [{"error": "year not found."}]
    return JSONResponse(status_code=404, content=smmlv_value)

  smmlv_value["smmlv"] = value
  return JSONResponse(status_code=200, content=smmlv_value)

@router.get('/salaries')
def salaries():
  """ Method to fetch all smmlv in Colombian.
  """
  # Devolver los valores obtenidos
  return JSONResponse(status_code=200, content=data_smmlv)