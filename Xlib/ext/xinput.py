# Xlib.ext.xinput -- XInput extension module
#
#    Copyright (C) 2012 Outpost Embedded, LLC
#      Forest Bond <forest.bond@rapidrollout.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

'''
A very incomplete implementation of the XInput extension.
'''

import sys, array

from Xlib.protocol import rq
from Xlib import X


extname = 'XInputExtension'

PropertyDeleted = 0
PropertyCreated = 1
PropertyModified = 2

NotifyNormal = 0
NotifyGrab = 1
NotifyUngrab = 2
NotifyWhileGrabbed = 3
NotifyPassiveGrab = 4
NotifyPassiveUngrab = 5

NotifyAncestor = 0
NotifyVirtual = 1
NotifyInferior = 2
NotifyNonlinear = 3
NotifyNonlinearVirtual = 4
NotifyPointer = 5
NotifyPointerRoot = 6
NotifyDetailNone = 7

GrabtypeButton = 0
GrabtypeKeycode = 1
GrabtypeEnter = 2
GrabtypeFocusIn = 3

AnyModifier = (1 << 31)
AnyButton = 0
AnyKeycode = 0

AsyncDevice = 0
SyncDevice = 1
ReplayDevice = 2
AsyncPairedDevice = 3
AsyncPair = 4
SyncPair = 5

SlaveSwitch = 1
DeviceChange = 2

MasterAdded = (1 << 0)
MasterRemoved = (1 << 1)
SlaveAdded = (1 << 2)
SlaveRemoved = (1 << 3)
SlaveAttached = (1 << 4)
SlaveDetached = (1 << 5)
DeviceEnabled = (1 << 6)
DeviceDisabled = (1 << 7)

AddMaster = 1
RemoveMaster = 2
AttachSlave = 3
DetachSlave = 4

AttachToMaster = 1
Floating = 2

ModeRelative = 0
ModeAbsolute = 1

MasterPointer = 1
MasterKeyboard = 2
SlavePointer = 3
SlaveKeyboard = 4
FloatingSlave = 5

KeyClass = 0
ButtonClass = 1
ValuatorClass = 2

KeyRepeat = (1 << 16)

AllDevices = 0
AllMasterDevices = 1

DeviceChanged = 1
KeyPress = 2
KeyRelease = 3
ButtonPress = 4
ButtonRelease = 5
Motion = 6
Enter = 7
Leave = 8
FocusIn = 9
FocusOut = 10
HierarchyChanged = 11
PropertyEvent = 12
RawKeyPress = 13
RawKeyRelease = 14
RawButtonPress = 15
RawButtonRelease = 16
RawMotion = 17

DeviceChangedMask = (1 << DeviceChanged)
KeyPressMask = (1 << KeyPress)
KeyReleaseMask = (1 << KeyRelease)
ButtonPressMask = (1 << ButtonPress)
ButtonReleaseMask = (1 << ButtonRelease)
MotionMask = (1 << Motion)
EnterMask = (1 << Enter)
LeaveMask = (1 << Leave)
FocusInMask = (1 << FocusIn)
FocusOutMask = (1 << FocusOut)
HierarchyChangedMask = (1 << HierarchyChanged)
PropertyEventMask = (1 << PropertyEvent)
RawKeyPressMask = (1 << RawKeyPress)
RawKeyReleaseMask = (1 << RawKeyRelease)
RawButtonPressMask = (1 << RawButtonPress)
RawButtonReleaseMask = (1 << RawButtonRelease)
RawMotionMask = (1 << RawMotion)

GrabModeSync = 0
GrabModeAsync = 1
GrabModeTouch = 2

DEVICEID = rq.Card16
DEVICE = rq.Card16
DEVICEUSE = rq.Card8


class XIQueryVersion(rq.ReplyRequest):
    _request = rq.Struct(
        rq.Card8('opcode'),
        rq.Opcode(47),
        rq.RequestLength(),
        rq.Card16('major_version'),
        rq.Card16('minor_version'),
        )
    _reply = rq.Struct(
        rq.ReplyCode(),
        rq.Pad(1),
        rq.Card16('sequence_number'),
        rq.ReplyLength(),
        rq.Card32('major_version'),
        rq.Card32('minor_version'),
        rq.Pad(16),
        )


def query_version(self):
    return XIQueryVersion(
        display=self.display,
        opcode=self.display.get_extension_major(extname),
        major_version=2,
        minor_version=0,
        )


EventMask = rq.Struct(
        DEVICE('deviceid'),
        rq.LengthOf('mask', 2),
        rq.List('mask', rq.Card32),
        )


class XISelectEvents(rq.Request):
    _request = rq.Struct(
        rq.Card8('opcode'),
        rq.Opcode(46),
        rq.RequestLength(),
        rq.Window('window'),
        rq.LengthOf('masks', 2),
        rq.Pad(2),
        rq.List('masks', EventMask),
        )

def pack_event_mask(deviceid, mask):
    mask_seq = array.array(rq.struct_to_array_codes['L'])

    if isinstance(mask, (int, long)):
        # We need to build a "binary mask" that (as far as I can tell) is
        # encoded in native byte order from end to end.  The simple case is
        # with a single unsigned 32-bit value, for which we construct an
        # array with just one item.  For values too big to fit inside 4
        # bytes we build a longer array, being careful to maintain native
        # byte order across the entire set of values.
        if sys.byteorder == 'little':
            f = lambda v: mask_seq.insert(0, v)
        elif sys.byteorder == 'big':
            f = mask_seq.append
        else:
            raise AssertionError(sys.byteorder)
        while mask:
            f(mask & 0xFFFFFFFF)
            mask = mask >> 32
    else:
        mask_seq.extend(mask)

    return {'deviceid': deviceid, 'mask': mask_seq}

def select_events(self, event_masks):
    '''
    select_events(event_masks)

    event_masks:
      Sequence of (deviceid, mask) pairs, where deviceid is a numerical device
      ID, or AllDevices or AllMasterDevices, and mask is either an unsigned
      integer or sequence of 32 byte unsigned values
    '''

    masks = [pack_event_mask(deviceid, mask) for deviceid, mask in event_masks]
    return XISelectEvents(
        display=self.display,
        opcode=self.display.get_extension_major(extname),
        window=self,
        masks=masks,
        )

class XIGrabDevice(rq.ReplyRequest):
    _request = rq.Struct(
        rq.Card8('opcode'),
        rq.Opcode(51),
        rq.RequestLength(),
        rq.Window('grab_window'),
        rq.Card32('time'),
        rq.Cursor('cursor', (X.NONE, )),
        DEVICEID('deviceid'),
        rq.Set('grab_mode', 1, (GrabModeSync, GrabModeAsync)),
        rq.Set('paired_device_mode', 1, (GrabModeSync, GrabModeAsync)),
        rq.Bool('owner_events'),
        rq.Pad(1),
        rq.LengthOf('mask', 2),
        rq.List('mask', rq.Card32),
    )

    _reply = rq.Struct(
        rq.ReplyCode(),
        rq.Pad(1),
        rq.Card16('sequence_number'),
        rq.ReplyLength(),
        rq.Card8('status'),
        rq.Pad(23),
        )

def grab_device(self, deviceid, time, grab_mode, paired_device_mode, owner_events, event_mask):
    mask = pack_event_mask(deviceid, event_mask)
    return XIGrabDevice(
        display=self.display,
        opcode=self.display.get_extension_major(extname),
        deviceid=deviceid,
        grab_window=self,
        time=time,
        cursor=X.NONE,
        grab_mode=grab_mode,
        paired_device_mode=paired_device_mode,
        owner_events=owner_events,
        mask=mask['mask'],
        )

class XIUngrabDevice(rq.Request):
    _request = rq.Struct(
        rq.Card8('opcode'),
        rq.Opcode(52),
        rq.RequestLength(),
        rq.Card32('time'),
        DEVICEID('deviceid'),
        rq.Pad(2),
    )

def ungrab_device(self, deviceid, time):
    return XIUngrabDevice(
        display=self.display,
        opcode=self.display.get_extension_major(extname),
        time=time,
        deviceid=deviceid,
    )

HierarchyInfo = rq.Struct(
        DEVICEID('deviceid'),
        DEVICEID('attachment'),
        DEVICEUSE('type'),
        rq.Bool('enabled'),
        rq.Pad(2),
        rq.Card32('flags'),
        )


HierarchyEventData = rq.Struct(
        DEVICEID('deviceid'),
        rq.Card32('time'),
        rq.Card32('flags'),
        rq.LengthOf('info', 2),
        rq.Pad(10),
        rq.List('info', HierarchyInfo),
        )

ModifierInfo = rq.Struct(
    rq.Card32('base_mods'),
    rq.Card32('latched_mods'),
    rq.Card32('locked_mods'),
    rq.Card32('effective_mods'),
)

GroupInfo = rq.Struct(
    rq.Card8('base_group'),
    rq.Card8('latched_group'),
    rq.Card8('locked_group'),
    rq.Card8('effective_group'),
)

class FP1616(rq.Int32):

    def check_value(self, value):
        return int(value * 65536.0)

    def parse_value(self, value, display):
        return float(value) / float(1 << 16)

DeviceEventData = rq.Struct(
    DEVICEID('deviceid'),
    rq.Card32('time'),
    rq.Card32('detail'),
    rq.Window('root'),
    rq.Window('event'),
    rq.Window('child'),
    FP1616('root_x'),
    FP1616('root_y'),
    FP1616('event_x'),
    FP1616('event_y'),
    rq.Card16('buttons_len'),
    rq.Card16('valulators_len'),
    DEVICEID('sourceid'),
    rq.Pad(2),
    rq.Card32('flags'),
    rq.Object('mods', ModifierInfo),
    rq.Object('groups', GroupInfo),
)


def init(disp, info):
    disp.extension_add_method('display', 'xinput_query_version', query_version)
    disp.extension_add_method('window', 'xinput_select_events', select_events)
    disp.extension_add_method('window', 'xinput_grab_device', grab_device)
    disp.extension_add_method('display', 'xinput_ungrab_device', ungrab_device)

    disp.ge_add_event_data(info.major_opcode, KeyPress, DeviceEventData)
    disp.ge_add_event_data(info.major_opcode, KeyRelease, DeviceEventData)
    disp.ge_add_event_data(info.major_opcode, HierarchyChanged, HierarchyEventData)
