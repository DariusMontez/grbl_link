#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the Grbl message parser module"""

import pytest

from grbl_link.parser import parse_line
from grbl_link.messages import *

def test_parse_welcome_message():
    message = parse_line("Grbl 1.1e ['$' for help]")

    assert isinstance(message, WelcomeMessage)
    assert message.version == "1.1e"

def test_parse_alarm_message():
    message = parse_line("ALARM:x")

    assert isinstance(message, AlarmMessage)
    assert message.alarm_state == "x"

def test_parse_settings_message():
    message = parse_line("$1=200.0")

    assert isinstance(message, SettingsMessage)
    assert message.setting_name == "1"
    assert message.setting_value == "200.0"

def test_parse_ok_message():
    message = parse_line("ok")

    assert isinstance(message, OKMessage)
    
def test_parse_error_message():
    message = parse_line("error:9")

    assert isinstance(message, ErrorMessage)
    assert message.error_number == "9"  # TODO: convert to int

def test_parse_feedback_message():
    message = parse_line("[MSG:Door open]")

    assert isinstance(message, FeedbackMessage)
    assert message.feedback == "Door open"

def test_parse_status_message():
    message = parse_line("<Idle|MPos:10,20,30|WCO:1.2,3.4,5.6>")

    assert isinstance(message, StatusMessage)
    assert message.status['mode'] == 'Idle'
    assert message.status['MPos'] == [10, 20, 30]
    assert message.status['WCO'] == [1.2, 3.4, 5.6]

def test_parse_startup_block_message__VALID():
    message = parse_line(">G91G20:ok")

    assert isinstance(message, StartupBlockMessage)
    assert message.startup_block == "G91G20"
    assert message.is_valid

def test_parse_startup_block_message__INVALID():
    message = parse_line(">G91G20:error")

    assert isinstance(message, StartupBlockMessage)
    assert message.startup_block == "G91G20"
    assert message.is_valid == False

