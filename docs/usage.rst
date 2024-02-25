=====
Usage
=====

To use Grbl Link in a project::

    from grbl_link import Grbl
    from serial import Serial

    # connect a Grbl (version 1+) device
    conn = Serial("/dev/ttyUSB0", baudrate=115200)

    
    grbl = Grbl(conn)

    # at this point, a background thread is spun off and communication with
    # the device is open

    # add a message handler

    def my_handler(message, grbl):
        print(message)

    grbl.protocol.add_message_handler(my_handler)

    # send commands

    grbl.send("G90 G20 G0 X1.25")
