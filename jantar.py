from time import sleep
from threading import Thread
from random import uniform
import random

garfo1 = 0
garfo2 = 0
filosofos = ['Descartes','Aristóteles','Nietzsche','Platão','Marx']
print('Iniciando jantar')

def jantar():
    i = 0
    filosofo = random.choice(filosofos)
    filosofos.remove(filosofo)
    while(i != 1): 
        print(f'O filósofo {filosofo} está pensando...') 
        sleep(uniform(2,10)) 
        print(f'O filósofo {filosofo} está com fome...') 
        comer(filosofo) 
        i += 1         
    sleep(uniform(2,10)) 
    print(f'O filósofo {filosofo} saiu da mesa.') 

def comer(filosofo):
    global garfo1
    global garfo2 
    garfos = {
            f'{filosofo}':[0,0]
    }
    sleep(uniform(2,10))
    if ( garfo1 == 0): 
        garfo1 = 1 
        garfos[filosofo][1] = 1
        print(f'O filósofo {filosofo} pegou o garfo da direita.') 
    else:
        print(f'O filósofo {filosofo} tentou pegar o garfo da direita, mas ele está ocupado.')         
    sleep(uniform(2,10))        
    if ( garfo2 == 0 ):
        garfo2 = 1 
        garfos[filosofo][0] = 1 
        print(f'O filósofo {filosofo} pegou o garfo da esquerda.')  
    else:
        print(f'O filósofo {filosofo} tentou pegar o garfo da esquerda, mas ele está ocupado.')  
        sleep(uniform(2,10)) 
    
    if ( garfos[filosofo][0] == 1 and garfos[filosofo][1] == 1 ): 
        print(f'O filósofo {filosofo} começou a comer.')  
        sleep(uniform(2,10)) 
        print(f'O filósofo {filosofo} devolveu os garfos.') 
        garfo1 = 0 
        garfo2 = 0 
    else:
        print(f'O filósofo {filosofo} não conseguiu comer pois um dos garfos está ocupado.') 
    if ((garfos)[filosofo][0] == 1): 
            garfo2 = 0 
    if ((garfos)[filosofo][1] == 1): 
            garfo1 = 0      
    sleep(2) 

t1 = Thread(target=jantar)
t2 = Thread(target=jantar)

t1.start()
t2.start()

t1.join()
t2.join()

print('Fim do jantar')
