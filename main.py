import fastapi as _fastapi
import block_chain as bc

blockchain = bc.BlockChain()
app = _fastapi.FastAPI()

#endpoint to mine a new block
@app.post("/mine")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="Blockchain is invalid")
    block = blockchain.mine(data)
    return block

#endpoint to get the full blockchain
@app.get("/blockchain")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="Blockchain is invalid")
    return blockchain.chain

#endpoint to check whether the blockchain is valid
@app.get("/is_valid")
def is_block_chain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="Blockchain is invalid")
    return blockchain.is_chain_valid()