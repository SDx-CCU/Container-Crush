FROM python:3.6.1-alpine
RUN pip install flask
CMD ["python","Hello.py"]
COPY Hello_World.py /Hello.py
EXPOSE 8080