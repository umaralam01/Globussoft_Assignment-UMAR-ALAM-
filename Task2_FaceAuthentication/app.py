import uvicorn
from fastapi import FastAPI, UploadFile, File
import shutil
import os
from predict import verify_faces
import webbrowser

app = FastAPI(
    title="Face Authentication API",
    description="Verify whether two face images belong to the same person",
    version="1.0"
)



    
    
@app.post("/verify")

async def verify(
    image1: UploadFile = File(...),
    image2: UploadFile = File(...)
):

    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    path1 = os.path.join(temp_dir, image1.filename)
    path2 = os.path.join(temp_dir, image2.filename)

    with open(path1, "wb") as buffer:
        shutil.copyfileobj(image1.file, buffer)

    with open(path2, "wb") as buffer:
        shutil.copyfileobj(image2.file, buffer)

    result = verify_faces(path1, path2)

    return result



if __name__ == "__main__":
    print("Server starting...")
    webbrowser.open("http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)