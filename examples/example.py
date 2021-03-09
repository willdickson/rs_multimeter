import rs_multimeter

port = '/dev/ttyUSB0'

dev = rs_multimeter.Multimeter(port)

while True:
    value, mode, unit, error = dev.get_reading()
    if not error:
        print(f'{value:0.3f}{unit}, mode = {mode}')
    else:
        print(error)

