from winsound import Beep as b

# lista de frequencias:
f = [528,528,594,528,704,660,528,528,594,528,792,704,
     880,880,1056,880,704,660,594,933,933,880,704,792,704]

#lista de tempos em milisegundos:
t = [300,300,500,500,400,1100,200,200,600,600,400,1100,200,
     200,600,400,400,400,1000,200,200,600,600,600,1200]

#lista de sílabas da letra:
s = ['PA','RA','BÉNS','PRA','VO','CÊ','NES','SA','DATA','QUE',
     'RI','DA','MUI','TAS','FE','LI','CI','DA','DES','MUITOS',
     'A','NOS', 'DE', 'VI','DA!']

for i in range(len(f)):
    #printando a letra segundo a melodia:
    print(s[i],end=' ')
    #Tocando a musica com a biblioteca winsound
    b(f[i],t[i])

    
