# -*- coding: utf-8 -*-
"""
@file
@brief A few functions about GPU.
"""


def pyopencl_status():
    """
    Looks into GPU and CPU to see which card is available.
    Returns a string.

    .. index:: GPU

    .. runpython::
        :showcode:

        from ensae_teaching_cs.faq.faq_gpu import pyopencl_status
        rows.append(pyopencl_status())
    """
    rows = []
    try:
        import pyopencl as cl
    except ImportError as e:
        rows.append("pyopencl is not available due to {}".format(e))
        return "\n".join(rows)

    def catch(fct):
        try:
            return fct()
        except Exception as e:
            return "Unable to retrieve that information due to {}".format(str(e).replace("\n", " "))

    rows.append('=' * 60)
    rows.append('OpenCL plats and Devices')
    for plat in cl.get_platforms():
        rows.append('=' * 60)
        rows.append('plat - Name:  ' + plat.name)
        rows.append('plat - Vendor:  ' + plat.vendor)
        rows.append('plat - Version:  ' + plat.version)
        rows.append('plat - Profile:  ' + plat.profile)
        # rows.append each device per-plat
        for device in plat.get_devices():
            rows.append('-' * 56)
            rows.append('Device - Name:  ' + catch(lambda: device.name))
            rows.append('Device - Type: {}'.format(
                        catch(lambda: cl.device_type.to_string(device.type))))
            rows.append('Device - Max Clock Speed:  {0} Mhz'.format(
                catch(lambda: device.max_clock_frequency)))
            rows.append('Device - Compute Units:  {0}'.format(
                catch(lambda: device.max_compute_units)))
            rows.append('Device - Local Memory:  {0:.0f} KB'.format(
                catch(lambda: device.local_mem_size / 1024.0)))
            rows.append('Device - Constant Memory:  {0:.0f} KB'.format(
                catch(lambda: device.max_constant_buffer_size / 1024.0)))
            rows.append('Device - Global Memory: {0:.0f} GB'.format(
                catch(lambda: device.global_mem_size / 1073741824.0)))
            rows.append('Device - Max Buffer/Image Size: {0:.0f} MB'.format(
                catch(lambda: device.max_mem_alloc_size / 1048576.0)))
            rows.append('Device - Max Work Group Size: {0:.0f}'.format(
                catch(lambda: device.max_work_group_size)))
    rows.append('=' * 60)
    return "\n".join(rows)
