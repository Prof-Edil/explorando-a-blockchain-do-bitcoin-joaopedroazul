import subprocess

command = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getdescriptorinfo "tr(xpub6Cx5tvq6nACSLJdra1A6WjqTo1SgeUZRFqsX5ysEtVBMwhCCRa4kfgFqaT2o1kwL3esB1PsYr3CUdfRZYfLHJunNWUABKftK2NjHUtzDms2/100/100)" | jq .descriptor '
result = subprocess.check_output(command, shell=True, text=True)
command2 = 'bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" deriveaddresses '+result
result2 = subprocess.check_output(command2, shell=True, text=True)
print(str(result2.split('"')[1]))
