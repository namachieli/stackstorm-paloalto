"""
    This action is deprecated and will be removed in a future release
"""

from lib.actions import BaseAction


class ApplySingleObject(BaseAction):
    """
    Apply an object to a device
    """
    def run(self, class_string, device_group, firewall, **kwargs):

        device = self.get_panorama(firewall, device_group)
        cls = self.get_pandevice_class(class_string)['cls']
        obj = cls(**kwargs)
        device.add(obj)
        obj.apply()

        device_value = device_group or firewall
        return True, "{} {} successfully applied to {}".format(cls.__name__, obj.name, device_value)
