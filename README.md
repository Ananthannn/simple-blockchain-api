# 🧱 Simple Blockchain API with Python & FastAPI

A lightweight blockchain implementation built from scratch in Python, wrapped in a FastAPI web server for interactive block mining, chain validation, and ledger inspection.

---

## 🚀 Project Overview

This project demonstrates how a basic blockchain works using Python and FastAPI.

It includes features like:

- Proof of Work (PoW) algorithm
- Mining new blocks with validation
- Cryptographic hashing (SHA-256)
- Chain integrity validation
- RESTful API using FastAPI
- Swagger UI for interactive testing

The aim is to **learn and visualize** how blockchains work at a fundamental level — no tokens, no wallets, just raw blocks, links, and logic.

---

## 🧠 Core Concepts

- **Block Structure:** Each block contains an index, timestamp, data, proof, and hash of the previous block.
- **Proof of Work:** A computational puzzle where miners must find a number such that `sha256(proof² - previous_proof²)` starts with `0000`.
- **Immutability:** Any tampering breaks the chain's validity.
- **FastAPI:** Lightweight Python web framework used to expose blockchain functions over HTTP.

---

## 📦 Project Structure

├── block_chain.py # Blockchain logic (mining, hashing, validation)

├── main.py # FastAPI server exposing REST endpoints

├── requirements.txt # Python dependencies

└── .gitignore # Ignores pycache and other system files


---

## ⚙️ How to Run

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

### Then open your browser at:
```bash
http://127.0.0.1:8000/docs
```

## API Reference

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| POST   | `/mine`       | Mine a new block with custom data |
| GET    | `/blockchain` | Get the full blockchain (ledger)  |
| GET    | `/is_valid`   | Validate the blockchain integrity |



### Example POST /mine request body:
```
{
  "data": "Alice sends 5 BTC to Bob"
}
```




### 🔒 Security Notice

This project is for educational purposes only. It does not implement:

-- Network consensus or peer-to-peer node syncing

--Transaction signatures or identity verification

-- Persistent or distributed data storage

-- Real-world token/coin economics


## 📜 License

This project is open-source and available under the [MIT](https://choosealicense.com/licenses/mit/) License.




## 🙋‍♂️ Questions?

Feel free to open an issue or fork the repo and contribute!

🔗 GitHub: https://github.com/Ananthannn/simple-blockchain-api

