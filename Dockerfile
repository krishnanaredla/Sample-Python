FROM python:3.8-slim

COPY ./app.py ./app.py

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]