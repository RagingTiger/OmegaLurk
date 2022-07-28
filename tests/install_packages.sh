# install python testing packages
pip install -r tests/requirements.txt

# add chrome browser to sources and install
if cat tests/requirements.txt | grep -q seleniumbase; then
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update && apt-get install -y \
  google-chrome-stable && \
  rm -rf /var/lib/apt/lists/* && \
  sbase install chromedriver
fi
