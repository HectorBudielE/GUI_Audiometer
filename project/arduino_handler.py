import serial
import serial.tools.list_ports

def initiate_arduino_port():
    arduino_ports=[p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description]
    ser=serial.Serial(port=arduino_ports[0])
    ser.close()
    ser.open()
