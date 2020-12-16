import pickle

from . import schemas
import pandas as pd


def get_loan(features: schemas.Features):
    feature = schemas.value
    # Get features and create a dataframe of features
    entry = pd.DataFrame([[features.gender, feature, features.duration, 0, features.saving_freq, features.amount_in_savings,
                           features.village_id, features.age]],
                         columns=['gender', 'request_date', 'duration', 'loan_status', 'no_of_saving_transactions',
                                  'savings_amount', 'village_id', 'age'], dtype=int)

    # Open the model file
    model = open("sql_app/loan_model", 'rb')
    try:
        imported_model = \
            pickle.load(model)
        model = imported_model
    except:
        # If an error occurs while opening the file print an exception an inform the user
        print("An exception occurred")
        return {"code": 101, "message": "An exception occurred"}

    predicted = int(model.predict(entry))

    # Return the prediction as JSON with a success message
    return {"code": 100, "message": "success", "loan": predicted}
