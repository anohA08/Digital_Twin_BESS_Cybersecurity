class AttackDetector:

    def __init__(self, threshold=15):
        """
        threshold:
            Maximum allowed SOC change (%) in one simulation step.
        """

        self.threshold = threshold
        self.previous_soc = None

        self.attack_detected = False

        self.total_measurements = 0
        self.total_detections = 0

    def detect(self, measured_soc):

        self.total_measurements += 1

        # First measurement
        if self.previous_soc is None:
            self.previous_soc = measured_soc
            self.attack_detected = False
            return measured_soc

        change = abs(measured_soc - self.previous_soc)

        if change > self.threshold:

            self.attack_detected = True
            self.total_detections += 1

        else:

            self.attack_detected = False
            self.previous_soc = measured_soc

        return measured_soc

    def statistics(self):

        return {

            "Measurements": self.total_measurements,

            "Detections": self.total_detections

        }