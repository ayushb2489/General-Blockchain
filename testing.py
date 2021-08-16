'''RESPONSES

1 REQUEST => http://127.0.0.1:5000/getChain


RESPONSE = 
{
    "chain": [
        {
            "index": 1,
            "previousHash": "0",
            "proof": 1,
            "timestamp": "2021-08-16 20:58:20.568031"
        }
    ],
    "length": 1
}



2 REQUEST => http://127.0.0.1:5000/mineBlock

RESPONSE = 
{
    "index": 2,
    "message": "Successfully Mined the Block",
    "previousHash": "3231bda8936da0502cc99d64d77d7beb61fd40aacb53561a0232bf2e39e6745e",
    "proof": 533,
    "timestamp": "2021-08-16 20:59:14.451984"
}

3  REQUEST => http://127.0.0.1:5000/mineBlock
4  REQUEST => http://127.0.0.1:5000/mineBlock
5  REQUEST => http://127.0.0.1:5000/mineBlock
6  REQUEST => http://127.0.0.1:5000/mineBlock
7  REQUEST => http://127.0.0.1:5000/mineBlock
8  REQUEST => http://127.0.0.1:5000/mineBlock
9  REQUEST => http://127.0.0.1:5000/mineBlock
10 REQUEST => http://127.0.0.1:5000/mineBlock

RESPONSES => 8 RESPONSES 





11 REQUEST => http://127.0.0.1:5000/getChain

RESPONSE = 
{
    "chain": [
        {
            "index": 1,
            "previousHash": "0",
            "proof": 1,
            "timestamp": "2021-08-16 20:58:20.568031"
        },
        {
            "index": 2,
            "previousHash": "3231bda8936da0502cc99d64d77d7beb61fd40aacb53561a0232bf2e39e6745e",
            "proof": 533,
            "timestamp": "2021-08-16 20:59:14.451984"
        },
        {
            "index": 3,
            "previousHash": "109cf798bb3bd33516c1c17016ed43a0b384468ed853055a433e17a20c61a216",
            "proof": 45293,
            "timestamp": "2021-08-16 21:00:36.646171"
        },
        {
            "index": 4,
            "previousHash": "0897d8accd843026d2cbc783b22136b70000d3afd9118d70172c417f7ae3dd54",
            "proof": 21391,
            "timestamp": "2021-08-16 21:00:37.020400"
        },
        {
            "index": 5,
            "previousHash": "821848e4c4904952fe05cd470fed1a443dd782b5b79a07c04d32d42351f14606",
            "proof": 8018,
            "timestamp": "2021-08-16 21:00:37.532912"
        },
        {
            "index": 6,
            "previousHash": "da7e70864d289ac5d90a0813cc1b101f0c8e1c29ea7f2e90675938c2ef54558f",
            "proof": 48191,
            "timestamp": "2021-08-16 21:00:38.080955"
        },
        {
            "index": 7,
            "previousHash": "6ef04ca5019155ec953e87bb168e759be10ba23d1bfc374b6c99bfcd03696190",
            "proof": 19865,
            "timestamp": "2021-08-16 21:00:38.516707"
        },
        {
            "index": 8,
            "previousHash": "d9fd25f9ac17d8808fb52b0bf5417c90a49bbb0ddea433c6f96c3e2b74c20d2c",
            "proof": 95063,
            "timestamp": "2021-08-16 21:00:39.114309"
        },
        {
            "index": 9,
            "previousHash": "0d426cbf769ac653904685a2f4bb822771f0ac73ccaaf6e1a4dea415ad6d1c3f",
            "proof": 15457,
            "timestamp": "2021-08-16 21:00:39.470249"
        },
        {
            "index": 10,
            "previousHash": "dc6d05dfb9448df8316f614340f95432992cee1f3ac558cdabb876ed122159da",
            "proof": 15479,
            "timestamp": "2021-08-16 21:00:40.086039"
        }
    ],
    "length": 10
}



12 REQUEST => http://127.0.0.1:5000/isValid

RESPONSE = 
{
    "message": "Blockchain is valid"
}

