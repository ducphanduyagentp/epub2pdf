FROM python:3

ADD app.py /app.py
ADD templates/ /templates/

RUN apt-get update && apt-get -y install wget sudo calibre && apt-get -y remove calibre && \
    sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin

CMD python3 /app.py
