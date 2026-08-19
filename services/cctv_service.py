import math


class CCTVService:

    def __init__(self):

        self.cameras = [
            {
                "id": "CCTV-NH16-VJA-01",
                "location": "NH-16 • Vijayawada",
                "lat": 16.5100,
                "lon": 80.6550
            },
            {
                "id": "CCTV-NH16-VJA-02",
                "location": "NH-16 • Vijayawada Bypass",
                "lat": 16.4950,
                "lon": 80.6300
            },
            {
                "id": "CCTV-NH16-GNT-01",
                "location": "NH-16 • Guntur",
                "lat": 16.3067,
                "lon": 80.4365
            },
            {
                "id": "CCTV-NH16-NLR-01",
                "location": "NH-16 • Nellore",
                "lat": 14.4426,
                "lon": 79.9865
            },
            {
                "id": "CCTV-NH44-KNL-01",
                "location": "NH-44 • Kurnool",
                "lat": 15.8281,
                "lon": 78.0373
            }
        ]

    def calculate_distance(self, lat1, lon1, lat2, lon2):

        radius = 6371

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return radius * c

    def find_nearest_camera(self, latitude, longitude):

        nearest_camera = None
        shortest_distance = float("inf")

        for camera in self.cameras:

            distance = self.calculate_distance(
                latitude,
                longitude,
                camera["lat"],
                camera["lon"]
            )

            if distance < shortest_distance:
                shortest_distance = distance
                nearest_camera = camera

        return nearest_camera, round(shortest_distance, 2)