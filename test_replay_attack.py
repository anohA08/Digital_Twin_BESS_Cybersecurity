from replay_attack import ReplayAttack

attack = ReplayAttack(
    probability=1.0,
    replay_length=3
)

for i in range(10):
    value, active = attack.attack(i)
    print(i, value, active)