import concurrent.futures as cf
import time
import psutil as psu
import numpy as np
import multiprocessing as mp
from spinner_progress import Spinner
import asyncio

# lowest blir satt till 0
# highest blir högsta talet i en uint32 429... nånting
lowest = np.iinfo(np.uint32).min
highest = np.iinfo(np.uint32).max

# med hjälp av randint så väljs en random key ut inom intervallet av lowest-highest en uint32 kan innehålla. 
key = np.random.randint(low=lowest, high=highest, dtype="uint32")

key = 121830 # Hårdkodar key för att det ska gå snabbare, orka vänta liksom..

# False = kör bara på de fysiska, alltså INGA LOGISKA.
# True = kör med de fysiska och logiska.
cpu_cores = psu.cpu_count(logical=True) 

# Skapar en global int för att kunna komma åt den överallt
def init_globals(key_not_found):
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found


def crack_key(cpu_num, key_count, key_end):
    print(f'CPU: {cpu_num} keyspace start at {key_count} and end at {key_end}')

    while KEY_NOT_FOUND.value and key_count <= key_end:
        if key_count == key:
            with KEY_NOT_FOUND.get_lock(): # låser variabeln så den inte kan ändras
                KEY_NOT_FOUND.value = False
            return (f'\nCPU: {cpu_num} found secret key at {key}\n')
        else:
            key_count += 1

def main():
    
    time_start = time.perf_counter() # startar en klocka för att hålla koll på tiden
    print(f'\nRandom secret key is: {key}')
    print(f'CPU process count is: {cpu_cores}\n')

    # Delar max numret för uint32 med antalet kärnor
    key_range = round(np.iinfo(np.uint32).max / cpu_cores)
    # skapar tomma listor vi kan använda
    cores = []
    start = []
    end = []

    # loop som körs från 0 till antalet cpu cores
    # lägger till i listorna
    for i in range(0, cpu_cores):
        cores.append( i + 1)
        start.append( i * key_range )
    # Lägger in sista numret i varje segment genom att ta nästa processors start nummer och 1
        end.append((i + 1 ) * key_range - 1)

    # Debugg för att kolla att värderna i listan är korrekt

    print(f'Start keyspace offset: {start}\nEnd keyspace offsets: {end}\n')

    key_not_found = mp.Value('i',True)
    # importera sprinner för frän effekt
    with Spinner():
        with cf.ProcessPoolExecutor(max_workers=cpu_cores, initializer=init_globals, initargs=(key_not_found,)) as executor:
            for result in executor.map(crack_key, cores, start, end):
                if result != None:
                    print(result)

    time_finish = time.perf_counter() # stannar tiden
    print(f'Finished in {round(time_finish - time_start, 2)} seconds\n')
    cpu_info()




# printar lite cpu info
def cpu_info():
    cpufreq = psu.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psu.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psu.cpu_percent()}%\n")
if __name__ == '__main__':
    main()