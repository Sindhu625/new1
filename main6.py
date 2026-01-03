from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()

persons = [
    {
        'account_id': 1,
        'Name': 'Cutie',
        'balance': 400,
    },
    {
        'account_id': 2,
        'Name': 'Littu',
        'balance': 400,
    }
]

@app.get('/persons')
def get_all_persons():
    return persons

@app.get('/person/{account_id}')
def get_person(account_id):
    for p in persons:
        if p['account_id'] ==int(account_id):
            return p
    return "No such person"

@app.get('/person/name/{Name}')
def get_person_by_Name(Name):
    result = []
    for p in persons:
        if Name.lower() in p["Name"].lower():
            result.append(p)
    return result

@app.post('/credit')
async def credit_amount(request:Request):
    data = await request.json() 
    for p in persons:
        if p['account_id']== data['account_id']:
            p['balance']+= data['amount']
            return p
    return "no such account"

@app.post('/withdraw')
async def withdraw_amount(request:Request):
    data = await request.json()
    for p in persons:
        if p['account_id'] == data['account_id']:
            p['balance']-=data['amount']
            return p
    return "no such account"

@app.post('/transfer')
async def transfer_amount(request:Request):
    data = await request.json()
    for p in persons:
        if p['account_id'] == data['from_account']:
            p['balance'] -= data['amount']

        if p['account_id'] == data['to_account']:
            p['balance'] += data['amount']
        
    return {"message":"success","persons":persons}