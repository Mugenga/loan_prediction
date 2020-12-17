from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from app import schemas, crud

from starlette.staticfiles import StaticFiles

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates/")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

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

@apiParam {Number} gender Gender for the user 0 for female and 1 for male
@apiParam {Number} age User Age
@apiParam {Number} amount_in_savings How much user has in savings
@apiParam {Number} saving_freq How often does the user save
@apiParam {Number} duration Loan duration
@apiParam {Number} village_id Village in which the user comes from

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
