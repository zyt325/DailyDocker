FROM harbor.base-fx.com/itd/sentry:8.22.0

COPY pip.conf /etc/
RUN apt-get update
RUN apt install libldap2-dev -y
RUN apt install libsasl2-2 libsasl2-dev -y
#RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
#RUN pip install sentry-ldap-auth
RUN pip install python-ldap
RUN pip install sentry-ldap-auth
