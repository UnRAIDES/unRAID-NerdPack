FROM python


WORKDIR /source



COPY requirements.txt .



RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./upgrade.packages.py /source/upgrade.packages.py


