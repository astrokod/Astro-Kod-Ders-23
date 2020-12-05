# Astropy'dan Units'i içe aktarmak
from astropy import units

# Nümerik veri
r1 = 4

# units (kilometre) verisi
r2 = 4 * units.km
print(r2)
# r2'nin değeri
print(r2.value)
# r2'nin birimi
print(r2.unit)
# r2'nin temel birim,
print(r2.decompose())

# Çoklu unit verisi.
rs = [1, 2, 3] * units.km

print(rs)
print(rs.decompose())
