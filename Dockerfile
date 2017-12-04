FROM ffpy:0.1

ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 9100

CMD ["python", "app.py"]
