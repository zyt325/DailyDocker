FROM harbor.base-fx.com/dev/python:3.7.4

RUN mkdir -p /app/packages
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --extra-index-url https://pypi.org/simple -i http://10.14.7.21:8080/ --trusted-host 10.14.7.21 --timeout 120 -r requirements.txt
VOLUME /app/packages
EXPOSE 8080
ENTRYPOINT ["pypi-server", "-p", "8080"]
CMD ["packages"]
