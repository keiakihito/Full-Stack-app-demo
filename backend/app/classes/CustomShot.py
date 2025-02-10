class CustomShot:
    def __init__(self, shot_data):
        self.is_make = shot_data.get('is_make', False)
        self.location_x = shot_data.get('location_x', 0)
        self.location_y = shot_data.get('location_y', 0)

    def to_dict(self):
        """Convert the CustomShot object to a dictionary."""
        return {
            'is_make': self.is_make,
            'location_x': self.location_x,
            'location_y': self.location_y
        }
