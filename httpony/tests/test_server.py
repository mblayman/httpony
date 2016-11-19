import unittest

import mock

from httpony import server


class TestServer(unittest.TestCase):

    @mock.patch('httpony.server.run_simple')
    def test_runs(self, run_simple):
        server.main()
        self.assertTrue(run_simple.called)
