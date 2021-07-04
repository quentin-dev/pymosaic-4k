from typing import List

from fastapi import FastAPI, File

app = FastAPI()


@app.post("/mosaic/create")
def create_mosaic(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}
