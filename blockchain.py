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
    
    
    def getPreviousHash (self):
        return self.chain[-1]
    
    
    # this will get the PoW by mining
    def proofOfWork (self, previousHash):
        
        proofCounter = 1;
        proofMatched = False
        
        while proofMatched is False:
            
            hashed = hashlib.sha256 (str (proofCounter ** 2 - previousHash ** 2).encode()).hexdigest()
            
            if hashed[ : 4] == '0000':
                proofMatched = True
            else:
                proofCounter += 1
                
            return proofCounter
        
      
        
      
    # return the hash of the block    
    def hash (self, block):
        
        # encode the json string of block
        encodedBlock = json.dumps (blocks, sort_keys = True).encode()
        
        return hashlib.sha256 (encodedBlock).hexdigest()
    
    
    
    # to Verify the the whole chain is valid to remove malicious activities
    def isChainValid (self, chain):
        
        previousBlock = chain[0]       
        currentBlockIndex = 1;
        
        
        #looping through whlole chain of blocks
        while currentBlockIndex < len (chain):
            
            block = chain[currentBlockChain]
            
            if (block['previousHash'] != self.hash (previousBlock)):
                return False
            
            previousProof = previousBlock ['proof']
            currentProof = block['proof']
            
            hashed = hashlib.sha256 (str(currentProof ** 2 - previousProof ** 2).encode()).encode()
            if (hashed[ : 4] != '0000'):
                return False
            
            previousBlock = block
            currentBlockIndex += 1
            
        return True
            




