FROM alpine:3.1
RUN apk add --update python py-pip
COPY app.py/app.py
EXPOSE 8080
CMD [ "python", "app.py","-p 8080" ]
