FROM ubuntu:latest

RUN apt update && apt upgrade -y && apt install git -y && apt install python3 -y && apt install python3-pip -y && apt install git -y && apt install python3-venv -y

RUN apt autoremove -y && apt clean

RUN git clone https://github.com/f3rnan15/text-extraction-and-analysis.git

WORKDIR /text-extraction-and-analysis

RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install requests wordcloud matplotlib pandas beautifulsoup4 pytest wordcloud lxml

CMD ["/bin/bash"]