import numpy as np
from scipy.constants import Boltzmann

def init(temperature, mass):
    return (np.random.rand(3) - 0.5) * np.sqrt(Boltzmann * temperature / (mass * 1.602e-19))


def update(DT, velocty, accelaretion: list):
    ''' Verlet velocity algorithm: mean is applied to acceleration to compensate discretized error '''
    return velocty + np.mean(accelaretion, axis=0)*DT

# Il codice importa il modulo NumPy come np e la costante di Boltzmann dal modulo scipy.constants. La funzione init() riceve la temperatura e la massa come parametri e restituisce una velocità casuale iniziale per una particella utilizzando la distribuzione di Maxwell-Boltzmann. La funzione update() riceve il passo di tempo DT, la velocità corrente e l'accelerazione corrente come parametri e restituisce la nuova velocità utilizzando l'algoritmo di Verlet. L'algoritmo di Verlet è un algoritmo di integrazione numerica utilizzato per risolvere le equazioni del moto di un sistema di particelle. La funzione update() utilizza l'algoritmo di Verlet per aggiornare la velocità della particella in base alla sua accelerazione e al passo di tempo.
#La funzione np.random.rand(3) genera un array di tre numeri casuali compresi tra 0 e 1. Sottraendo 0,5 all'array, si ottiene un array di numeri casuali compresi tra -0,5 e 0,5. Moltiplicando l'array per la radice quadrata di Boltzmann * temperature / (mass * 1.602e-19), si ottiene una velocità casuale iniziale per una particella utilizzando la distribuzione di Maxwell-Boltzmann.
#La funzione np.mean(acceleration, axis=0) calcola la media delle accelerazioni lungo l'asse 0 dell'array acceleration. La funzione update() utilizza la media delle accelerazioni per calcolare la nuova velocità della particella utilizzando l'algoritmo di Verlet.