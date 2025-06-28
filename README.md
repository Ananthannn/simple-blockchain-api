# Simple Blockchain API with Python & FastAPI ⛓️

A lightweight blockchain implementation built from scratch in Python, wrapped in a FastAPI web server for interactive block mining, chain validation, and ledger inspection.

---

## 🚀 Features

- **Proof of Work (PoW):** Simple mining algorithm for block validation.
- **Block Mining:** Add new blocks with custom data.
- **Chain Validation:** Check blockchain integrity at any time.
- **Cryptographic Hashing:** Uses SHA-256 for block hashes.
- **RESTful API:** FastAPI server with Swagger UI for interactive testing.
- **Educational:** Designed for learning and visualization—no tokens, wallets, or real-world economics.

---

## 🧠 Core Concepts

- **Block Structure:** Each block contains an index, timestamp, data, proof, and previous hash.
- **Proof of Work:** Find a number so that `sha256(proof² - previous_proof²)` starts with `0000`.
- **Immutability:** Any tampering breaks the chain’s validity.
- **FastAPI:** Lightweight Python web framework for HTTP endpoints.

---

## 📦 Project Structure

```
simple-blockchain-api/
├── block_chain.py        # Blockchain logic (mining, hashing, validation)
├── main.py               # FastAPI server exposing REST endpoints
├── requirements.txt      # Python dependencies
└── .gitignore            # Ignores pycache and other system files
```

---

## 🛠️ Local Development

### 1. Clone the repository

```bash
git clone https://github.com/Ananthannn/simple-blockchain-api.git
cd simple-blockchain-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API server

```bash
uvicorn main:app --reload
```

Then open your browser at:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📚 API Reference

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| POST   | `/mine`       | Mine a new block with custom data |
| GET    | `/blockchain` | Get the full blockchain (ledger)  |
| GET    | `/is_valid`   | Validate the blockchain integrity |

#### Example POST `/mine` request body:
```json
{
  "data": "Alice sends 5 BTC to Bob"
}
```

---

## 🔒 Security Notice

This project is for educational purposes only. It does **not** implement:
- Network consensus or peer-to-peer node syncing
- Transaction signatures or identity verification
- Persistent or distributed data storage
- Real-world token/coin economics

---

## 📄 License

MIT License

---

---

## 🌐 Connect with Me

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/v_ananthann_?igsh=MWFlcHo5a2pvNm5yaA==)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/v-anantha-krishnan-739b942a5/)
[![Email](https://img.shields.io/badge/Email-%23D14836.svg?style=flat&logo=gmail&logoColor=white)](mailto:vananthakrs@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?style=flat&logo=github&logoColor=white)](https://github.com/Ananthannn)

---

> Made with ❤️ by V Anantha Krishnan
