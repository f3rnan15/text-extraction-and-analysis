# text-extraction-and-analysis

conda create --name open_science_env python=3.9
conda activate open_science_env
pip install requests wordcloud matplotlib pandas beautifulsoup4 pytest wordcloud
sudo apt install docker
sudo docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
