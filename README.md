# 🧱 Simple Blockchain API

A lightweight educational blockchain implementation built with **Python 3.13+** and **FastAPI**.  
Ideal for learning concepts like Proof-of-Work, block validation, and RESTful API design.

---

## 🚀 Features

- ✅ **Proof-of-Work** (PoW) algorithm
- 🔗 Block validation and hashing
- 🧱 Full blockchain storage in memory
- ⚙️ RESTful API to mine, view, and verify the chain
- 📦 Simple setup, no database or third-party dependencies

---

## 📬 API Endpoints

| Method | Endpoint               | Description                                 |
|--------|------------------------|---------------------------------------------|
| `GET`  | `/`                    | Check API status                            |
| `POST` | `/mine_block`          | Add a new block with custom data            |
| `GET`  | `/blockchain`          | Return full blockchain (if valid)           |
| `GET`  | `/blockchain/last`     | Get the most recent block                   |
| `GET`  | `/validate`            | Check integrity of the entire chain         |

### 🧪 Example request (POST `/mine_block`):
```json
{
  "data": "This is a new block"
}
