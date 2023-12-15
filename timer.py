# importe o módulo time
import ???
from playsound import playsound


# defina a função "countdown_timer"
def ???(seconds):
    while seconds > 0:

        mins = int(seconds / 60)
        secs = int(seconds % 60)
        
        timer = f'{mins}:{secs}'
        
        print(timer,end='\r')
        time.sleep(1)
        seconds -= 1
    
    print('Tempo Esgotado!')
    playsound('mixkit-sound.wav')


# digite o tempo em segundos
seconds = input("Digite o tempo em segundos: ")
# chamada da função
countdown_timer(int(seconds))
