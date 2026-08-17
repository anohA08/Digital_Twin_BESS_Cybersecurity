from detector import AttackDetector

detector = AttackDetector(threshold=15)

values = [

    50,
    51,
    52,
    53,
    54,
    80,
    81,
    55,
    56,
]

for soc in values:

    detector.detect(soc)

    print(
        soc,
        detector.attack_detected
    )

print()

print(detector.statistics())