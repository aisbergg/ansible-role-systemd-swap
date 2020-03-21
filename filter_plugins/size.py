import re


class FilterModule(object):

    def filters(self):
        return {
            'size': self.size,
        }

    def size(self, size, system_memory):
        if isinstance(size, int):
            return str(size) + "M"
        if not (isinstance(size, str) and size):
            raise ValueError("Size must be a non empty string")

        match = re.match(r"(\d+)\s*(%|(K|M|G|T|P|E|Z|Y)(iB|B){,1}){,1}", size)
        if match:
            value = int(match.group(1))
            unit = match.group(2) or "M"
            if unit == "%":
                value = int(system_memory / 100 * value)
                unit = "M"
            size = str(value) + unit
        else:
            raise ValueError(
                "Size must be a positive number. If no unit is specified it will default to 'M'. A percent value '%' refers to the amount of total available memory. The following units are allowed: K,M,G,T,P,E,Z,Y,KiB,KB,MiB,..."
            )

        return size
