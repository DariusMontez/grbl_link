=========
Grbl Link
=========


.. image:: https://img.shields.io/pypi/v/grbl_link.svg
        :target: https://pypi.python.org/pypi/grbl_link

.. image:: https://img.shields.io/travis/DariusMontez/grbl_link.svg
        :target: https://travis-ci.org/DariusMontez/grbl_link

.. image:: https://readthedocs.org/projects/grbl-link/badge/?version=latest
        :target: https://grbl-link.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/DariusMontez/grbl_link/shield.svg
     :target: https://pyup.io/repos/github/DariusMontez/grbl_link/
     :alt: Updates



Interact seamlessly with a Grbl CNC controller. Stream files, jog, and receive status messages from a connected Grbl device.

* Documentation: https://grbl-link.readthedocs.io.

Quick Start
-----------

Install with pip: 

.. code-block:: sh

  pip install grbl_link

Plug in the Grbl device to a USB port.


.. code-block:: python

  import serial
  conn = serial.Serial(port='/dev/ttyACM0', baudrate=115200)


Create a Grbl instance.

.. code-block:: python

  from grbl_link.interface import Grbl
  grbl = Grbl(conn)


Add a message handler to get feedback from Grbl.

.. code-block:: python

  def message_handler(message, grbl):
    print("From Grbl:", message)

  grbl.add_message_handler(message_handler)


You may also turn on debug mode in the constructor to see realtime activity.

.. code-block:: python

  grbl = Grbl(conn, debug=True)


Start the Grbl main loop. It runs in the background as a thread,
listening for messages from the connected Grbl device.

.. code-block:: python

  grbl.start()


Send G-Code commands to Grbl

.. code-block:: python

  grbl.send("G21")
  grbl.send("G0 X30")


Realtime commands are sent immediately. All other commands are queued
and executed in order as Grbl completes them.

Get status information from Grbl.

.. code-block:: python

  print(grbl.version)
  print(grbl.status)
  print(grbl.alarm_state)
  print(grbl.check)
  print(grbl.sleeping)


Features
--------

* Send GCODE and Grbl-specific commands
* Built-in jog API
* Receive push messages sent from Grbl
* Free software: MIT license

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
