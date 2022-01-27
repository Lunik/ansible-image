
FROM python:{{ python }}-{{ os }}


{% if 'alpine' in os -%}
RUN apk upgrade --update --no-cache \
  && apk add git openssh-client openssl
{%- else -%}
RUN apt update \
  && apt upgrade -y --no-install-recommends \
  && apt install -y --no-install-recommends \
  git openssh-client openssl \
  && rm -rf /var/lib/apt/lists/*
{%- endif %}

COPY requirements.txt /tmp/requirements.txt
{% if 'alpine' in os -%}
RUN apk add --update --no-cache --virtual .build \
  build-base libffi-dev python3-dev openssl-dev cargo \
{%- else -%}
RUN apt update \
  && apt install -y --no-install-recommends \
  build-essential libssl-dev libffi-dev python3-dev cargo \
{%- endif %}
  && pip3 install --upgrade pip \
  && pip3 install -r /tmp/requirements.txt \
{% if 'alpine' in os -%}
  && apk del .build
{%- else -%}
  && apt remove -y \
  build-essential libssl-dev libffi-dev python3-dev cargo  \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*
{%- endif %}

WORKDIR /opt/ansible

VOLUME /opt/ansible

CMD ["ansible"]