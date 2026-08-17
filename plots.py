import matplotlib.pyplot as plt


def plot_soc(results):
    """
    Plot Battery State of Charge (SOC) over time.
    """

    plt.figure(figsize=(10,5))

    plt.plot(
        results["Hour"],
        results["SOC"],
        marker="o",
        linewidth=2
    )

    plt.title("Battery State of Charge")

    plt.xlabel("Hour")

    plt.ylabel("SOC (%)")

    plt.grid(True)

    plt.savefig("results/soc_plot.png", dpi=300)

    plt.show()


def plot_energy(results):
    """
    Plot stored battery energy.
    """

    plt.figure(figsize=(10,5))

    plt.plot(
        results["Hour"],
        results["Energy"],
        marker="s",
        linewidth=2
    )

    plt.title("Battery Energy")

    plt.xlabel("Hour")

    plt.ylabel("Energy (kWh)")

    plt.grid(True)

    plt.savefig("results/energy_plot.png", dpi=300)

    plt.show()


def plot_solar_demand(results):
    """
    Plot solar generation and load demand.
    """

    plt.figure(figsize=(10,5))

    plt.plot(
        results["Hour"],
        results["Solar"],
        marker="o",
        label="Solar"
    )

    plt.plot(
        results["Hour"],
        results["Demand"],
        marker="s",
        label="Demand"
    )

    plt.title("Solar Generation vs Load Demand")

    plt.xlabel("Hour")

    plt.ylabel("Power (kW)")

    plt.legend()

    plt.grid(True)

    plt.savefig("results/solar_demand.png", dpi=300)

    plt.show()


def plot_battery_power(results):
    """
    Plot charging/discharging power.
    """

    plt.figure(figsize=(10,5))

    plt.bar(
        results["Hour"],
        results["Battery Power"]
    )

    plt.title("Battery Power")

    plt.xlabel("Hour")

    plt.ylabel("Power (kW)")

    plt.grid(True)

    plt.savefig("results/battery_power.png", dpi=300)

    plt.show()

def plot_sync_error(results):
    """
    Plot Digital Twin synchronization error over time.
    """
    
    plt.figure(figsize=(10, 5))

    plt.plot(
        results["Hour"],
        results["Sync_Error"],
        marker="o",
        linewidth=2
    )

    plt.title("Digital Twin Synchronization Error")

    plt.xlabel("Hour")

    plt.ylabel("SOC Error (%)")

    plt.grid(True)

    plt.savefig(
        "results/sync_error.png",
        dpi=300
    )

    plt.show()
    
def plot_attack(results):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,5))

    colors = ["red" if x else "blue" for x in results["Attack"]]

    plt.scatter(
        results["Hour"],
        results["Sync_Error"],
        c=colors
    )

    plt.xlabel("Hour")
    plt.ylabel("Synchronization Error (%)")
    plt.title("Synchronization Error During Sensor Spoofing Attack")

    plt.grid(True)

    plt.savefig(
        "results/attack_plot.png",
        dpi=300
    )

    plt.show()