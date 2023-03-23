# coding=utf-8
import uvicorn
from fastapi import FastAPI

from data.data_api import dataAPI
from lesson.lesson_api import lessonAPI
from message.message_api import messageAPI
from schedule.schedule_api import scheduleAPI
from user.user_api import userAPI

app = FastAPI(
    title='BACK API Docs',
    description='back',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.include_router(userAPI, prefix='/user', tags=['API'])
app.include_router(scheduleAPI, prefix='/schedule', tags=['API'])
app.include_router(lessonAPI, prefix='/lesson', tags=['API'])
app.include_router(dataAPI, prefix='/data', tags=['API'])
app.include_router(messageAPI, prefix='/message', tags=['API'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8888, reload=True, workers=1)
