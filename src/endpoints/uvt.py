from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query
from typing import Optional
import datetime
import json

router = APIRouter(tags=["Unidad de Valor Tributario"])

with open('fake_data/uvt.json') as uvt_file:
  data_uvt = json.load(uvt_file)

@router.get('/uvt-per-year')
def uvt_per_year(year: Optional[int] = Query(default=datetime.date.today().year, ge=1990, le=datetime.date.today().year)):
  """ Method to fetch uvt per year in Colombia.
  """
  uvt_value = data_uvt.copy()
  value = list(filter(lambda salary: salary["year"] == year, uvt_value["uvt"]))
  if (len(value) == 0):
    uvt_value["uvt"] = [{"error": "year not found."}]
    return JSONResponse(status_code=404, content=uvt_value)

  uvt_value["uvt"] = value
  return JSONResponse(status_code=200, content=uvt_value)

@router.get('/uvt')
def uvt():
  """ Method to fetch all uvt in Colombian.
  """
  # Devolver los valores obtenidos
  return JSONResponse(status_code=200, content=data_uvt)
