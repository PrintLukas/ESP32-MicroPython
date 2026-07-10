import time

class BMP180:
    def __init__(self, i2c, addr=0x77):
        self.i2c = i2c
        self.addr = addr
        self.oversample_sett = 3
        self._load_calibration()

    def _read_signed(self, reg):
        d = self.i2c.readfrom_mem(self.addr, reg, 2)
        val = (d[0] << 8) | d[1]
        return val - 65536 if val > 32767 else val

    def _read_unsigned(self, reg):
        d = self.i2c.readfrom_mem(self.addr, reg, 2)
        return (d[0] << 8) | d[1]

    def _load_calibration(self):
        self.AC1 = self._read_signed(0xAA)
        self.AC2 = self._read_signed(0xAC)
        self.AC3 = self._read_signed(0xAE)
        self.AC4 = self._read_unsigned(0xB0)
        self.AC5 = self._read_unsigned(0xB2)
        self.AC6 = self._read_unsigned(0xB4)
        self.B1 = self._read_signed(0xB6)
        self.B2 = self._read_signed(0xB8)
        self.MB = self._read_signed(0xBA)
        self.MC = self._read_signed(0xBC)
        self.MD = self._read_signed(0xBE)

    def _read_raw_temp(self):
        self.i2c.writeto_mem(self.addr, 0xF4, b'\x2E')
        time.sleep_ms(5)
        d = self.i2c.readfrom_mem(self.addr, 0xF6, 2)
        return (d[0] << 8) | d[1]

    def _read_raw_pressure(self):
        self.i2c.writeto_mem(self.addr, 0xF4, bytes([0x34 + (self.oversample_sett << 6)]))
        time.sleep_ms(2 + (3 << self.oversample_sett))
        d = self.i2c.readfrom_mem(self.addr, 0xF6, 3)
        return ((d[0] << 16) + (d[1] << 8) + d[2]) >> (8 - self.oversample_sett)

    def _get_B5(self, UT):
        X1 = ((UT - self.AC6) * self.AC5) >> 15
        X2 = (self.MC << 11) // (X1 + self.MD)
        return X1 + X2

    @property
    def temperature(self):
        B5 = self._get_B5(self._read_raw_temp())
        return ((B5 + 8) >> 4) / 10

    @property
    def pressure(self):
        UT = self._read_raw_temp()
        UP = self._read_raw_pressure()
        B5 = self._get_B5(UT)
        B6 = B5 - 4000
        X1 = (self.B2 * (B6 * B6 >> 12)) >> 11
        X2 = (self.AC2 * B6) >> 11
        X3 = X1 + X2
        B3 = (((self.AC1 * 4 + X3) << self.oversample_sett) + 2) >> 2
        X1 = (self.AC3 * B6) >> 13
        X2 = (self.B1 * (B6 * B6 >> 12)) >> 16
        X3 = ((X1 + X2) + 2) >> 2
        B4 = (self.AC4 * (X3 + 32768)) >> 15
        B7 = (UP - B3) * (50000 >> self.oversample_sett)
        p = (B7 * 2) // B4 if B7 < 0x80000000 else (B7 // B4) * 2
        X1 = (p >> 8) * (p >> 8)
        X1 = (X1 * 3038) >> 16
        X2 = (-7357 * p) >> 16
        return p + ((X1 + X2 + 3791) >> 4)