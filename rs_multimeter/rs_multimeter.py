import serial

class Multimeter(serial.Serial):

    CommandChar = 'D\r\n';

    def __init__(self, port, timeout=0.5, convert_to_V=True):

        params = {
                'timeout': timeout,
                'baudrate': 600, 
                'bytesize': serial.SEVENBITS,
                'stopbits' : serial.STOPBITS_TWO, 
                }
        super().__init__(port,**params)
        self.setDTR(1)
        self.setRTS(0)
        while self.inWaiting() > 0:
            self.read()
        self.convert_to_V = convert_to_V 

    def get_reading(self):
        self.write(self.CommandChar.encode())
        line = self.readline()
        if len(line) == 15:
            line = line[1:]
        mode = str(line[:2].decode('utf-8'))
        unit = str(line[-3:-1].decode('utf-8')).strip()
        try:
            value = float(line[3:-3].decode('utf-8'))
            error = False
        except ValueError:
            value = 0.0
            error = True
        if self.convert_to_V and unit == 'mV':
            value = value/1.0e3
            unit = 'V'
        return value, mode, unit, error


