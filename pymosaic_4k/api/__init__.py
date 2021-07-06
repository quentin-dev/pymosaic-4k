import os
from tempfile import NamedTemporaryFile
from typing import List

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse, HTMLResponse

from pymosaic_4k.logic import mosaic as mosaic_logic

app = FastAPI()


def _remove_tmp_file(path: str) -> None:
    os.remove(path)


@app.post("/mosaic/create")
async def create_mosaic(
    background_tasks: BackgroundTasks,
    files: List[UploadFile] = File(...),
    resize: bool = Form(False),
):
    mosaic = mosaic_logic.create_mosaic_from_files(
        files=[file.file for file in files], resize=resize
    )

    with NamedTemporaryFile(suffix=".png", delete=False) as response_file:
        mosaic.save(response_file, "PNG")
        background_tasks.add_task(_remove_tmp_file, response_file.name)
        return FileResponse(
            response_file.name,
            status_code=200,
            filename=response_file.name,
            media_type="image/png",
        )


@app.get("/")
async def main():
    content = """
<body>
<form action="/mosaic/create" enctype="multipart/form-data" method="post">
    <div>
        <input name="files" type="file" multiple>
        <input name="resize" id="resize" type="checkbox" checked>
        <label for="resize">Resize images</label>
    </div>
    <div>
        <input type="submit">
    </div>
</form>
</body>
    """
    return HTMLResponse(content=content)
