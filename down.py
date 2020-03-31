from urllib.request import urlretrieve

def download(url):
    urlretrieve(str(url),'novo')

url = input('insira o url')

download(url)
