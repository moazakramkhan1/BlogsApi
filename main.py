from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get('/{id}')
def helloWorld(id:int,published:Optional[bool]=True):
    if published:
     return f' {id} speaking'
    else:
       return "yaowzaaaa"
