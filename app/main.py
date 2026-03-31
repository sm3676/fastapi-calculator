from fastapi import FastAPI, HTTPException
import logging
from app import operations

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def home():
    return {"message": "Calculator API running"}

@app.get("/add")
def add(a: float, b: float):
    result = operations.add(a, b)
    logger.info(f"Add {a} + {b} = {result}")
    return {"result": result}

@app.get("/subtract")
def subtract(a: float, b: float):
    result = operations.subtract(a, b)
    return {"result": result}

@app.get("/multiply")
def multiply(a: float, b: float):
    result = operations.multiply(a, b)
    return {"result": result}

@app.get("/divide")
def divide(a: float, b: float):
    try:
        result = operations.divide(a, b)
        return {"result": result}
    except ValueError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))