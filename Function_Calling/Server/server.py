# # uvicorn server:app --reload --port 8077 --host 0.0.0.0

from fastapi import FastAPI, Query, Header, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

api_key = "932333107-de01c6b3-16c5-4155-8448"

users_db = {
    "100" : 23000,
    "101" : 25000,
    "102" : 50000
}

users_address = {
    "100" : "Vizag",
    "101" : "Vijayawada",
    "102" : "Tamil Nadu"
}

users_name = {
    "100" : "Sharma",
    "101" : "John",
    "102" : "Rahul"
}

user_transaction_status = {
    "100" : {
        "transactions" : {
            "50" : "Success",
            "51" : "Pending",
            "52" : "Failed",
            "53" : "In Progress"
        }
    },
    "101" :{
        "transactions" : {
            "60" : "Success",
            "61" : "Pending",
            "62" : "Failed",
            "63" : "In Progress"
        }
    },
    "102" : {
        "transactions" : {
            "70" : "Success",
            "71" : "Pending",
            "72" : "Failed",
            "73" : "In Progress"
        }
    }
}

payment_status = {
    "100" : "5,000",
    "101" : "0",
    "102" : "10,000"
}

class details(BaseModel):
    userID: str

class transaction(BaseModel):
    userID : str
    transactionID : str

# @app.get("/balance")
# def give_details(request: details):

#     user_id = request.userID
#     if user_id not in users_db:
#         return {"balance": None}
#     else:
#         return {"balance": users_db[user_id]}

Key = "932333107-de01c6b3-16c5-4155-8448"

@app.get("/balance")
def give_details(userID: str = Query("userID"), api_key: str = Header(None)):

    print("This is the header api key",api_key)
    if(api_key != Key):
        raise HTTPException(status_code=403, detail="Forbidden: You don't have permission to access this resource")

    print("This is the request: ",userID)

    if userID not in users_db:
        return {"User id not found": None}
    else:
        return {"balance": users_db[userID]}


    
@app.get("/address")
def give_address(userID: str = Query("userID"), api_key: str = Header(None)):

    if(api_key != Key):
        raise HTTPException(status_code=403, detail="Forbidden: You don't have permission to access this resource")

    if userID not in users_address:
        return {"address": None}
    else:
        return {"address":users_address[userID]}
    
@app.get("/name")
def give_name(userID: str = Query("userID"), api_key: str = Header(None)):

    if(api_key != Key):
        raise HTTPException(status_code=403, detail="Forbidden: You don't have permission to access this resource")
    
    if userID not in users_name:
        return {"Name": None}
    else:
        return {"Name": users_name[userID]}
    
@app.get("/transactionStatus")
def get_status(userID: str = Query("userID"), transactionID: str = Query("transactionID"), api_key: str = Header(None)):

    if(api_key != Key):
        raise HTTPException(status_code=403, detail="Forbidden: You don't have permission to access this resource")


    if userID not in user_transaction_status:
        return {"User Id" : None}
    else:
        if transactionID in user_transaction_status[userID]["transactions"]:
            return {"Status" : user_transaction_status[userID]["transactions"][transactionID]}
        else:
            return {"Transaction id" : None}

@app.get("/paymentStatus")
def get_payment(userID: str = Query("userID"), api_key: str = Header(None)):

    if(api_key != Key):
        raise HTTPException(status_code=403, detail="Forbidden: You don't have permission to access this resource")


    if userID not in payment_status:
        return  {"User id" : None}
    else:
        return {"Payment Status" : payment_status[userID]}           


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8077, log_level="info")