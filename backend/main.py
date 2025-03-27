from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from documents.upload import upload_file

app = FastAPI()

# Monta la directory frontend come file statici
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    with open("../frontend/index.html") as f:
        return f.read()

@app.post("/upload/")
async def upload_endpoint(file: UploadFile = File(...)):
    return await upload_file(file)