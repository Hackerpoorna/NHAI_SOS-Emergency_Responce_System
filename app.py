import customtkinter as ctk
import random

from PIL import Image, ImageDraw, ImageFont, ImageTk

from ui.map_panel import HighwayMap

from services.cctv_service import CCTVService
from services.emergency_service import EmergencyService
from services.location_service import LocationService
from services.highway_service import HighwayService

from database import Database


# ============================================================
# APPLICATION THEME
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# ============================================================
# MAIN APPLICATION
# ============================================================

class NHAISOSApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ====================================================
        # WINDOW SETTINGS
        # ====================================================

        self.title(
            "NHAI • Highway Emergency Surveillance"
        )

        self.geometry(
            "1400x850"
        )

        self.minsize(
            1200,
            750
        )

        self.configure(
            fg_color="#080D14"
        )

        # ====================================================
        # SERVICES
        # ====================================================

        self.cctv_service = CCTVService()

        self.emergency_service = EmergencyService()

        self.location_service = LocationService()

        self.highway_service = HighwayService()

        self.database = Database()

        # ====================================================
        # INCIDENT STATE
        # ====================================================

        # Start count from existing database incidents
        self.incident_count = (
            self.database.get_incident_count()
        )

        self.current_incident = None

        self.current_camera = None

        self.current_location = None

        self.current_response_unit = None

        self.current_response_distance = 0

        self.current_emergency_data = None

        self.response_status = "SYSTEM READY"

        # ====================================================
        # ANDHRA PRADESH INCIDENT LOCATIONS
        # ====================================================

        self.incident_locations = [

            {
                "name": "NH-16 • Vijayawada",
                "lat": 16.5062,
                "lon": 80.6480
            },

            {
                "name": "NH-16 • Guntur",
                "lat": 16.3300,
                "lon": 80.4400
            },

            {
                "name": "NH-16 • Ongole",
                "lat": 15.5057,
                "lon": 80.0499
            },

            {
                "name": "NH-16 • Nellore",
                "lat": 14.4426,
                "lon": 79.9865
            },

            {
                "name": "NH-40 • Kadapa",
                "lat": 14.4673,
                "lon": 78.8242
            },

            {
                "name": "NH-44 • Kurnool",
                "lat": 15.8281,
                "lon": 78.0373
            },

            {
                "name": "NH-16 • Eluru",
                "lat": 16.7107,
                "lon": 81.1056
            },

            {
                "name": "NH-16 • Rajahmundry",
                "lat": 17.0005,
                "lon": 81.8040
            },

            {
                "name": "NH-16 • Visakhapatnam",
                "lat": 17.6868,
                "lon": 83.2185
            }
        ]

        # ====================================================
        # BUILD UI
        # ====================================================

        self.create_header()

        self.create_main_area()

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            height=75,
            corner_radius=0,
            fg_color="#0D141D"
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        ctk.CTkLabel(
            header,
            text="NHAI",
            font=("Arial", 26, "bold"),
            text_color="#F4C430"
        ).pack(
            side="left",
            padx=(30, 5)
        )

        ctk.CTkLabel(
            header,
            text="HIGHWAY SURVEILLANCE • ANDHRA PRADESH",
            font=("Arial", 15),
            text_color="#AAB4C0"
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkLabel(
            header,
            text="● CONTROL ROOM ONLINE",
            font=("Arial", 13, "bold"),
            text_color="#48D597"
        ).pack(
            side="right",
            padx=30
        )

    # ========================================================
    # MAIN AREA
    # ========================================================

    def create_main_area(self):

        main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # ====================================================
        # MAP PANEL
        # ====================================================

        map_panel = ctk.CTkFrame(
            main,
            fg_color="#0D141D",
            corner_radius=15
        )

        map_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        ctk.CTkLabel(
            map_panel,
            text="ANDHRA PRADESH • NATIONAL HIGHWAY NETWORK",
            font=("Arial", 17, "bold"),
            text_color="#E8EDF3"
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        self.highway_map = HighwayMap(
            map_panel,
            cctv_callback=self.open_cctv_from_map
        )

        # ====================================================
        # RIGHT CONTROL PANEL
        # ====================================================

        right = ctk.CTkFrame(
            main,
            width=340,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            fill="y"
        )

        right.pack_propagate(
            False
        )

        # ====================================================
        # SOS PANEL
        # ====================================================

        sos = ctk.CTkFrame(
            right,
            height=330,
            fg_color="#111923",
            corner_radius=18
        )

        sos.pack(
            fill="x",
            pady=(0, 12)
        )

        sos.pack_propagate(
            False
        )

        ctk.CTkLabel(
            sos,
            text="HIGHWAY EMERGENCY SOS",
            font=("Arial", 19, "bold"),
            text_color="white"
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            sos,
            text="Automatic incident generation & response simulation",
            font=("Arial", 10),
            text_color="#8995A3"
        ).pack()

        self.sos_button = ctk.CTkButton(
            sos,
            text="SOS",
            width=190,
            height=110,
            corner_radius=55,
            fg_color="#C81E2A",
            hover_color="#E52B38",
            font=("Arial", 34, "bold"),
            command=self.activate_emergency
        )

        self.sos_button.pack(
            pady=12
        )

        self.cctv_button = ctk.CTkButton(
            sos,
            text="VIEW ACTIVE CCTV",
            width=250,
            height=35,
            fg_color="#263647",
            hover_color="#334A62",
            state="disabled",
            command=self.show_cctv_footage
        )

        self.cctv_button.pack()

        # ====================================================
        # STATUS CARDS
        # ====================================================

        self.highway_status_value = (
            self.create_status_card(
                right,
                "HIGHWAY STATUS",
                "● NORMAL",
                "#48D597"
            )
        )

        self.cctv_status_value = (
            self.create_status_card(
                right,
                "ACTIVE CCTV",
                "22 CAMERAS",
                "#F4C430"
            )
        )

        self.response_status_value = (
            self.create_status_card(
                right,
                "RESPONSE STATUS",
                "SYSTEM READY",
                "#48D597"
            )
        )

        self.incident_status_value = (
            self.create_status_card(
                right,
                "TOTAL INCIDENTS",
                f"{self.incident_count:02d}",
                "#AAB4C0"
            )
        )

    # ========================================================
    # ACTIVATE SOS
    # ========================================================

    def activate_emergency(self):

        # Disable temporarily
        self.sos_button.configure(
            text="PROCESSING...",
            state="disabled"
        )

        # Clear previous map response
        self.highway_map.clear_emergency()

        # New incident number
        self.incident_count += 1

        # ====================================================
        # RANDOM ANDHRA PRADESH LOCATION
        # ====================================================

        location = random.choice(
            self.incident_locations
        )

        emergency_lat = location["lat"]

        emergency_lon = location["lon"]

        # ====================================================
        # CREATE COMPLETE INCIDENT
        # ====================================================

        emergency_data = (
            self.emergency_service.create_emergency(
                emergency_lat,
                emergency_lon,
                self.incident_count
            )
        )

        # ====================================================
        # GET RANDOM INCIDENT DETAILS
        # ====================================================

        incident = {

            "type": emergency_data["type"],

            "title": emergency_data["title"],

            "description":
                emergency_data["description"],

            "display":
                emergency_data["display"]
        }

        # ====================================================
        # CCTV VERIFICATION
        # ====================================================

        nearest_camera, camera_distance = (
            self.cctv_service.find_nearest_camera(
                emergency_lat,
                emergency_lon
            )
        )

        # Add CCTV data
        emergency_data["cctv"] = nearest_camera

        emergency_data["cctv_distance"] = (
            camera_distance
        )

        # ====================================================
        # RESPONSE UNIT
        # ====================================================

        response_unit = (
            emergency_data["response_unit"]
        )

        response_distance = (
            emergency_data["response_distance"]
        )

        # ====================================================
        # HOSPITAL
        # ====================================================

        hospital = (
            emergency_data["hospital"]
        )

        hospital_distance = (
            emergency_data["hospital_distance"]
        )

        # ====================================================
        # SAVE CURRENT STATE
        # ====================================================

        self.current_incident = incident

        self.current_camera = nearest_camera

        self.current_location = location

        self.current_response_unit = response_unit

        self.current_response_distance = (
            response_distance
        )

        self.current_emergency_data = (
            emergency_data
        )

        # ====================================================
        # SAVE TO DATABASE
        # ====================================================

        try:

            self.database.save_incident(
                emergency_data
            )

        except Exception as error:

            print(
                "Database error:",
                error
            )

        # ====================================================
        # UPDATE UI
        # ====================================================

        self.sos_button.configure(
            text="ACTIVE"
        )

        self.cctv_button.configure(
            state="normal"
        )

        self.highway_status_value.configure(
            text="● INCIDENT DETECTED",
            text_color="#FF4B55"
        )

        self.cctv_status_value.configure(
            text=nearest_camera["id"],
            text_color="#FF4B55"
        )

        self.response_status_value.configure(
            text="CCTV VERIFIED",
            text_color="#F4C430"
        )

        self.incident_status_value.configure(
            text=f"{self.incident_count:02d}",
            text_color="#FF4B55"
        )

        # ====================================================
        # SHOW INCIDENT ON MAP
        # ====================================================

        self.highway_map.show_emergency(
            emergency_lat,
            emergency_lon,
            incident["display"]
        )

        self.highway_map.highlight_cctv(
            nearest_camera["id"]
        )

        # ====================================================
        # SHOW EMERGENCY POPUP
        # ====================================================

        self.show_emergency_popup(
            location,
            incident,
            nearest_camera,
            camera_distance,
            response_unit,
            response_distance,
            hospital,
            hospital_distance
        )

        # ====================================================
        # START RESPONSE AFTER 5 SECONDS
        # ====================================================

        self.after(
            5000,
            lambda: self.start_response(
                response_unit,
                emergency_lat,
                emergency_lon,
                response_distance
            )
        )

        # ====================================================
        # RESET SOS FOR REPEATED INCIDENT
        # ====================================================

        self.after(
            2500,
            self.reset_sos_button
        )

    # ========================================================
    # START RESPONSE
    # ========================================================

    def start_response(
        self,
        response_unit,
        latitude,
        longitude,
        distance
    ):

        self.response_status_value.configure(
            text="DISPATCHED",
            text_color="#F4C430"
        )

        self.highway_map.start_response_tracking(
            response_unit,
            latitude,
            longitude,
            distance,
            status_callback=self.update_response_status
        )

    # ========================================================
    # RESPONSE STATUS
    # ========================================================

    def update_response_status(
        self,
        status
    ):

        if status == "DISPATCHED":

            color = "#F4C430"

        elif status == "EN ROUTE":

            color = "#48A7FF"

        elif status == "APPROACHING INCIDENT":

            color = "#FF8C42"

        elif status == "ARRIVED":

            color = "#48D597"

        else:

            color = "#FFFFFF"

        self.response_status_value.configure(
            text=status,
            text_color=color
        )

        # Update database when response arrives
        if (
            status == "ARRIVED"
            and self.current_emergency_data
        ):

            try:

                self.database.update_status(
                    self.current_emergency_data[
                        "incident_id"
                    ],
                    "RESPONSE ARRIVED"
                )

            except Exception as error:

                print(
                    "Status update error:",
                    error
                )

    # ========================================================
    # RESET SOS
    # ========================================================

    def reset_sos_button(self):

        self.sos_button.configure(
            text="SOS",
            state="normal",
            fg_color="#C81E2A",
            hover_color="#E52B38"
        )

    # ========================================================
    # CCTV CLICK FROM MAP
    # ========================================================

    def open_cctv_from_map(
        self,
        camera_id
    ):

        self.current_camera = {
            "id": camera_id
        }

        self.show_cctv_footage()

    # ========================================================
    # CREATE CCTV INCIDENT IMAGE
    # ========================================================

    def create_cctv_image(
        self,
        incident_type,
        camera_id
    ):

        width = 640
        height = 320

        image = Image.new(
            "RGB",
            (width, height),
            (18, 22, 28)
        )

        draw = ImageDraw.Draw(
            image
        )

        # ROAD

        draw.rectangle(
            (
                0,
                180,
                width,
                height
            ),
            fill=(45, 48, 52)
        )

        # ROAD LINES

        for x in range(
            0,
            width,
            90
        ):

            draw.rectangle(
                (
                    x,
                    245,
                    x + 45,
                    252
                ),
                fill=(220, 190, 70)
            )

        # CCTV HEADER

        draw.rectangle(
            (
                0,
                0,
                width,
                45
            ),
            fill=(0, 0, 0)
        )

        # ====================================================
        # INCIDENT VISUAL
        # ====================================================

        if incident_type == "ACCIDENT":

            draw.rectangle(
                (
                    220,
                    190,
                    360,
                    250
                ),
                fill=(160, 30, 30)
            )

            draw.rectangle(
                (
                    330,
                    205,
                    450,
                    255
                ),
                fill=(45, 70, 130)
            )

            incident_label = (
                "ROAD ACCIDENT DETECTED"
            )

        elif incident_type == "FIRE":

            draw.rectangle(
                (
                    250,
                    200,
                    390,
                    260
                ),
                fill=(80, 80, 80)
            )

            draw.polygon(
                [
                    (300, 200),
                    (330, 130),
                    (360, 200)
                ],
                fill=(240, 80, 20)
            )

            incident_label = (
                "VEHICLE FIRE DETECTED"
            )

        elif incident_type == "MEDICAL":

            draw.rectangle(
                (
                    260,
                    210,
                    390,
                    260
                ),
                fill=(170, 170, 170)
            )

            draw.ellipse(
                (
                    315,
                    170,
                    350,
                    205
                ),
                fill=(220, 180, 150)
            )

            incident_label = (
                "MEDICAL ASSISTANCE REQUIRED"
            )

        else:

            draw.rectangle(
                (
                    250,
                    210,
                    430,
                    265
                ),
                fill=(120, 100, 50)
            )

            incident_label = (
                "HIGHWAY OBSTRUCTION DETECTED"
            )

        # ====================================================
        # FONT
        # ====================================================

        try:

            font = ImageFont.truetype(
                "arial.ttf",
                18
            )

        except:

            font = ImageFont.load_default()

        # ====================================================
        # CCTV TEXT
        # ====================================================

        draw.text(
            (15, 12),
            f"LIVE • {camera_id}",
            fill=(0, 255, 120),
            font=font
        )

        draw.text(
            (15, 60),
            incident_label,
            fill=(255, 80, 80),
            font=font
        )

        return image

    # ========================================================
    # CCTV WINDOW
    # ========================================================

    def show_cctv_footage(self):

        window = ctk.CTkToplevel(
            self
        )

        window.title(
            "NHAI CCTV INCIDENT VERIFICATION"
        )

        window.geometry(
            "760x560"
        )

        window.configure(
            fg_color="#0B1017"
        )

        camera_id = "UNKNOWN"

        incident_type = "NORMAL"

        incident_name = (
            "LIVE HIGHWAY MONITORING"
        )

        if self.current_camera:

            camera_id = (
                self.current_camera["id"]
            )

        if self.current_incident:

            incident_type = (
                self.current_incident["type"]
            )

            incident_name = (
                self.current_incident["title"]
            )

        ctk.CTkLabel(
            window,
            text="CCTV INCIDENT VERIFICATION",
            font=("Arial", 22, "bold"),
            text_color="#FF4B55"
        ).pack(
            pady=(20, 10)
        )

        image = self.create_cctv_image(
            incident_type,
            camera_id
        )

        photo = ImageTk.PhotoImage(
            image
        )

        image_label = ctk.CTkLabel(
            window,
            text="",
            image=photo
        )

        image_label.image = photo

        image_label.pack(
            pady=10
        )

        ctk.CTkLabel(
            window,
            text=f"""
CAMERA: {camera_id}

EVENT: {incident_name}

STATUS: INCIDENT VERIFIED

NHAI CONTROL ROOM:
RESPONSE DISPATCH INITIATED
""",
            font=("Arial", 14),
            text_color="#E8EDF3",
            justify="left"
        ).pack(
            anchor="w",
            padx=60,
            pady=10
        )

        ctk.CTkButton(
            window,
            text="CLOSE CCTV",
            command=window.destroy
        ).pack(
            pady=10
        )

    # ========================================================
    # INCIDENT POPUP
    # ========================================================

    def show_emergency_popup(
        self,
        location,
        incident,
        camera,
        camera_distance,
        response_unit,
        response_distance,
        hospital,
        hospital_distance
    ):

        popup = ctk.CTkToplevel(
            self
        )

        popup.title(
            "NHAI Emergency Response"
        )

        popup.geometry(
            "550x720"
        )

        popup.resizable(
            False,
            False
        )

        popup.configure(
            fg_color="#111923"
        )

        ctk.CTkLabel(
            popup,
            text=f"🚨 {incident['title']}",
            font=("Arial", 21, "bold"),
            text_color="#FF4B55"
        ).pack(
            pady=(25, 20)
        )

        details = f"""
INCIDENT ID
NHAI-AP-{self.incident_count:04d}


INCIDENT
{incident["description"]}


HIGHWAY LOCATION
{location["name"]}


COORDINATES
{location["lat"]:.4f}, {location["lon"]:.4f}


CCTV VERIFICATION
📹 {camera["id"]}

DISTANCE
{camera_distance} KM


RESPONSE UNIT
{response_unit["symbol"]} {response_unit["type"]}

UNIT ID
{response_unit["id"]}

DISTANCE
{response_distance} KM


NEAREST MEDICAL SUPPORT
🏥 {hospital["name"]}

DISTANCE
{hospital_distance} KM


CONTROL ROOM STATUS
CCTV VERIFIED


DISPATCH STATUS
RESPONSE UNIT ACTIVATES IN 5 SECONDS
"""

        ctk.CTkLabel(
            popup,
            text=details,
            font=("Arial", 13),
            text_color="#E8EDF3",
            justify="left"
        ).pack(
            anchor="w",
            padx=35
        )

        ctk.CTkButton(
            popup,
            text="VIEW CCTV VERIFICATION",
            width=260,
            height=40,
            fg_color="#263647",
            hover_color="#334A62",
            command=self.show_cctv_footage
        ).pack(
            pady=15
        )

    # ========================================================
    # STATUS CARD
    # ========================================================

    def create_status_card(
        self,
        parent,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            parent,
            height=85,
            fg_color="#0D141D",
            corner_radius=15
        )

        card.pack(
            fill="x",
            pady=6
        )

        card.pack_propagate(
            False
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 10),
            text_color="#7F8B99"
        ).pack(
            anchor="w",
            padx=18,
            pady=(13, 2)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 17, "bold"),
            text_color=color
        )

        value_label.pack(
            anchor="w",
            padx=18
        )

        return value_label


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app = NHAISOSApp()

    app.mainloop()