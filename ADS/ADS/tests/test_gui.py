import unittest
import platform


class TestGui(unittest.TestCase):
    # I don't know that this class should exist. GUI test?
    def test_windows(self):
        if platform.system() == 'Windows':
            from ADS.ADS.gui.windows_gui import WindowsGui
            WindowsGui().run()

    def test_linux(self):
        if platform.system() == 'Linux':
            return

    def test_apple(self):
        if platform.system() == 'Darwin':
            return

    def test_java(self):
        if platform.system() == 'Java':
            return

    def test_other(self):
        if platform.system() == '':
            return

