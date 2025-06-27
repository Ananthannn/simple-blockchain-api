import datetime as _dt
import hashlib as _hl
import json as _json

class BlockChain:
    def __init__(self):
        self.chain = list()
        genesis_block = self.create_block(
            data="Genesis Block",
            proof=1,
            previous_hash="0",
            index=1
        )
        self.chain.append(genesis_block)

    def create_block(self , data:str , proof:int , previous_hash: str , index:int ) -> dict:
        block ={
            'index': index,
            'timestamp': str(_dt.datetime.now()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash
        }

        return block
    
    def get_previous_block(self) -> dict:
        return self.chain[-1]
    
    def proof_of_work(self , previous_proof:int)->int:
        new_proof = 1

        while True:
            guess = str(new_proof**2 - previous_proof**2).encode()
            guess_hash = _hl.sha256(guess).hexdigest()
            if guess_hash[:4] == "0000":
                return new_proof   
            else:
                new_proof += 1

    def hash(self, block: dict) -> str:
        encoded_block = _json.dumps(block, sort_keys=True).encode()
        return _hl.sha256(encoded_block).hexdigest()

    def mine(self, data: str):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        block = self.create_block(data, proof, previous_hash, len(self.chain)+1)
        self.chain.append(block)
        return block
    
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            guess = str(current_proof**2 - previous_proof**2).encode()
            guess_hash = _hl.sha256(guess).hexdigest()
            if guess_hash[:4] != "0000":
                return False

        return True
    

