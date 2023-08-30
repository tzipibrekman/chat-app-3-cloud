#!bin/bash
if [ git rev-parse -q --verify "refs/tags/$1" ] && [ git cat-file -e "$1" ];then
   git tag $1 $2
   git push origin $1

   docker build -t chat-app:$1 .
   docker push chat-app:$1
else
   echo "wrong params"
fi
