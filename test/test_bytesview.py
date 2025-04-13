
import unittest

from Xlib.protocol.display import bytesview


class BytesViewTest(unittest.TestCase):

    def test(self):
        with self.assertRaises(TypeError):
            bytesview('foobar')
        data = b'0123456789ABCDEF'
        view = bytesview(data)
        self.assertEqual(len(view), 16)
        self.assertEqual(view[:], data)
        self.assertIsInstance(view[:], bytes)
        self.assertEqual(view[5:-6], b'56789')
        self.assertEqual(view[7], ord('7'))
        view = bytesview(view, 5)
        self.assertEqual(view[:], b'56789ABCDEF')
        self.assertEqual(view[4], ord('9'))
        view = bytesview(view, 0, 5)
        self.assertEqual(view[:], b'56789')
        self.assertEqual(view[1], ord('6'))
