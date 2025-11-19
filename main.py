from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ======================================
# MODELO BÁSICO PARA TESTE
# ======================================

@app.get("/")
def root():
    return {"mensagem": "API funcionando!"}


# ======================================
# MODELOS
# ======================================

class News(BaseModel):
    icon: str
    description: str

class User(BaseModel):
    id: int
    name: str
    email: str
    balance: float
    news: List[News] = []


# ======================================
# BANCO DE DADOS  (em memória)
# ======================================

fake_db = {
    1: User(id=1, name="Ana Souza", email="ana@example.com", balance=5000, news=[]),
    2: User(id=2, name="Carlos Lima", email="carlos@example.com", balance=12000, news=[]),
    3: User(id=3, name="Marina Alves", email="marina@example.com", balance=8000, news=[]),
    4: User(id=4, name="Pedro Santos", email="pedro@example.com", balance=1000, news=[]),
    5: User(id=5, name="Rafaela Silva", email="rafaela@example.com", balance=3000, news=[]),
}


# ======================================
# GET USER
# ======================================

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]


# ======================================
# PUT USER
# ======================================

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    fake_db[user_id] = user
    return {"message": "User updated successfully", "user": user}
