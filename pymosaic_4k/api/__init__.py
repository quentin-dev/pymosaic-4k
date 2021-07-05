import os
from io import BytesIO
from tempfile import NamedTemporaryFile, gettempdir
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse, HTMLResponse, Response
from PIL.Image import Image as ImageType
from starlette.responses import StreamingResponse

from pymosaic_4k.logic import mosaic as mosaic_logic

app = FastAPI()


def _remove_tmp_file(path: str) -> None:
    os.remove(path)


@app.post("/mosaic/create")
async def create_mosaic(
    background_tasks: BackgroundTasks, files: List[UploadFile] = File(...)
):
    image = mosaic_logic.create_mosaic_from_files([file.file for file in files])

    with NamedTemporaryFile(suffix=".png", delete=False) as response_file:
        image.save(response_file, format="png")
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
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
