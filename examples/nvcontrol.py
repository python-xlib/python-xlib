#!/usr/bin/python
#
# examples/nvcontrol.py -- demonstrate the NV-CONTROL extension
#
#    Copyright (C) 2019 Roberto Leinardi <roberto@leinardi.com>
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
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA


# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os

# Change path so we find Xlib
from pprint import pprint

from Xlib.display import Display
from Xlib.ext.nvcontrol import Gpu, Cooler

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':
    display = Display()
    # Check for extension
    if not display.has_extension('NV-CONTROL'):
        sys.stderr.write('{}: server does not have the NV-CONTROL extension\n'.format(sys.argv[0]))
        ext = display.query_extension('NV-CONTROL')
        print(ext)
        sys.stderr.write("\n".join(display.list_extensions()))
        if ext is None:
            sys.exit(1)

    gpu = Gpu(0)
    fan = Cooler(0)

    perf_level = 3

    dic = {
        'get_gpu_count': display.nvcontrol_get_gpu_count(),
        'get_vram': display.nvcontrol_get_vram(gpu),
        'get_irq': display.nvcontrol_get_irq(gpu),
        'supports_framelock': display.nvcontrol_supports_framelock(gpu),
        'get_core_temp': display.nvcontrol_get_core_temp(gpu),
        'get_core_threshold': display.nvcontrol_get_core_threshold(gpu),
        'get_default_core_threshold': display.nvcontrol_get_default_core_threshold(gpu),
        'get_max_core_threshold': display.nvcontrol_get_max_core_threshold(gpu),
        'get_ambient_temp': display.nvcontrol_get_ambient_temp(gpu),
        'get_cuda_cores': display.nvcontrol_get_cuda_cores(gpu),
        'get_memory_bus_width': display.nvcontrol_get_memory_bus_width(gpu),
        'get_total_dedicated_gpu_memory': display.nvcontrol_get_total_dedicated_gpu_memory(gpu),
        'get_used_dedicated_gpu_memory': display.nvcontrol_get_used_dedicated_gpu_memory(gpu),
        'get_curr_pcie_link_width': display.nvcontrol_get_curr_pcie_link_width(gpu),
        'get_max_pcie_link_width': display.nvcontrol_get_max_pcie_link_width(gpu),
        'get_curr_pcie_link_generation': display.nvcontrol_get_curr_pcie_link_generation(gpu),
        'get_encoder_utilization': display.nvcontrol_get_encoder_utilization(gpu),
        'get_decoder_utilization': display.nvcontrol_get_decoder_utilization(gpu),
        'get_current_performance_level': display.nvcontrol_get_current_performance_level(gpu),
        'get_gpu_nvclock_offset': display.nvcontrol_get_gpu_nvclock_offset(gpu, perf_level),
        'get_mem_transfer_rate_offset': display.nvcontrol_get_mem_transfer_rate_offset(gpu, perf_level),
        'get_cooler_manual_control_enabled': display.nvcontrol_get_cooler_manual_control_enabled(gpu),
        'get_fan_duty': display.nvcontrol_get_fan_duty(fan),
        'get_fan_rpm': display.nvcontrol_get_fan_rpm(fan),
        'get_coolers_used_by_gpu': display.nvcontrol_get_coolers_used_by_gpu(gpu),
        'get_max_displays': display.nvcontrol_get_max_displays(gpu),
        'get_name': display.nvcontrol_get_name(gpu),
        'get_driver_version': display.nvcontrol_get_driver_version(gpu),
        'get_vbios_version': display.nvcontrol_get_vbios_version(gpu),
        'get_gpu_uuid': display.nvcontrol_get_gpu_uuid(gpu),
        'get_utilization_rates': display.nvcontrol_get_utilization_rates(gpu),
        'get_performance_modes': display.nvcontrol_get_performance_modes(gpu),
        'get_gpu_nvclock_offset_range': display.nvcontrol_get_gpu_nvclock_offset_range(gpu, perf_level),
        'get_mem_transfer_rate_offset_range': display.nvcontrol_get_mem_transfer_rate_offset_range(gpu, perf_level),
        'get_clock_info': display.nvcontrol_get_clock_info(gpu)
    }

    pprint(dic)

    display.close()
