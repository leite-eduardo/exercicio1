# Importando as bibliotecas
from time import sleep
from threading import Thread
from random import uniform

status = 0
arquivos = ['trabalho.txt','foto.png','TCC.docx','boleto.pdf']
print(f'A lista de arquivos a ser impresso: {arquivos}')
# Definindo a função fila
def fila(threadName):
    global status
    while ( len(arquivos) != 0 ):
        if ( status == 0 ):
            status = 1
            arquivo = arquivos.pop(0)
            sleep(2)
            print(f'[{threadName}]: Iniciando a impressão de {arquivo}')
            impressao(threadName,arquivo)
        print(f'[{threadName}]: Aguardando...')
        sleep(2)

def impressao(threadName,arquivo):
    global status
    sleep(uniform(2,10))
    print(f'[{threadName}]: {arquivo} impresso com sucesso!')
    status = 0


t1 = Thread(target=fila, args=('Thread 1',))
t2 = Thread(target=fila, args=('Thread 2',))

t1.start()
t2.start()

t1.join()
t2.join()

print('Fila de impressão vazia...')
sleep(5)
