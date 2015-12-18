from config import BEACON, DEACTIVATE


class URLBuilder(object):
    """
    docstring for BeaconHelper
    """
    def beacon_deactivation_url(self, beacon_details):
        """
        Returns URL to deactivate the beacons
        """
        return BEACON + beacon_details.beacon_name + DEACTIVATE

    def beacon_modification_url(self, beacon):
        """
        Returns URL to modify beacon details
        """
        return BEACON + beacon.beacon_name

    def __init__(self):
        super(URLBuilder, self).__init__()
