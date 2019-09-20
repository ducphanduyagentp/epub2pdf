FROM python:3

RUN apt-get update && apt-get -y install wget sudo calibre && apt-get -y remove calibre && \
    sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
