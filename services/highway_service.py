# =========================================================
# NHAI SOS - HIGHWAY SERVICE
# =========================================================

from config import HIGHWAYS


class HighwayService:

    # =====================================================
    # GET ALL ANDHRA PRADESH HIGHWAYS
    # =====================================================

    def get_all_highways(self):

        return HIGHWAYS.copy()

    # =====================================================
    # GET HIGHWAY BY NAME
    # =====================================================

    def get_highway_by_name(self, highway_name):

        for highway in HIGHWAYS:

            if highway["name"] == highway_name:
                return highway.copy()

        return None

    # =====================================================
    # GET HIGHWAY BY LOCATION
    # =====================================================

    def get_highway_by_location(self, location):

        for highway in HIGHWAYS:

            if highway["location"].lower() == location.lower():
                return highway.copy()

        return None

    # =====================================================
    # GET HIGHWAYS UNDER MONITORING
    # =====================================================

    def get_monitoring_highways(self):

        monitoring_list = []

        for highway in HIGHWAYS:

            if highway["status"] in [
                "MONITORING",
                "ROAD WORK"
            ]:

                monitoring_list.append(
                    highway.copy()
                )

        return monitoring_list

    # =====================================================
    # GET ROAD WORK LOCATIONS
    # =====================================================

    def get_road_work_locations(self):

        road_work = []

        for highway in HIGHWAYS:

            if highway["status"] == "ROAD WORK":

                road_work.append(
                    {
                        "name": (
                            f'{highway["name"]} • '
                            f'{highway["location"]}'
                        ),
                        "latitude": highway["latitude"],
                        "longitude": highway["longitude"],
                        "status": "ROAD WORK"
                    }
                )

        return road_work

    # =====================================================
    # GET NORMAL HIGHWAYS
    # =====================================================

    def get_normal_highways(self):

        normal_highways = []

        for highway in HIGHWAYS:

            if highway["status"] == "NORMAL":

                normal_highways.append(
                    highway.copy()
                )

        return normal_highways

    # =====================================================
    # GET HIGHWAY SUMMARY
    # =====================================================

    def get_highway_summary(self):

        total = len(HIGHWAYS)

        normal = len(
            self.get_normal_highways()
        )

        monitoring = len(
            self.get_monitoring_highways()
        )

        road_work = len(
            self.get_road_work_locations()
        )

        return {
            "total_highways": total,
            "normal": normal,
            "monitoring": monitoring,
            "road_work": road_work
        }