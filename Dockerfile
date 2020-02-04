FROM python:3-alpine

ADD getExchange.py /

COPY requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt
COPY . /tmp/

COPY openexchangerates.conf /tmp/

CMD [ "python3", "./getExchange.py" ]
