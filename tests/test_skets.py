#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_skets
----------------------------------

Tests for `skets` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from skets import skets
from skets import cli


class TestSkets(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'skets.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_echo_function(self):
        runner = CliRunner()
        sk = skets.Skets()
        result = runner.invoke(sk.echo("This is not a drill soldier"))
        assert "This is not a drill soldier\n" in result.output

if __name__ == '__main__':
    sys.exit(unittest.main())
