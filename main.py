from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import os
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename
    with open(os.path.join("uploads", filename), "wb") as f:
        f.write(contents)
    return {"filename": filename}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
