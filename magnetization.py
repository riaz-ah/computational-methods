
import numpy as np
import matplotlib.pyplot as plt
import time

from numba import jit


@jit(nopython=True)
def energy(system, i, j, L):
    """Energy function of spins connected to site (i, j)."""
    return -1. * system[i, j] * (system[np.mod(i - 1, L), j] + system[np.mod(i + 1, L), j] +
                                 system[i, np.mod(j - 1, L)] + system[i, np.mod(j + 1, L)])


@jit
def prepare_system(L):
    """Initialize the system."""
    system = 2 * (0.5 - np.random.randint(0, 2, size=(L, L)))
    return system


@jit(nopython=True)
def measure_energy(system):
    L = system.shape[0]
    E = 0
    for i in range(L):
        for j in range(L):
            E += energy(system, i, j, L) / 2.
    return E


@jit(nopython=True)
def measure_magnetization(system, L):
    """Calculate the magnetization."""
    return np.sum(system) / (L * L)


@jit(nopython=True)
def metropolis_loop(system, T, N_sweeps, N_eq, N_flips):
    """ Main loop doing the Metropolis algorithm."""
    E = measure_energy(system)
    L = system.shape[0]
    M_list = []
    E_list = []
    for step in range(N_sweeps + N_eq):
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)

        dE = -2. * energy(system, i, j, L)
        if dE <= 0.:
            system[i, j] *= -1
            E += dE

        elif np.exp(-1. / T * dE) > np.random.rand():
            system[i, j] *= -1
            E += dE

        # Measurement
        if step >= N_eq and np.mod(step, N_flips) == 0:
            M_list.append(measure_magnetization(system, L))
            E_list.append(E)

    return np.array(M_list)


if __name__ == "__main__":
    # Set parameters here
    L = 10  # Linear system size
    N_sweeps = 10000  # Number of steps for the measurements
    N_eq = 1000  # Number of equilibration steps before the measurements start
    N_flips = 10  # Number of steps between measurements
    N_bins = 10  # Number of bins use for the error analysis

    T_range = np.arange(1.5, 3.1, 0.1)

    Tc = 2. / np.log(1. + np.sqrt(2))
    system = prepare_system(L)
    magnetization_list=[]

    for T in T_range:
        magnetization_list_bin=[]
        for k in range(N_bins):
            Ms = metropolis_loop(system, T, N_sweeps, N_eq, N_flips)
            mean_Ms= np.mean(Ms)
            magnetization_list_bin.append(mean_Ms)
        magnetization_list.append([np.mean(magnetization_list_bin), np.std(magnetization_list_bin) / np.sqrt(N_bins)])
        print(T, mean_Ms, magnetization_list[-1])

    magnetization_list = np.array(magnetization_list)
    plt.errorbar(T_range, magnetization_list[:, 0], magnetization_list[:, 1])
    Tc = 2. / np.log(1. + np.sqrt(2))
    print(Tc)
    plt.axvline(Tc, color='r', linestyle='--')
    plt.xlabel('$T$')
    plt.ylabel('$M$')
    plt.show()



