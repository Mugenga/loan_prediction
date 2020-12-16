from typing import List
from pydantic import BaseModel


# This is for data validation
class Features(BaseModel):
    gender: int
    age: int
    amount_in_savings: int
    saving_freq: int
    duration: int
    village_id: int


value = 100000000000000



