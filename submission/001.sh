# What is the hash of block 654,321?
hash=$(bitcoin-cli -rpcconnect=84.247.182.145 -rpcuser=user_239 -rpcpassword=JoFkBpY9NsUC getblockhash 654321)
echo $hash