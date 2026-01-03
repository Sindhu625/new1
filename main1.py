from fastapi import FastAPI

app=FastAPI()

@app.get("/details")
def read_root():
    return {"message:Today is 31st December"}