
from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.com.br',
    ])

with open('coroa.txt','r') as livro:
    with open ('coroa_traduzida.txt','w',encoding ='utf-8')as trad:
        
        for t in livro:
            try:
                traduzida = open ('coroa_traduzida.txt','a',encoding ='utf-8')
                tt = translator.translate(t, dest='pt')
                traduzida.write(tt.text)
            except:
                continue
           


print('terminado')
