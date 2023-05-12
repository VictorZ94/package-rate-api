from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query
from typing import Optional
import datetime
import json

router = APIRouter(tags=["Transport assistance"])

with open('fake_data/aux_transporte.json') as assistance_file:
  data_assistance = json.load(assistance_file)

@router.get('/transport-assistance-per-year')
def transport_assistance_per_year(
  year: Optional[int] = Query(
    default=datetime.date.today().year,
    ge=1990,
    le=datetime.date.today().year
  )
):
  """ Method to fetch transport assistance per year in Colombian.
  """
  assistance_value = data_assistance.copy()
  value = list(filter(lambda salary: salary["year"] == year, assistance_value["aux_trans"]))
  if (len(value) == 0):
    assistance_value["aux_trans"] = [{"error": "year not found."}]
    return JSONResponse(status_code=404, content=assistance_value)

  assistance_value["aux_trans"] = value
  return JSONResponse(status_code=200, content=assistance_value)

@router.get('/transport-assistance')
def transport_assistance():
  """ Method to fetch all transport assistance in Colombian.
  """
  # Devolver los valores obtenidos
  return JSONResponse(status_code=200, content=data_assistance)