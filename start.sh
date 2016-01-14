#!/bin/bash
#edit by Zjj

WORKDIR='/app/src'

init(){
  echo 'image iseeyou not exist'
  echo 'building docker image ...'
  echo
  docker build -t iseeyou .
}

if [[ $(docker images -q iseeyou  ) == ""  ]]; then
  init
fi

docker run -it -d -p 3000:3000 -v $(pwd):$WORKDIR iseeyou python $WORKDIR/app.py -log_file_prefix=$WORKDIR/log/app.log

