from flask import Flask, jsonify    #flask for web app
import json                         # wrapping up the details of block

import datetime                     # storing information of blocks and transaction (time stamp) 

import hashlib                      # for hashing


class Blockchain:
    
    def __init__(self):
        
        # list containing all the blocks
        self.chain = []
        
        self.createBlock (proof = 1, previousHash = '0') 
        
        
    #Creating the block after we get the PoW by mining the block
    
    def createBlock (self, proof, previousHash):
        
        block = {
                    'index'         : len (self.chain) + 1,
                    'timestamp'     : str(datetime.datetime.now()), 
                    'proof'         : proof,
                    'previousHash'  : previousHash
                }
        
        self.chain.append (block)
        return block
    
    
    def getPreviousBlock (self):
        return self.chain[-1]
    
    
    # this will get the PoW by mining
    def proofOfWork (self, previousProof):
        
        proofCounter = 1;
        proofMatched = False
        
        while proofMatched is False:
            
            hashed = hashlib.sha256 (str (proofCounter ** 2 - previousProof ** 2).encode()).hexdigest()
            
            if hashed[ : 4] == '0000':
                proofMatched = True
            else:
                proofCounter += 1
                
            return proofCounter
        
      
        
      
    # return the hash of the block    
    def getHash (self, block):
        
        # encode the json string of block
        encodedBlock = json.dumps (blocks, sort_keys = True).encode()
        
        return hashlib.sha256 (encodedBlock).hexdigest()
    
    
    
    # to Verify that the whole chain is valid so to remove malicious activities
    def isChainValid (self, chain):
        
        previousBlock = chain[0]       
        currentBlockIndex = 1;
        
        
        #looping through whlole chain of blocks
        while currentBlockIndex < len (chain):
            
            block = chain[currentBlockChain]
            
            if (block['previousHash'] != self.getHash (previousBlock)):
                return False
            
            previousProof = previousBlock ['proof']
            currentProof = block['proof']
            
            hashed = hashlib.sha256 (str(currentProof ** 2 - previousProof ** 2).encode()).encode()
            if (hashed[ : 4] != '0000'):
                return False
            
            previousBlock = block
            currentBlockIndex += 1
            
        return True
    
    

    
    
    
    
# Creating a web app
app = Flask (__name__)
    
# BlockChain object created
blockchain = BlockChain ()
    
''' GET request from HTTP Postman that will add new block to the
    blockchain and in response return '''
@app.route ('/mineBlock', methods = ['GET'])
    
''' This will mine a new block by doing the proof of work 
    and add the block to the block chain and give response to GET request'''
def mineBlock ():
    
    # Getting the requirements for createBlock , proof and previousHash
    previousBlock = blockchain.getPreviousBlock ()
    previousProof = previousBlock ['proof']
    
    proof = blockchain.proofOfWork (previousProof)
    previousHash = blockchain.getHash (previousBlock)
    
    block = blockchain.createBlock (proof, previousHash)
    
    # response for the GET method for HTTP Postman interface
    response =  {
                    'message'       : 'Successfully Mined the Block',
                    'index'         : block['index'],
                    'timestamp'     : block['timestamp'],
                    'proof'         : block['proof'],
                    'previousHash'  : block['previousHash']
                }
    
    # Returning the response as json and with HTTP status code (200) = successful
    return jsonify (response), 200
    
    
            




