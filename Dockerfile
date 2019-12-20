FROM python:3
ADD Hello.py /
RUN pip install pystrich
CMD [ "python", "./App.py" ]
EXPOSE 8080