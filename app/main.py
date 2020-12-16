from fastapi import FastAPI

from app import schemas, crud

app = FastAPI(debug=True)


# Main endpoint for loan prediction
@app.post("/model")
def get_loan(features: schemas.Features):
    # Method call upon the prediction model
    loan = crud.get_loan(features)
    return loan




