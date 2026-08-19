# =========================================================
# NHAI SOS - EMERGENCY RESPONSE PANEL
# =========================================================

import customtkinter as ctk


class EmergencyPanel:

    def __init__(
        self,
        parent,
        emergency_data,
        cctv_data=None
    ):

        self.parent = parent
        self.emergency_data = emergency_data
        self.cctv_data = cctv_data

        self.show()

    # =====================================================
    # SHOW EMERGENCY WINDOW
    # =====================================================

    def show(self):

        emergency_window = ctk.CTkToplevel(
            self.parent
        )

        emergency_window.title(
            "🚨 NHAI Emergency Response Active"
        )

        emergency_window.geometry(
            "520x700"
        )

        emergency_window.resizable(
            False,
            False
        )

        emergency_window.configure(
            fg_color="#111923"
        )

        # =================================================
        # TITLE
        # =================================================

        title = ctk.CTkLabel(
            emergency_window,
            text="🚨 EMERGENCY RESPONSE ACTIVE",
            font=("Arial", 21, "bold"),
            text_color="#FF4B55"
        )

        title.pack(
            pady=(25, 20)
        )

        # =================================================
        # INCIDENT INFORMATION
        # =================================================

        incident_id = self.emergency_data.get(
            "incident_id",
            "NHAI-AP-0001"
        )

        incident_title = self.emergency_data.get(
            "title",
            "HIGHWAY EMERGENCY"
        )

        latitude = self.emergency_data.get(
            "latitude",
            16.5062
        )

        longitude = self.emergency_data.get(
            "longitude",
            80.6480
        )

        response_unit = self.emergency_data.get(
            "response_unit",
            {}
        )

        hospital = self.emergency_data.get(
            "hospital",
            {}
        )

        response_distance = self.emergency_data.get(
            "response_distance",
            0
        )

        hospital_distance = self.emergency_data.get(
            "hospital_distance",
            0
        )

        status = self.emergency_data.get(
            "status",
            "DISPATCH INITIATED"
        )

        # =================================================
        # RESPONSE UNIT DETAILS
        # =================================================

        response_symbol = response_unit.get(
            "symbol",
            "🚑"
        )

        response_name = response_unit.get(
            "id",
            "NHAI RESPONSE UNIT"
        )

        response_type = response_unit.get(
            "type",
            "EMERGENCY RESPONSE"
        )

        # =================================================
        # CCTV DETAILS
        # =================================================

        if self.cctv_data:

            cctv_id = self.cctv_data.get(
                "id",
                "CCTV-AP-01"
            )

            cctv_distance = self.cctv_data.get(
                "distance",
                0
            )

        else:

            cctv_id = "SEARCHING..."

            cctv_distance = 0

        # =================================================
        # EMERGENCY DETAILS TEXT
        # =================================================

        emergency_text = f"""
INCIDENT ID
{incident_id}

INCIDENT TYPE
{incident_title}

LOCATION
ANDHRA PRADESH NATIONAL HIGHWAY

COORDINATES
{latitude:.6f}, {longitude:.6f}

NEAREST CCTV
📹 {cctv_id}
Distance: {cctv_distance} KM

EMERGENCY RESPONSE
{response_symbol} {response_type}
Unit: {response_name}
Distance: {response_distance} KM

NEAREST HOSPITAL
🏥 {hospital.get("name", "Emergency Hospital")}
Distance: {hospital_distance} KM

STATUS
{status}
"""

        details = ctk.CTkLabel(
            emergency_window,
            text=emergency_text,
            font=("Arial", 14),
            text_color="#E8EDF3",
            justify="left"
        )

        details.pack(
            anchor="w",
            padx=45,
            pady=10
        )

        # =================================================
        # STATUS BUTTON
        # =================================================

        status_label = ctk.CTkLabel(
            emergency_window,
            text="NHAI CONTROL ROOM • RESPONSE MONITORING",
            font=("Arial", 11, "bold"),
            text_color="#F4C430"
        )

        status_label.pack(
            pady=(10, 5)
        )

        # =================================================
        # CLOSE BUTTON
        # =================================================

        close_button = ctk.CTkButton(
            emergency_window,
            text="CLOSE MONITOR",
            width=180,
            height=40,
            fg_color="#283442",
            hover_color="#364556",
            command=emergency_window.destroy
        )

        close_button.pack(
            pady=(10, 25)
        )

        # Bring window to front
        emergency_window.lift()
        emergency_window.focus_force()