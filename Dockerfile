FROM python:3
ADD Hello.py /
RUN pip install pystrich
CMD [ "python", "./Hello.py" ]
EXPOSE 8080
