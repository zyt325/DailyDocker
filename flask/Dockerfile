FROM harbor.base-fx.com/itd/python:3.7.4

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host  mirrors.aliyun.com --timeout 30 -U pip
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host  mirrors.aliyun.com --timeout 30 -r requirements.txt
