FROM python:3

# Japanese Localization
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# file copy
ADD requirements.txt /tmp/

# python package
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

CMD ["python", "/tmp/main.py"]