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
```

---

## ⚡️ Quickstart (Copy–Paste This)

```bash
# 1. Clone the project
git clone https://github.com/whereismytime/Blockchain-demo.git
cd Blockchain-demo

# 2. (Optional) Create virtual environment
python -m venv .venv

# For Windows:
.venv\Scripts\activate

# For macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload
```

---

## 🌐 Open in your browser

Once running, open:

- http://127.0.0.1:8000/ — API status
- http://127.0.0.1:8000/docs — Swagger UI
- http://127.0.0.1:8000/redoc — ReDoc view

---

## 📦 Dependencies (from `requirements.txt`)

```txt
fastapi
uvicorn
```

📌 Or regenerate full list:
```bash
pip freeze > requirements.txt
```

---

## 🧠 What's Next?

- [ ] Save blockchain to file (`blockchain.json`)
- [ ] Add transaction structure
- [ ] Add Web UI (HTML/JS)
- [ ] Host on Render / Replit

---

## 👨‍💻 Author

Made with ❤️ by [@whereismytime](https://github.com/whereismytime)  
Feel free to fork, improve, or deploy.
