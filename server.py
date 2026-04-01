from fastapi import FastAPI
import os

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/balance')
def balance():
    return {'address': os.environ.get('TRON_ADDR', ''), 'token': 'USDT'}