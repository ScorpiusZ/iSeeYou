From debian:jessie

# install python 
RUN apt-get update && apt-get install -y \
       python2.7 \
       python2.7-dev \
       python-pip \
       python-pandas \ 
       python-sklearn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy tornado


