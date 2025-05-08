# FastAPI interface for the blockchain
# FastAPI-інтерфейс до блокчейну

from fastapi import FastAPI, HTTPException, Body
from blockchain import Blockchain

app = FastAPI(title="Simple Blockchain API")
bc = Blockchain()

@app.get("/")
def home():
    """Root endpoint / Кореневий ендпоінт"""
    return {"message": "Blockchain API is running 🧱"}

@app.post("/mine_block")
def mine_block(data: str = Body(..., embed=True)):
    """Mine a block with given data / Майнимо блок із даними"""
    block = bc.mine_block(data)
    return {"message": "Block mined successfully", "block": block}

@app.get("/blockchain")
def get_blockchain():
    """Return the full blockchain if valid / Повертає весь блокчейн (якщо валідний)"""
    if not bc.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")
    return {"length": len(bc.get_chain()), "chain": bc.get_chain()}

@app.get("/blockchain/last")
def previous_block():
    """Get the last block in chain / Повертає останній блок у ланцюгу"""
    if not bc.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")
    return bc.get_previous_block()

@app.get("/validate")
def is_blockchain_valid():
    """Check chain integrity / Перевірка цілісності блокчейну"""
    return {"is_valid": bc.is_chain_valid()}
