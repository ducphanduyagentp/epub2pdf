FROM python:3

RUN apt-get update && apt-get -y install wget sudo calibre && apt-get -y remove calibre && \
    sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin

ADD app.py /app.py

ADD templates/ /templates/

ADD requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

CMD python3 /app.py

