import subprocess

commandGetBlockHash = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getrawtransaction  "e5969add849689854ac7f28e45628b89f7454b83e9699e551ce14b6f90c86163" 1 | jq .vin[].txinwitness[2] '
resultGetBlockHash = subprocess.check_output(commandGetBlockHash, shell=True, text=True).split("\n")[0].split('"')[1]
print(type(resultGetBlockHash))

if resultGetBlockHash[0:2] == '63' and resultGetBlockHash[2:4] == '21': #se a chave e compacta e possui 33 bytes
    print(resultGetBlockHash[4:70])
