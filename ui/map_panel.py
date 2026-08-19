from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import os


class HighwayMap:

    def __init__(self, parent, cctv_callback=None):

        self.cctv_callback = cctv_callback

        # =====================================================
        # MAP WIDGET
        # =====================================================

        self.map_widget = TkinterMapView(
            parent,
            corner_radius=12
        )

        self.map_widget.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # Andhra Pradesh center
        self.map_widget.set_position(
            16.45,
            80.70
        )

        # Moderate zoom for faster initial loading
        self.map_widget.set_zoom(7)

        # =====================================================
        # MAP OBJECTS
        # =====================================================

        self.emergency_marker = None
        self.response_marker = None
        self.route_path = None

        self.cctv_markers = {}
        self.highlighted_cctv = None

        self.animation_id = None
        self.animation_active = False

        self.current_status = None

        # =====================================================
        # VEHICLE ICONS
        # =====================================================

        self.vehicle_images = {}
        self.load_vehicle_icons()

        # Load map markers after UI appears
        parent.after(
            300,
            self.load_static_markers
        )

    # =====================================================
    # LOAD VEHICLE PNG ICONS
    # =====================================================

    def load_vehicle_icons(self):

        # Project root folder
        base_path = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        icons_path = os.path.join(
            base_path,
            "assets",
            "icons"
        )

        icon_files = {

            "AMBULANCE": "ambulance.png",

            "FIRE & RESCUE": "firetruck.png",

            "HIGHWAY PATROL": "patrol.png"

        }

        for unit_type, filename in icon_files.items():

            file_path = os.path.join(
                icons_path,
                filename
            )

            try:

                image = Image.open(
                    file_path
                )

                image = image.resize(
                    (42, 42)
                )

                self.vehicle_images[
                    unit_type
                ] = ImageTk.PhotoImage(
                    image
                )

            except Exception as e:

                print(
                    f"Icon not loaded: {filename}"
                )

    # =====================================================
    # GET VEHICLE ICON
    # =====================================================

    def get_vehicle_icon(self, unit_type):

        return self.vehicle_images.get(
            unit_type
        )

    # =====================================================
    # DELAYED STATIC MARKER LOADING
    # =====================================================

    def load_static_markers(self):

        self.add_highway_markers()

        # Load CCTV slightly later
        self.map_widget.after(
            250,
            self.add_cctv_markers
        )

    # =====================================================
    # HIGHWAY LOCATIONS
    # =====================================================

    def add_highway_markers(self):

        highways = [

            ("NH-16 • Vijayawada", 16.5062, 80.6480),
            ("NH-16 • Guntur", 16.3300, 80.4400),
            ("NH-16 • Ongole", 15.5057, 80.0499),
            ("NH-16 • Nellore", 14.4426, 79.9865),

            ("NH-40 • Kadapa", 14.4673, 78.8242),
            ("NH-44 • Kurnool", 15.8281, 78.0373),

            ("NH-16 • Eluru", 16.7107, 81.1056),
            ("NH-16 • Rajahmundry", 17.0005, 81.8040),

            ("NH-16 • Visakhapatnam", 17.6868, 83.2185),
            ("NH-16 • Srikakulam", 18.2949, 83.8938)

        ]

        for name, lat, lon in highways:

            self.map_widget.set_marker(
                lat,
                lon,
                text=name
            )

    # =====================================================
    # CCTV NETWORK
    # =====================================================

    def add_cctv_markers(self):

        cameras = [

            ("CCTV-VJA-01", 16.5150, 80.6550),
            ("CCTV-VJA-02", 16.4980, 80.6350),
            ("CCTV-VJA-03", 16.5250, 80.6700),

            ("CCTV-GNT-01", 16.3400, 80.4500),
            ("CCTV-GNT-02", 16.3200, 80.4300),
            ("CCTV-GNT-03", 16.3100, 80.4200),

            ("CCTV-ELR-01", 16.7100, 81.1050),
            ("CCTV-ELR-02", 16.7300, 81.1200),

            ("CCTV-RJM-01", 17.0000, 81.8040),
            ("CCTV-RJM-02", 17.0200, 81.8200),

            ("CCTV-ONG-01", 15.5050, 80.0500),
            ("CCTV-ONG-02", 15.4900, 80.0400),

            ("CCTV-NLR-01", 14.4500, 79.9800),
            ("CCTV-NLR-02", 14.4300, 79.9700),
            ("CCTV-NLR-03", 14.4700, 80.0000),

            ("CCTV-KDP-01", 14.4750, 78.8300),
            ("CCTV-KDP-02", 14.4500, 78.8100),

            ("CCTV-KNL-01", 15.8400, 78.0450),
            ("CCTV-KNL-02", 15.8600, 78.0600),

            ("CCTV-VSP-01", 17.6868, 83.2185),
            ("CCTV-VSP-02", 17.7000, 83.2300),

            ("CCTV-SKL-01", 18.2949, 83.8938)

        ]

        self._load_camera_batch(
            cameras,
            0
        )

    # =====================================================
    # LOAD CCTV IN BATCHES
    # =====================================================

    def _load_camera_batch(
        self,
        cameras,
        start_index
    ):

        batch_size = 5

        end_index = min(
            start_index + batch_size,
            len(cameras)
        )

        for index in range(
            start_index,
            end_index
        ):

            camera_id, lat, lon = cameras[index]

            marker = self.map_widget.set_marker(
                lat,
                lon,
                text=f"📹 {camera_id}",
                command=lambda marker, cid=camera_id:
                    self.open_cctv(cid)
            )

            self.cctv_markers[
                camera_id
            ] = marker

        if end_index < len(cameras):

            self.map_widget.after(
                150,
                lambda: self._load_camera_batch(
                    cameras,
                    end_index
                )
            )

    # =====================================================
    # CCTV CLICK
    # =====================================================

    def open_cctv(self, camera_id):

        if self.cctv_callback:

            self.cctv_callback(
                camera_id
            )

    # =====================================================
    # STOP ANIMATION
    # =====================================================

    def stop_animation(self):

        self.animation_active = False

        if self.animation_id is not None:

            try:

                self.map_widget.after_cancel(
                    self.animation_id
                )

            except Exception:

                pass

            self.animation_id = None

    # =====================================================
    # CLEAR OLD EMERGENCY
    # =====================================================

    def clear_emergency(self):

        self.stop_animation()

        if self.emergency_marker:

            try:
                self.emergency_marker.delete()
            except Exception:
                pass

            self.emergency_marker = None

        if self.response_marker:

            try:
                self.response_marker.delete()
            except Exception:
                pass

            self.response_marker = None

        if self.route_path:

            try:
                self.route_path.delete()
            except Exception:
                pass

            self.route_path = None

        if self.highlighted_cctv:

            camera_id = self.highlighted_cctv

            if camera_id in self.cctv_markers:

                try:

                    self.cctv_markers[
                        camera_id
                    ].set_text(
                        f"📹 {camera_id}"
                    )

                except Exception:

                    pass

        self.highlighted_cctv = None
        self.current_status = None

    # =====================================================
    # SHOW INCIDENT
    # =====================================================

    def show_emergency(
        self,
        latitude,
        longitude,
        incident_title="EMERGENCY"
    ):

        self.emergency_marker = self.map_widget.set_marker(
            latitude,
            longitude,
            text=f"🚨 INCIDENT\n{incident_title}"
        )

        self.map_widget.set_position(
            latitude,
            longitude
        )

        self.map_widget.set_zoom(
            10
        )

    # =====================================================
    # HIGHLIGHT CCTV
    # =====================================================

    def highlight_cctv(self, camera_id):

        if camera_id not in self.cctv_markers:

            return

        if (
            self.highlighted_cctv
            and self.highlighted_cctv
            in self.cctv_markers
        ):

            try:

                self.cctv_markers[
                    self.highlighted_cctv
                ].set_text(
                    f"📹 {self.highlighted_cctv}"
                )

            except Exception:

                pass

        marker = self.cctv_markers[
            camera_id
        ]

        marker.set_text(
            f"🔴 ACTIVE CCTV\n{camera_id}\nCLICK TO VIEW"
        )

        self.highlighted_cctv = camera_id

    # =====================================================
    # RESPONSE UNIT TEXT
    # =====================================================

    def get_unit_text(
        self,
        unit,
        status
    ):

        unit_id = unit.get(
            "id",
            "NHAI-UNIT"
        )

        return (
            f"{unit_id}\n"
            f"{status}"
        )

    # =====================================================
    # START RESPONSE TRACKING
    # =====================================================

    def start_response_tracking(
        self,
        unit,
        emergency_lat,
        emergency_lon,
        distance_km,
        status_callback=None
    ):

        self.stop_animation()

        # Remove previous vehicle
        if self.response_marker:

            try:
                self.response_marker.delete()
            except Exception:
                pass

            self.response_marker = None

        # Remove previous route
        if self.route_path:

            try:
                self.route_path.delete()
            except Exception:
                pass

            self.route_path = None

        start_lat = unit["lat"]
        start_lon = unit["lon"]

        # =================================================
        # RESPONSE ROUTE
        # =================================================

        self.route_path = self.map_widget.set_path(
            [
                (start_lat, start_lon),
                (emergency_lat, emergency_lon)
            ],
            width=4
        )

        # =================================================
        # SELECT VEHICLE PNG
        # =================================================

        unit_type = unit.get(
            "type",
            "HIGHWAY PATROL"
        )

        vehicle_icon = self.get_vehicle_icon(
            unit_type
        )

        # =================================================
        # CREATE MOVING VEHICLE MARKER
        # =================================================

        if vehicle_icon:

            self.response_marker = self.map_widget.set_marker(
                start_lat,
                start_lon,
                text=self.get_unit_text(
                    unit,
                    "DISPATCHED"
                ),
                icon=vehicle_icon,
                icon_anchor="center"
            )

        else:

            # Fallback if PNG is missing
            self.response_marker = self.map_widget.set_marker(
                start_lat,
                start_lon,
                text=self.get_unit_text(
                    unit,
                    "DISPATCHED"
                )
            )

        # =================================================
        # ANIMATION SETTINGS
        # =================================================

        duration_seconds = max(
            25,
            min(
                62,
                int(distance_km * 9)
            )
        )

        total_steps = duration_seconds * 5

        self.animation_active = True
        self.current_status = "DISPATCHED"

        if status_callback:

            status_callback(
                "DISPATCHED"
            )

        self.animate_vehicle(
            start_lat,
            start_lon,
            emergency_lat,
            emergency_lon,
            unit,
            0,
            total_steps,
            status_callback
        )

    # =====================================================
    # VEHICLE MOVEMENT
    # =====================================================

    def animate_vehicle(
        self,
        start_lat,
        start_lon,
        end_lat,
        end_lon,
        unit,
        step,
        total_steps,
        status_callback
    ):

        if not self.animation_active:

            return

        # =================================================
        # ARRIVED
        # =================================================

        if step >= total_steps:

            try:

                self.response_marker.set_position(
                    end_lat,
                    end_lon
                )

                self.response_marker.set_text(
                    self.get_unit_text(
                        unit,
                        "ARRIVED"
                    )
                )

            except Exception:

                pass

            if status_callback:

                status_callback(
                    "ARRIVED"
                )

            self.animation_active = False
            self.animation_id = None

            return

        progress = step / total_steps

        # Smooth movement
        smooth_progress = (
            progress
            * progress
            * (3 - 2 * progress)
        )

        current_lat = (
            start_lat
            + (end_lat - start_lat)
            * smooth_progress
        )

        current_lon = (
            start_lon
            + (end_lon - start_lon)
            * smooth_progress
        )

        try:

            self.response_marker.set_position(
                current_lat,
                current_lon
            )

        except Exception:

            return

        # =================================================
        # RESPONSE STATUS
        # =================================================

        if progress < 0.08:

            status = "DISPATCHED"

        elif progress < 0.85:

            status = "EN ROUTE"

        else:

            status = "APPROACHING INCIDENT"

        if status != self.current_status:

            self.current_status = status

            try:

                self.response_marker.set_text(
                    self.get_unit_text(
                        unit,
                        status
                    )
                )

            except Exception:

                pass

            if status_callback:

                status_callback(
                    status
                )

        # =================================================
        # NEXT FRAME
        # =================================================

        self.animation_id = self.map_widget.after(
            300,
            lambda: self.animate_vehicle(
                start_lat,
                start_lon,
                end_lat,
                end_lon,
                unit,
                step + 1,
                total_steps,
                status_callback
            )
        )