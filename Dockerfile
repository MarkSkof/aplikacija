FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/aplikacija
COPY . ./
RUN pip install -r requirements.txt


