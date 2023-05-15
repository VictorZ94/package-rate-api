#!/usr/bin/env python3
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router
from fastapi import FastAPI
import uvicorn

app = FastAPI()

origins = ["http://localhost:8000", "http://localhost:5173"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
  uvicorn.run(app="main:app", log_level="info", reload=True)
