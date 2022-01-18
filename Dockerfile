FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . .


# RUN python3 telegrambot.py
EXPOSE 8090
ENTRYPOINT ["python3", "telegrambot.py" ]
# CMD [ "python3", "-m" , "telegrambot.py"]