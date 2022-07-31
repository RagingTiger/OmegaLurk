# base python
FROM python:3.10.5 AS builder

# set default port
EXPOSE 8484

# set build cache inline
ARG BUILDKIT_INLINE_CACHE=1

# set env
ENV TZ=America/New_York
ENV DEBIAN_FRONTEND=noninteractive
ENV HF_HOME=/models/huggingface
ENV TRANSFORMERS_CACHE=${HF_HOME}/transformers

# create workdir
WORKDIR /OmegaLurk

# copy source
COPY . /OmegaLurk

# update and pip install
RUN apt-get update && apt-get install -y \
      tzdata && \
    pip3 install -r requirements.txt

# setup app
FROM builder AS app

# set command
CMD ["streamlit", "run", "app.py"]

# setup test
FROM builder AS test

# install testing packages
RUN bash tests/install_packages.sh

# set test command
CMD ["bash", "tests/run_tests.sh"]
