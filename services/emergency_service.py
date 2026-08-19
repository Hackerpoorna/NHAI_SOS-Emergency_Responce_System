import math
import random


class EmergencyService:

    def __init__(self):

        # =========================================================
        # AMBULANCE UNITS
        # =========================================================

        self.ambulances = [
            {
                "id": "AMB-VJA-01",
                "type": "AMBULANCE",
                "symbol": "🚑",
                "lat": 16.5200,
                "lon": 80.6600
            },
            {
                "id": "AMB-GNT-01",
                "type": "AMBULANCE",
                "symbol": "🚑",
                "lat": 16.3300,
                "lon": 80.4500
            },
            {
                "id": "AMB-ONG-01",
                "type": "AMBULANCE",
                "symbol": "🚑",
                "lat": 15.5000,
                "lon": 80.0600
            },
            {
                "id": "AMB-NLR-01",
                "type": "AMBULANCE",
                "symbol": "🚑",
                "lat": 14.4550,
                "lon": 79.9800
            },
            {
                "id": "AMB-KNL-01",
                "type": "AMBULANCE",
                "symbol": "🚑",
                "lat": 15.8400,
                "lon": 78.0500
            }
        ]

        # =========================================================
        # FIRE UNITS
        # =========================================================

        self.fire_units = [
            {
                "id": "FIRE-VJA-01",
                "type": "FIRE & RESCUE",
                "symbol": "🚒",
                "lat": 16.5350,
                "lon": 80.6700
            },
            {
                "id": "FIRE-GNT-01",
                "type": "FIRE & RESCUE",
                "symbol": "🚒",
                "lat": 16.3450,
                "lon": 80.4600
            },
            {
                "id": "FIRE-ONG-01",
                "type": "FIRE & RESCUE",
                "symbol": "🚒",
                "lat": 15.4900,
                "lon": 80.0400
            },
            {
                "id": "FIRE-NLR-01",
                "type": "FIRE & RESCUE",
                "symbol": "🚒",
                "lat": 14.4600,
                "lon": 79.9750
            },
            {
                "id": "FIRE-KNL-01",
                "type": "FIRE & RESCUE",
                "symbol": "🚒",
                "lat": 15.8500,
                "lon": 78.0600
            }
        ]

        # =========================================================
        # HIGHWAY PATROL
        # =========================================================

        self.patrol_units = [
            {
                "id": "PATROL-NH16-01",
                "type": "HIGHWAY PATROL",
                "symbol": "🚓",
                "lat": 16.4900,
                "lon": 80.6200
            },
            {
                "id": "PATROL-NH16-02",
                "type": "HIGHWAY PATROL",
                "symbol": "🚓",
                "lat": 16.3200,
                "lon": 80.4300
            },
            {
                "id": "PATROL-ONG-01",
                "type": "HIGHWAY PATROL",
                "symbol": "🚓",
                "lat": 15.5200,
                "lon": 80.0700
            },
            {
                "id": "PATROL-NLR-01",
                "type": "HIGHWAY PATROL",
                "symbol": "🚓",
                "lat": 14.4300,
                "lon": 79.9700
            },
            {
                "id": "PATROL-KNL-01",
                "type": "HIGHWAY PATROL",
                "symbol": "🚓",
                "lat": 15.8600,
                "lon": 78.0700
            }
        ]

        # =========================================================
        # HOSPITALS
        # =========================================================

        self.hospitals = [
            {
                "name": "Vijayawada Emergency Hospital",
                "lat": 16.5150,
                "lon": 80.6450
            },
            {
                "name": "Guntur Trauma Center",
                "lat": 16.3100,
                "lon": 80.4400
            },
            {
                "name": "Ongole Emergency Hospital",
                "lat": 15.5100,
                "lon": 80.0500
            },
            {
                "name": "Nellore Trauma Center",
                "lat": 14.4500,
                "lon": 79.9900
            },
            {
                "name": "Kurnool Emergency Hospital",
                "lat": 15.8300,
                "lon": 78.0400
            }
        ]

    # =========================================================
    # DISTANCE CALCULATION
    # =========================================================

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
            +
            math.cos(lat1)
            *
            math.cos(lat2)
            *
            math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return radius * c

    # =========================================================
    # FIND NEAREST
    # =========================================================

    def find_nearest(self, resources, latitude, longitude):

        nearest = None
        shortest_distance = float("inf")

        for resource in resources:

            distance = self.calculate_distance(
                latitude,
                longitude,
                resource["lat"],
                resource["lon"]
            )

            if distance < shortest_distance:

                shortest_distance = distance
                nearest = resource

        return nearest, round(shortest_distance, 2)

    # =========================================================
    # RESPONSE UNIT
    # =========================================================

    def get_response_unit(
        self,
        emergency_type,
        latitude,
        longitude
    ):

        if emergency_type == "MEDICAL":

            resources = self.ambulances

        elif emergency_type == "FIRE":

            resources = self.fire_units

        else:

            resources = self.patrol_units

        return self.find_nearest(
            resources,
            latitude,
            longitude
        )

    # =========================================================
    # HOSPITAL
    # =========================================================

    def find_nearest_hospital(
        self,
        latitude,
        longitude
    ):

        return self.find_nearest(
            self.hospitals,
            latitude,
            longitude
        )

    # =========================================================
    # RANDOM INCIDENT
    # =========================================================

    def get_random_incident(self):

        incidents = [

            {
                "type": "ACCIDENT",
                "title": "ROAD ACCIDENT",
                "description": "Two vehicles involved in a highway collision.",
                "display": "ACCIDENT"
            },

            {
                "type": "MEDICAL",
                "title": "MEDICAL EMERGENCY",
                "description": "Passenger requires urgent medical support.",
                "display": "MEDICAL SOS"
            },

            {
                "type": "FIRE",
                "title": "VEHICLE FIRE",
                "description": "Vehicle fire detected on the highway.",
                "display": "FIRE ALERT"
            },

            {
                "type": "FIRE",
                "title": "ACCIDENT WITH FIRE",
                "description": "Highway collision followed by a vehicle fire.",
                "display": "ACCIDENT + FIRE"
            },

            {
                "type": "BREAKDOWN",
                "title": "VEHICLE BREAKDOWN",
                "description": "Vehicle stopped in an unsafe highway zone.",
                "display": "BREAKDOWN"
            },

            {
                "type": "ACCIDENT",
                "title": "MULTIPLE VEHICLE COLLISION",
                "description": "Multiple vehicles involved in a highway collision.",
                "display": "MULTI VEHICLE ACCIDENT"
            },

            {
                "type": "FIRE",
                "title": "TRUCK FIRE",
                "description": "Heavy vehicle fire reported on NH corridor.",
                "display": "TRUCK FIRE"
            },

            {
                "type": "MEDICAL",
                "title": "DRIVER MEDICAL DISTRESS",
                "description": "Driver requires immediate emergency support.",
                "display": "MEDICAL DISTRESS"
            },

            {
                "type": "ACCIDENT",
                "title": "OVERTURNED VEHICLE",
                "description": "Vehicle overturned and partially blocking highway.",
                "display": "OVERTURNED VEHICLE"
            },

            {
                "type": "BREAKDOWN",
                "title": "ROAD OBSTRUCTION",
                "description": "Hazard detected requiring highway patrol.",
                "display": "ROAD HAZARD"
            }
        ]

        return random.choice(incidents)
    
        # =========================================================
    # GENERATE INCIDENT ID
    # =========================================================

    def generate_incident_id(self, incident_number):

        return f"NHAI-AP-{incident_number:04d}"


    # =========================================================
    # CREATE COMPLETE EMERGENCY DATA
    # =========================================================

    def create_emergency(
        self,
        latitude,
        longitude,
        incident_number
    ):

        # Get random incident
        incident = self.get_random_incident()

        # Find nearest emergency response unit
        response_unit, response_distance = (
            self.get_response_unit(
                incident["type"],
                latitude,
                longitude
            )
        )

        # Find nearest hospital
        hospital, hospital_distance = (
            self.find_nearest_hospital(
                latitude,
                longitude
            )
        )

        # Generate complete emergency object
        emergency_data = {

            "incident_id": self.generate_incident_id(
                incident_number
            ),

            "type": incident["type"],

            "title": incident["title"],

            "description": incident["description"],

            "display": incident["display"],

            "latitude": latitude,

            "longitude": longitude,

            "response_unit": response_unit,

            "response_distance": response_distance,

            "hospital": hospital,

            "hospital_distance": hospital_distance,

            "status": "DISPATCH INITIATED"
        }

        return emergency_data


    # =========================================================
    # DISPATCH RESPONSE
    # =========================================================

    def dispatch_response(self, emergency_data):

        emergency_data[
            "status"
        ] = "UNIT EN ROUTE"

        return emergency_data


    # =========================================================
    # CALCULATE ESTIMATED RESPONSE TIME
    # =========================================================

    def calculate_response_time(
        self,
        distance,
        emergency_type
    ):

        speeds = {

            "MEDICAL": 60,

            "FIRE": 50,

            "ACCIDENT": 60,

            "BREAKDOWN": 70
        }

        speed = speeds.get(
            emergency_type,
            50
        )

        time_minutes = (
            distance / speed
        ) * 60

        return max(
            1,
            round(time_minutes)
        )