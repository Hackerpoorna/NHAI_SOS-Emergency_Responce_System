# =========================================================
# NHAI SOS - LOCATION SERVICE
# =========================================================

import math
import random


class LocationService:

    # =====================================================
    # CALCULATE DISTANCE BETWEEN TWO GPS LOCATIONS
    # =====================================================

    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):

        # Earth radius in kilometers
        radius = 6371

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)

        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_lat / 2) ** 2
            +
            math.cos(lat1_rad)
            * math.cos(lat2_rad)
            * math.sin(delta_lon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        distance = radius * c

        return round(distance, 2)

    # =====================================================
    # FIND NEAREST LOCATION
    # =====================================================

    def find_nearest(self, latitude, longitude, locations):

        nearest_location = None
        nearest_distance = float("inf")

        for location in locations:

            lat = location.get("latitude")
            lon = location.get("longitude")

            if lat is None or lon is None:
                continue

            distance = self.calculate_distance(
                latitude,
                longitude,
                lat,
                lon
            )

            if distance < nearest_distance:

                nearest_distance = distance
                nearest_location = location.copy()

        if nearest_location is not None:

            nearest_location["distance"] = round(
                nearest_distance,
                2
            )

        return nearest_location

    # =====================================================
    # GENERATE RANDOM SOS LOCATION
    # =====================================================

    def generate_random_location(self, highways):

        if not highways:
            return {
                "latitude": 16.5062,
                "longitude": 80.6480,
                "highway": "NH-16 • Vijayawada"
            }

        highway = random.choice(highways)

        base_lat = highway["latitude"]
        base_lon = highway["longitude"]

        # Generate a nearby emergency point
        latitude = base_lat + random.uniform(
            -0.025,
            0.025
        )

        longitude = base_lon + random.uniform(
            -0.025,
            0.025
        )

        return {
            "latitude": round(latitude, 6),
            "longitude": round(longitude, 6),
            "highway": (
                f'{highway["name"]} • '
                f'{highway["location"]}'
            )
        }

    # =====================================================
    # FORMAT COORDINATES
    # =====================================================

    @staticmethod
    def format_coordinates(latitude, longitude):

        return (
            f"{latitude:.6f}, "
            f"{longitude:.6f}"
        )