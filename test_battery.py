from battery import Battery


def test_soc():

    battery = Battery(

        capacity=100,

        initial_soc=50,

        min_soc=20,

        max_soc=100,

        charge_efficiency=0.95,

        discharge_efficiency=0.95

    )

    assert battery.get_soc() == 50