FROM python:3.6.9-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python","main.py"]
