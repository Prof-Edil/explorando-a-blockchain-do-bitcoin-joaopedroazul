# How many new outputs were created by block 123,456?
block=$(bitcoin-cli -rpcconnect="84.247.182.145" -rpcuser="user_239" -rpcpassword="JoFkBpY9NsUC" getblockstats 123456 )
echo $block | jq .outs