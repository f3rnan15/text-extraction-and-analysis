FROM ubuntu:latest

RUN apt update && apt upgrade -y && apt install git -y && apt install python3 -y && apt install python3-pip -y && apt install git -y && apt install python3-venv -y

#RUN apt install -y docker.io 

RUN apt autoremove -y && apt clean

RUN git clone https://github.com/f3rnan15/text-extraction-and-analysis.git

WORKDIR /text-extraction-and-analysis

RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install requests wordcloud matplotlib pandas beautifulsoup4 pytest wordcloud lxml

RUN apt install -y xvfb

ENV DISPLAY=:99

#RUN docker pull lfoppiano/grobid:0.7.2 && docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

CMD ["/bin/bash"]