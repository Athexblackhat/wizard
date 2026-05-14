FROM python:3.10
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Athexblackhat/wizard && cp -r wizard /usr/src/wizard
WORKDIR /usr/src/redhawk
CMD [ "python", "./wizard.py", "<<<","$'fix'" ]
CMD [ "python", "./wizard.py", "<<<","$'update'" ]
CMD [ "python", "./wizard.py" ]
