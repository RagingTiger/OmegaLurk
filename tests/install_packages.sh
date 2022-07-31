# install python testing packages
pip install -r tests/requirements.txt && \
if cat tests/requirements.txt | grep -q seleniumbase; then
  apt-get install -y \
    gpg && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | \
    gpg --dearmor | \
    tee /usr/share/keyrings/google.gpg > /dev/null && \
  echo "deb [signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update && apt-get install -y \
  google-chrome-stable && \
  rm -rf /var/lib/apt/lists/* && \
  sbase install chromedriver
fi
