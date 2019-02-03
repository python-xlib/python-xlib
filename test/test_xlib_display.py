#!/usr/bin/env python

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib.display
import Xlib.error
import Xlib.protocol.display
import Xlib.protocol.event
import Xlib.protocol.rq
import Xlib.xobject.fontable
import Xlib.X


class TestXlibDisplay(unittest.TestCase):
    def setUp(self):
        # Create authority file.
        self.display_num = os.getenv("DISPLAY")
        self.display = Xlib.display.Display(self.display_num)
        self.dummy_str = "qqq"
        self.keysym = 65535

    def test_display_instance(self):
        self.assertTrue(isinstance(self.display, Xlib.display.Display))

    def test_default_display_name(self):
        self.assertEqual(self.display.get_display_name(), self.display_num)

    def test_default_screen_number(self):
        self.assertEqual(self.display.get_default_screen(), 0)

    def test_returns_no_events(self):
        self.assertEqual(self.display.pending_events(), 0)

    def test_pointer_mapping_is_list(self):
        self.assertTrue(isinstance(self.display.get_pointer_mapping(), list))

    def test_set_get_pointer_mapping(self):
        orig_mapping = self.display.get_pointer_mapping()
        length = len(orig_mapping)
        try:
            self.display.set_pointer_mapping([0] * length)
            self.assertEqual(self.display.get_pointer_mapping(), [0] * length)
        finally:
            self.display.set_pointer_mapping(orig_mapping)

    def test_can_close_display(self):
        self.display.close()
        self.assertEqual(str(self.display.display.socket_error), "Display connection closed by client")

    def test_can_close_display_and_check_for_error(self):
        self.display.close()
        self.assertRaises(Xlib.error.ConnectionClosedError, self.display.flush)

    def test_return_fileno(self):
        self.assertTrue(isinstance(self.display.fileno(), int))

    def test_has_no_invalid_extension(self):
        self.assertTrue(~self.display.has_extension(self.dummy_str))

    def test_has_valid_extension(self):
        extensions = self.display.list_extensions()
        if extensions:
            self.assertTrue(~self.display.has_extension(extensions[0]))

    def test_can_create_resource_object(self):
        self.assertTrue(
            isinstance(self.display.create_resource_object("font", 0), Xlib.xobject.fontable.Font))

    def test_get_default_screen_instance(self):
        self.assertTrue(isinstance(self.display.screen(), Xlib.protocol.rq.DictWrapper))

    def test_get_zero_screen_instance(self):
        self.assertTrue(isinstance(self.display.screen(0), Xlib.protocol.rq.DictWrapper))

    def test_default_screen_count(self):
        self.assertEqual(self.display.screen_count(), 1)

    def test_cannot_add_existing_display_method(self):
        self.assertRaises(AssertionError, self.display.extension_add_method,
                          "display", "extension_add_method", lambda x: x)

    def test_cannot_add_existing_font_method(self):
        self.assertRaises(AssertionError, self.display.extension_add_method, "font", "__init__", lambda x: x)

    def test_can_add_extension_error(self):
        self.display.add_extension_error(1, Xlib.error.XError)
        self.assertEqual(self.display.display.error_classes[1], Xlib.error.XError)

    def test_keycode_to_keysym_for_invalid_index(self):
        self.assertEqual(self.display.keycode_to_keysym(0, 0), Xlib.X.NoSymbol)

    def test_keysym_to_keycode_for_nosymbol(self):
        self.assertEqual(self.display.keysym_to_keycode(Xlib.X.NoSymbol), 0)

    def test_keysym_to_keycode_for_valid_symbol(self):
        self.assertEqual(self.display.keysym_to_keycode(self.keysym), 119)

    def test_keysym_to_keycodes_for_nosymbol(self):
        self.assertEqual(self.display.keysym_to_keycodes(Xlib.X.NoSymbol), [])

    def test_refresh_keyboard_mapping_invalid_event(self):
        self.assertRaises(TypeError, self.display.refresh_keyboard_mapping, Xlib.protocol.event.AnyEvent)

    def test_get_modifier_mapping(self):
        self.assertEqual(len(self.display.get_modifier_mapping()), 8)

    def test_set_modifier_mapping(self):
        mapping = self.display.get_modifier_mapping()
        self.assertEqual(self.display.set_modifier_mapping(mapping), Xlib.X.MappingSuccess)

    def test_get_screensaver(self):
        self.assertTrue(isinstance(self.display.get_screen_saver(), Xlib.protocol.request.GetScreenSaver))

    def test_list_hosts(self):
        self.assertTrue(isinstance(self.display.list_hosts(), Xlib.protocol.request.ListHosts))

    def test_get_keyboard_control(self):
        self.assertTrue(
            isinstance(self.display.get_keyboard_control(), Xlib.protocol.request.GetKeyboardControl))

    def test_change_keyboard_mapping(self):
        kpt_mapping = self.display.get_keyboard_mapping(254, 1)
        self.display.change_keyboard_mapping(254, kpt_mapping)
        self.assertEqual(self.display.get_keyboard_mapping(254, 1), kpt_mapping)

    def test_get_font_path(self):
        self.assertNotEqual(self.display.get_font_path(), [])

    def test_get_atom_name(self):
        atom = self.display.get_atom(self.display_num)
        val = self.display.get_atom_name(atom)
        self.assertEqual(val, self.display_num)

    def test_intern_atom(self):
        atom = self.display.intern_atom(self.display_num)
        val = self.display.get_atom_name(atom)
        self.assertEqual(val, self.display_num)

    def test_get_input_focus(self):
        self.assertTrue(isinstance(self.display.get_input_focus(), Xlib.protocol.request.GetInputFocus))

    def test_query_keymap(self):
        self.assertTrue(isinstance(self.display.query_keymap(), list))

    def test_open_invalid_font(self):
        self.assertEqual(self.display.open_font(self.dummy_str), None)

    def test_list_fonts(self):
        fonts = self.display.list_fonts("*", 1)
        self.assertNotEqual(fonts, [])

    def test_lookup_valid_keysym(self):
        self.assertNotEqual(self.display.lookup_string(self.keysym), None)

    def test_lookup_invalid_keysym(self):
        self.assertEqual(self.display.lookup_string(-1), None)

    def test_rebind_string(self):
        self.display.rebind_string(self.keysym, self.dummy_str)
        self.assertEqual(self.display.lookup_string(self.keysym), self.dummy_str)

    def test_get_selection_owner(self):
        atom = self.display.get_atom(self.display_num)
        self.assertEqual(self.display.get_selection_owner(atom), 0)


if __name__ == '__main__':
    unittest.main()
