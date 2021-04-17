#!/usr/bin/python
#
# examples/xres.py -- demonstrate the X-Resource extension
#
#    Copyright (C) 2021 Aleksei Bavshin <alebastr89@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    51 Franklin Street,
#    Fifth Floor,
#    Boston, MA 02110-1301 USA

import os
import sys

# Change path so we find Xlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from Xlib.display import Display
from Xlib.ext import res as XRes


def check_ext(disp, extname, version):
    if disp.query_extension(extname) is None:
        raise AssertionError("Server has {} extension".format(extname))

    r = disp.res_query_version()
    if (r.server_major, r.server_minor) < version:
        raise AssertionError(
            "Server has requested version {} of {} extension".format(version, extname)
        )


def query_client_id(display, wid):
    specs = [{"client": wid, "mask": XRes.LocalClientPIDMask}]
    r = display.res_query_client_ids(specs)
    for id in r.ids:
        if id.spec.client > 0 and id.spec.mask == XRes.LocalClientPIDMask:
            for value in id.value:
                return value
    return None


def print_client_info(disp, client):
    print("client: {}".format(client))

    resources = disp.res_query_client_resources(client)
    rc = [r.count for r in resources.types]
    print("\tresouces: {} resources of {} types".format(sum(rc), len(rc)))

    pb = disp.res_query_client_pixmap_bytes(client)
    print("\tpixmaps: {} bytes {} overflow".format(pb.bytes, pb.bytes_overflow))

    pid = query_client_id(disp, client)
    print("\tpid: {}".format(pid))

    rb = disp.res_query_resource_bytes(client, [{"resource": 0, "type": 0}])
    sizes = [s.size.bytes for s in rb.sizes]
    print("\t{} resources consume {} bytes".format(len(sizes), sum(sizes)))


def main():
    display = Display()
    check_ext(display, XRes.extname, (1, 2))

    clients = display.res_query_clients().clients
    print("{} clients connected to the server".format(len(clients)))

    for client in clients:
        print_client_info(display, client.resource_base)


if __name__ == "__main__":
    main()
