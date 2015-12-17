# pylint: disable-msg=too-many-arguments
class Beacon(object):
    """
    Beacon Details
    """
    def __init__(self, form):
        self.advertised_id = form.get('advid')
        self.beacon_type = form.get('type')
        self.status = form.get('status')
        self.description = form.get('description')
        self.indoorlevel_name = form.get('indoorlevel_name')
        self.latitude = form.get('latitude')
        self.longitude = form.get('longitude')
        self.expected_stability = form.get('expected_stability')
        self.position = form.get('position')
        self.place_id = form.get('place_id')

    def registration_request_body(self):
        """
        Return the request body in json format
        """
        body = {
            "advertisedId": {
                "type": self.beacon_type,
                "id": self.advertised_id,
            },
            "status": self.status,
            "placeId": self.place_id,
            "latLng": {
                "latitude": self.latitude,
                "longitude": self.longitude,
            },
            "indoorLevel": {
                "name": self.indoorlevel_name,
            },
            "expectedStability": self.expected_stability,
            "description": self.description,
            "properties": {
                "position": self.position,
            }
        }
        return body
