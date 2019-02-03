#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the Grbl interface module"""

import pytest
from unittest.mock import MagicMock

from grbl_link.interface import Grbl

@pytest.fixture
def grbl():

    serial = MagicMock()
    serial.in_waiting = 0

    return Grbl(serial, debug=True)

def test_send_realtime(grbl):
    grbl.send(b'!')

    assert grbl.protocol.serial.write.called

