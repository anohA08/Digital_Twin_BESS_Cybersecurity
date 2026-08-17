
import config

from battery import Battery
from utils import load_data
from simulation import Simulation
from logger import logger
from digital_twin import DigitalTwin

from plots import (
    plot_soc,
    plot_energy,
    plot_solar_demand,
    plot_battery_power,
    plot_sync_error,
    plot_attack,
)


# ------------------------------------
# Create Battery
# ------------------------------------

# Physical battery
physical_battery = Battery(
    capacity=config.BATTERY_CAPACITY,
    initial_soc=config.INITIAL_SOC,
    min_soc=config.MIN_SOC,
    max_soc=config.MAX_SOC,
    charge_efficiency=config.CHARGE_EFFICIENCY,
    discharge_efficiency=config.DISCHARGE_EFFICIENCY
)

twin_battery = Battery(
    capacity=config.BATTERY_CAPACITY,
    initial_soc=config.INITIAL_SOC,
    min_soc=config.MIN_SOC,
    max_soc=config.MAX_SOC,
    charge_efficiency=config.CHARGE_EFFICIENCY,
    discharge_efficiency=config.DISCHARGE_EFFICIENCY
)

digital_twin = DigitalTwin(twin_battery)

# ------------------------------------
# Load Dataset
# ------------------------------------

data = load_data("Bess_data.csv")

# ------------------------------------
# Run Simulation
# ------------------------------------

simulation = Simulation(physical_battery,digital_twin, data)

results = simulation.run()
print()
print(results.describe())

maximum_soc = results["SOC"].max()
minimum_soc = results["SOC"].min()

print()
print("Maximum SOC:", maximum_soc)
print("Minimum SOC:", minimum_soc)

maximum_energy = results["Energy"].max()

minimum_energy = results["Energy"].min()

print()

print("Maximum Energy:", maximum_energy)

print("Minimum Energy:", minimum_energy)

print()

print("Detector Statistics")

print(simulation.detector.statistics())

# ------------------------------------
# Save Results
# ------------------------------------
with open(
    "results/validation_report.txt",
    "w"
) as file:

    file.write("BESS Validation Report\n")

    file.write("----------------------\n")

    file.write(
        f"Maximum SOC : {maximum_soc:.2f}\n"
    )

    file.write(
        f"Minimum SOC : {minimum_soc:.2f}\n"
    )

    file.write(
        f"Maximum Energy : {maximum_energy:.2f}\n"
    )

    file.write(
        f"Minimum Energy : {minimum_energy:.2f}\n"
    )
results.to_csv(
    "results/simulation_results.csv",
    index=False
)

# ------------------------------------
# Show Results
# ------------------------------------

print(results)

# ------------------------------------
# Create Graphs
# ------------------------------------

plot_soc(results)

plot_energy(results)

plot_solar_demand(results)

plot_battery_power(results)

plot_sync_error(results)

plot_attack(results)

logger.info(
    "Simulation completed successfully."
)
# Programmatic Graph Validation Check
print("SOC Valid:", (results["SOC"].min() >= 20) and (results["SOC"].max() <= 100))
print("Energy Valid:", (results["Energy"].min() >= 0) and (results["Energy"].max() <= config.BATTERY_CAPACITY))





from plots import (
    plot_soc,
    plot_energy,
    plot_solar_demand,
    plot_battery_power,
    plot_sync_error
)
plot_sync_error(results)