FROM python:3.12-bullseye

WORKDIR /usr/src/app

RUN git clone https://github.com/Kizitor/Aeris_Project.git

RUN cd Aeris_Project/ && pip3.12 install --no-cache-dir -r requirements.txt

EXPOSE 80/tcp

EXPOSE 5000/tcp

CMD cd Aeris_Project/ && bash ./start.sh