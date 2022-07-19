# base python
FROM python:3.10

# set default port
EXPOSE 8484

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
RUN apt-get update && apt-get install -y tzdata && \
    pip3 install -r requirements.txt

# set command
CMD streamlit run app.py
