from battery import Battery


class DigitalTwin:
    """
    Digital Twin of a Battery Energy Storage System.
    """

    def __init__(self, battery: Battery):

        self.battery = battery
        self.last_error = 0.0
        self.error_history = []

    def update(self, measured_soc):
        """
        Update the Digital Twin using the measured SOC.
        """

        self.battery.energy = (
        measured_soc / 100
    ) * self.battery.capacity

    def calculate_error(self, physical_battery: Battery) -> float:
        """
        Calculate SOC synchronization error.
        """

        physical_soc = physical_battery.get_soc()
        twin_soc = self.battery.get_soc()

        soc_error = abs(physical_soc - twin_soc)

        self.last_error = soc_error
        self.error_history.append(soc_error)

        return soc_error

    def is_synchronized(self, threshold: float = 1.0) -> bool:
        """
        Check whether the Digital Twin is synchronized.
        """

        return self.last_error <= threshold

    def get_current_soc(self) -> float:
        return self.battery.get_soc()

    def get_error_history(self):
        return self.error_history

    def reset(self) -> None:
        self.error_history.clear()
        self.last_error = 0