from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app=FastAPI()

contacts = [
    {'id': 1, 'name': 'Ammu', 'phone': '7893565066'}
]

# CREATE
@app.get('/all')
def add_contact(id, name, phone):
    return({'id': 1, 'name': 'Ammu', 'phone': 7893565066})