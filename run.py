# coding=utf-8
import uvicorn
from fastapi import FastAPI

from main import application

app = FastAPI(
    title='BACK API Docs',
    description='back',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.include_router(application, prefix='/app', tags=['API'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='127.0.0.1', port=8001, reload=True, workers=1)
