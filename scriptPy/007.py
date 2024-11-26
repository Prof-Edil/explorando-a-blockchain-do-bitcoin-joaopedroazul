import subprocess

commandGetBlockHash = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblockhash  123321 '
resultGetBlockHash = subprocess.check_output(commandGetBlockHash, shell=True, text=True)

commandGetBlockTx = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblock '+resultGetBlockHash.split("\n")[0]+' 1 | jq .tx[] '
resultGetBlockTx = subprocess.check_output(commandGetBlockTx, shell=True, text=True).split("\n")
resultGetBlockTx.remove('')

addressResult = ""
for i in range(0,len(resultGetBlockTx)):
    commandGetBlockVout = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getrawtransaction  '+resultGetBlockTx[i]+' 2  | jq .vout[].n'
    resultGetBlockVout = subprocess.check_output(commandGetBlockVout, shell=True, text=True).split('\n')
    resultGetBlockVout.remove('')
    #resultGetBlockOut1.remove('')
    for y in range(0,len(resultGetBlockVout)):
        commandGetUtxo = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" gettxout '+resultGetBlockTx[i].split('"')[1]+' '+resultGetBlockVout[y]+' | jq .scriptPubKey.address'  
        #print(commandGetUtxo)
        resultGetUtxo = subprocess.check_output(commandGetUtxo, shell=True, text=True)#.split('{')[1].split("}")[0].split('\n')
        if len(resultGetUtxo) > 10:
            addressResult = resultGetUtxo.split('"')[1]
            break
    if  len(addressResult) > 5:
        break 
print(addressResult)