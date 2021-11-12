from Vehicle import Vehicle
from Bus import Bus
from Train import Train

if __name__ == '__main__':
    v = Vehicle("V1", "100", 4)
    v.info()

    b = Bus("V2", "100", 64, 140, [1, 2, 3])
    b.info()

    t = Train("V2", "100", 64, "Houston", [1, 2, 3], 5)
    t.info()
