from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app=FastAPI()

contacts = [
    {
        'id': 1,
        'name': 'Sai',
        'phone': '9913908752'
    },
    {
        'id': 2,
        'name': 'Sri',
        'phone': '7013908752'
    }
]

@app.post('/add/contact')
async def add_contact(request:Request):
    data = await request.json() #{'id':3, 'name'='somu'}
    contacts.append(data)
    return contacts

@app.get('/contacts')
def get_all_contacts():
    return contacts

@app.put('/contacts')
async def update_contacts(request: Request):
    data = await request.json()
    for c in contacts:
        if c['id'] == data['id']:
            c.update(data)
            return contacts
        return "No such contacts"

@app.delete('/contacts/{contacts_id}')
def delete_contacts(contacts_id):
    for c in contacts:
        if c['id'] == int(contacts_id):
            contacts.remove(c)
            return contacts
    return "No such contacts"