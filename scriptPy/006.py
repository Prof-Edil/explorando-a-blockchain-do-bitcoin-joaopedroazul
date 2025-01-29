import subprocess

commandGetBlockHashOut = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblockhash  256128 '
resultGetBlockHashOut = subprocess.check_output(commandGetBlockHashOut, shell=True, text=True)

commandGetBlockOut = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblock '+resultGetBlockHashOut.split("\n")[0]+' 2 | jq .tx[0].txid '#.vout[0].scriptPubKey.address' 
resultGetBlockOut = subprocess.check_output(commandGetBlockOut, shell=True, text=True).split('\n')[0]

commandGetBlockHashIn = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblockhash  257343 '
resultGetBlockHashIn = subprocess.check_output(commandGetBlockHashIn, shell=True, text=True)

commandGetBlockIn = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblock '+resultGetBlockHashIn.split("\n")[0]+'  1 | jq .tx[] ' 
resultGetBlockIn = subprocess.check_output(commandGetBlockIn, shell=True, text=True).split('\n')
resultGetBlockIn.remove('')

test = 0 
index = 0

for x in range(1,len(resultGetBlockIn)):
    commandGetBlockInTxid = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getrawtransaction '+resultGetBlockIn[x]+'  1 | jq .vin[].txid ' 
    resultGetBlockInTxid = subprocess.check_output(commandGetBlockInTxid, shell=True, text=True).split('\n')
    resultGetBlockInTxid = resultGetBlockInTxid[:-1]
    for y in range(0,len(resultGetBlockInTxid)):
        if str(resultGetBlockInTxid[y].split('"')[1]) == str(resultGetBlockOut.split('"')[1]):
            test = 1
            break
    if test == 1:
        index = x
        test = 0
        break   

commandGetBlockIn = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getrawtransaction '+resultGetBlockIn[index]+'  1 | jq .txid ' 
resultGetBlockIn1 = subprocess.check_output(commandGetBlockIn, shell=True, text=True).split('\n')[0].split('"')[1]
print(resultGetBlockIn1)
