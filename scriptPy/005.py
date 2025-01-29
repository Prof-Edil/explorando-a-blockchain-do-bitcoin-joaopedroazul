import subprocess

commandGetPk = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getrawtransaction  "37d966a263350fe747f1c606b159987545844a493dd38d84b070027a895c4517" 1 | jq .vin[].txinwitness[1]'
resultGetPk = subprocess.check_output(commandGetPk, shell=True, text=True).split("\n")
resultGetPk = resultGetPk[:-1] #tirando o enter do vetor

commandCreateMultiSig = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" createmultisig 1 '+ '[\\"'+resultGetPk[0].split('"')[1]+'\\"'+','+'\\"'+resultGetPk[1].split('"')[1]+'\\"'','+ '\\"'+resultGetPk[2].split('"')[1]+'\\"'','+ '\\"'+resultGetPk[3].split('"')[1]+'\\"'+']  | jq .address '
resultCreateMultiSig = subprocess.check_output(commandCreateMultiSig, shell=True, text=True)
print(resultCreateMultiSig.split('"')[1])
