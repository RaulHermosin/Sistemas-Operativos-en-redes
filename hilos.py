import threading


def info():
    print(f'{threading.current_thread().name} {threading.get_native_id()}')


hilo1 = threading.Thread(target=info)

def ejecutar():
    hilo1.start()


while True:
    ejecutar()


