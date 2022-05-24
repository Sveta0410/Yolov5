import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse('index.html')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
