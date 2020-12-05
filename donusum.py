from astropy import units

# Hız birmi, km/saat
hiz = 5 * units.km / units.hour

# hiz'ı temel birimlerine dönüştürürsek, m/s olacaktır
print(hiz.decompose())
# hiz'ı mil/saat'e dönüştürmek
print(hiz.to(units.imperial.mile / units.hour))

# Sıcaklık verisi
T = 5500 * units.K
print(T)
# Sıcaklık verisi dönüştürmek için, equivalencies yani denklikler kullanılmalı
print(T.to(units.imperial.deg_F, equivalencies=units.temperature()))
