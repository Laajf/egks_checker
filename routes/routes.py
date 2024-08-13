from fastapi import FastAPI, BackgroundTasks
#import uvicorn
#from egks_cheker.api.service.service import get_data
from api.service.service import get_data
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любого домена. Укажите конкретные домены, если необходимо.
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
async def home():
    BASE_DIR = Path(__file__).resolve().parent
    HTML_FILE_PATH = BASE_DIR / "return_file" / "egks.html"

    if not HTML_FILE_PATH.exists():
        return {"error": "File not found"}

    return FileResponse(HTML_FILE_PATH, media_type='text/html')

@app.get("/get_data_card/{number}")
def get_data_card(number: str,):
    text = get_data.get_money_data(number)
    return {"message": text}


@app.put("/post_update_bd")
def update_bd():
    pass

@app.post("/new_user")
def create_new_user():
    pass
