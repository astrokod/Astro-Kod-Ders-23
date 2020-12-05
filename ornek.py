from astropy import units
from astropy import constants


# wien Yasası
def wien1(T):
    # b değerini tanılma
    b = 2.897771955 * 10 ** -3 * units.m * units.K
    # Gelen sıcaklık (Kelvin) değeri ile maksimum dalgaboyunu hesapla
    return b / T


# wien Yasası
def wien2(T):
    # b değerini tanılma
    b = 2.897771955 * 10 ** -3 * units.m * units.K
    # Gelen sıcaklık (Herhangi. Sıcaklık değeri Kelvin'e dönüştürülmekte) değeri ile maksimum dalgaboyunu hesapla
    return b / T.to(units.K, equivalencies=units.temperature())


def wien3(T):
    # b değerini constants alt paketinden al ve gelen sıcaklık (Herhangi. Sıcaklık değeri Kelvin'e dönüştürülmekte)
    # değeri ile maksimum dalgaboyunu hesapla
    return constants.b_wien / T.to(units.K, equivalencies=units.temperature())


if __name__ == '__main__':
    print(wien2(5300 * units.K).to(units.nm))
    print(wien3(5300 * units.K).to(units.nm))
    print(wien3([5500, 10000, 15000] * units.K).to(units.nm))
