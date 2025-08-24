from fastapi import FastAPI
from ch02.orders.api import api

app = FastAPI(debug=True)


