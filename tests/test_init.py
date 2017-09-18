from unittest import TestCase
import stashy
import os
import re


class TestStashInit(TestCase):
    def test_stashy_version(self):
        """
        Ensure setup.py version matches code
        """
        # Setup
        setup_path = os.path.join(
            os.path.dirname(os.path.dirname(stashy.__file__)),
            'setup.py'
        )
        regex = re.compile('version="([^"]+)"')
        with open(setup_path) as fobj:
            for line in fobj:
                mobj = regex.search(line)
                if mobj:
                    expected = mobj.group(1)
        # Exercise

        observed = stashy.__version__
        # Verify
        self.assertEqual(expected, observed)
