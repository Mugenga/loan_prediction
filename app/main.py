from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import schemas, crud

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main endpoint for loan prediction
@app.post("/model")
def get_loan(features: schemas.Features):
    # Method call upon the prediction model
    loan = crud.get_loan(features)
    return loan


# Main endpoint for loan prediction
@app.get("/")
def get_loan():
    return {"Hello": "Welcome to our API visit .../docs for the documentation"}




