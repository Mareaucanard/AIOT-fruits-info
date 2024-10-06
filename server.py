from fastapi import FastAPI, HTTPException
from read_data import search, get_units_as_names, get_units_as_floats

app = FastAPI()


@app.get("/")
async def lifeline():
    return "OK"


@app.get("/units")
async def unit_names():
    return get_units_as_names()


@app.get("/units_number")
async def units_numbers():
    return get_units_as_names()


@app.get("/search/{name}")
async def research(name: str):
    result = search(name.lower())
    if result is None:
        return HTTPException(404, detail=f"No such item in database: {name}")
    else:
        return result
