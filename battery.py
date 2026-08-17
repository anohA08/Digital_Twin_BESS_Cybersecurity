class Battery:

    def __init__(
        self,
        capacity: float,
        initial_soc: float,
        min_soc: float,
        max_soc: float,
        charge_efficiency: float,
        discharge_efficiency: float,
    ):
        # Validation checks
        if capacity <= 0:
            raise ValueError("Battery capacity must be positive.")

        if initial_soc < 0 or initial_soc > 100:
            raise ValueError("Initial SOC must be between 0 and 100.")

        if min_soc >= max_soc:
            raise ValueError("Minimum SOC must be smaller than Maximum SOC.")

        # Initialize attributes
        self.capacity = capacity
        self.energy = capacity * initial_soc / 100
        self.min_energy = capacity * min_soc / 100
        self.max_energy = capacity * max_soc / 100
        self.charge_efficiency = charge_efficiency
        self.discharge_efficiency = discharge_efficiency

    def get_soc(self) -> float:
        return (self.energy / self.capacity) * 100

    def charge(self, power: float, timestep: float):
        self.energy += power * self.charge_efficiency * timestep
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def discharge(self, power: float, timestep: float):
        self.energy -= (power / self.discharge_efficiency) * timestep
        if self.energy < self.min_energy:
            self.energy = self.min_energy