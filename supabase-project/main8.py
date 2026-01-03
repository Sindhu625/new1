from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from supabase import create_client

db_url = "https://ijpwdjzvtfvdewmzsgat.supabase.co"
db_key = "sb_publishable_jL8FSr6z7CLqdnXBerAudQ_W_05v8LH"

db = create_client(db_url, db_key)

app = FastAPI()

@app.post('/add/contact')
async def add_contact(request:Request):
    data = await request.json() #{'id':3, 'name'='Saii', 'phone'='1234567890'}
    result = db.table('contacts').insert(data).execute()
    return "Success"

@app.get('/contacts')
def get_all_contacts():
    result = db.table('contacts').select('*').execute()
    contacts = result.data
    return contacts

@app.get('/contact')
def get_contact(contact_id):
    result = db.table('contacts').select('*').eq('id', contact_id).execute()
    data = result.data
    return data

@app.put('/contact/{contact_id}')
async def update_contact(request: Request, contact_id):
    data = await request.json() #{'name': 'new name', 'phone': '123456789'}
    result = db.table('contacts').update(data).eq('id', contact_id).execute()
    return "Updated successfully"

@app.delete('/contact/{contact_id}')
def delete_contacts(contact_id):
    result = db.table('contacts').delete().eq('id', contact_id).execute()
    return "Deleted successfully"