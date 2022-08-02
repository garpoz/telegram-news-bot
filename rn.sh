#! /bin/bash
#* * * * * cd ~/Wallet&&./rn.sh
#one minute run
#lsof -t -i tcp:80 | xargs kill -9

if ps -e|egrep main
then
    echo "is run..."
else
    nohup python main.py&
fi
