from fastapi import FastAPI
import PdfToExcel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/pdf")
async def pdf():
    return await PdfToExcel.pdfToExcel()
