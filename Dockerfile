FROM python:3.7.4-slim-buster

RUN apt-get update && apt-get install -y apt-utils
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    build-essential \
    pkg-config \
    libicu-dev \
    python3.7-icu

WORKDIR root

CMD ["bash"]