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
def metropolis_loop(system, T, N_sweeps, N_eq, N_flips):
    """ Main loop doing the Metropolis algorithm."""
    E = measure_energy(system)
    L = system.shape[0]
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

        if step >= N_eq and np.mod(step, N_flips) == 0:
            # measurement
            E_list.append(E)
    return np.array(E_list)


if __name__ == "__main__":
    """ Scan through some temperatures """
    # Set parameters here
    L_values = [10, 20, 30]  # Different system sizes
    N_sweeps = 10000  # Number of steps for the measurements
    N_eq = 1000  # Number of equilibration steps before the measurements start
    N_flips = 10  # Number of steps between measurements
    N_bins = 10  # Number of bins use for the error analysis

    T_range = np.arange(1.5, 3.1, 0.1)

    for L in L_values:
        C_list = []
        system = prepare_system(L)
        for T in T_range:
            C_list_bin = []
            for k in range(N_bins):
                Es = metropolis_loop(system, T, N_sweeps, N_eq, N_flips)

                mean_E = np.mean(Es)
                mean_E2 = np.mean(Es**2)

                C_list_bin.append(1. / T**2. / L**2. * (mean_E2 - mean_E**2))
            C_list.append([np.mean(C_list_bin), np.std(C_list_bin) / np.sqrt(N_bins)])

            print("L:", L, "T:", T, "mean_E:", mean_E, "C_V:", C_list[-1])

        # Plot the results
        C_list = np.array(C_list)
        plt.errorbar(T_range, C_list[:, 0], C_list[:, 1], label=f'L={L}')

    Tc = 2. / np.log(1. + np.sqrt(2))
    print("Critical Temperature (analytical):", Tc)
    plt.axvline(Tc, color='r', linestyle='--', label='Critical Temperature')
    plt.xlabel('$T$')
    plt.ylabel('$C_V$')
    plt.legend()
    plt.show()

    import numpy as np
    # import matplotlib.pyplot as plt
    # import matplotlib.patches as patches
    #
    # points = 10000
    # rand = np.random.uniform(-1, 1, 2 * points)
    # rand_points = rand.reshape(points, 2)
    # norm_points = rand_points[:, 0] ** 2 + rand_points[:, 1] ** 2
    # points_inside = rand_points[norm_points < 1]
    # points_outside = rand_points[norm_points > 1]
    # pi_approx = 4 * len(points_inside) / points
    # print(pi_approx)
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111, aspect='equal')
    # rectangle = patches.Rectangle((-1, -1), 2, 2, facecolor='none', edgecolor='black')
    # circle = patches.Circle((0, 0), 1, facecolor='none', edgecolor='black')
    # ax.add_patch(rectangle)
    # ax.add_patch(circle)
    # plt.xlim([-2, 2])
    # plt.ylim([-2, 2])
    # plt.scatter(points_inside[:, 0], points_inside[:, 1], color='green', s=0.05)
    # plt.scatter(points_outside[:, 0], points_outside[:, 1], color='red', s=0.05)
    #
    # plt.show()
    #
    # def variance():
    #     arr = []
    #
    #     for i in range(100):
    #         points_inside = rand_points[norm_points < 1]
    #         points_outside = rand_points[norm_points > 1]
    #         pi_approx = 4 * len(points_inside) / points
    #         error_square = (pi_approx - np.pi) ** 2
    #         arr.append(error_square)
    #     var = np.mean(arr)
    #     print(var)
    #
    # variance()
    #
