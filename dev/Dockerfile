FROM python:3.7

RUN pip install --upgrade pip

# Install netbox.
RUN mkdir -p /opt
RUN git clone --single-branch --branch master https://github.com/netbox-community/netbox.git /opt/netbox/ && \
    cd /opt/netbox/ && \
    pip install -r /opt/netbox/requirements.txt

# Copy entrypoint script.
COPY dev/entrypoint.sh /opt/netbox/entrypoint.sh

# Work around https://github.com/rq/django-rq/issues/421
RUN pip install django-rq==2.3.2

# Install plugin.
RUN pip install netbox-virtual-circuit-plugin

WORKDIR /opt/netbox/netbox/
