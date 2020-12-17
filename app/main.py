from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from app import schemas, crud

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
@api {post} /model Loan Prediction Endpoint
@apiName Loan Prediction
@apiGroup Loan

@apiParam {Number} gender 
@apiParam {Number} age 
@apiParam {Number} amount_in_savings 
@apiParam {Number} saving_freq 
@apiParam {Number} duration 
@apiParam {Number} village_id 

@apiSuccess {Number} code success code.
@apiSuccess {String} message API Response Message.
@apiSuccess {Number} loan How muh user is allowed to borrow.
"""


# Main endpoint for loan prediction
@app.post("/model")
def get_loan(features: schemas.Features):
    # Method call upon the prediction model
    loan = crud.get_loan(features)
    return loan


# Main endpoint for loan prediction
@app.get("/")
def get_loan(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})
