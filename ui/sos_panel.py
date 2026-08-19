# =========================================================
# NHAI SOS - SOS CONTROL PANEL
# =========================================================

import customtkinter as ctk


class SOSPanel(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        sos_callback
    ):

        super().__init__(
            parent,
            height=300,
            fg_color="#111923",
            corner_radius=18
        )

        self.sos_callback = sos_callback

        # Prevent frame size from changing
        self.pack_propagate(False)

        self.create_ui()

    # =====================================================
    # CREATE SOS UI
    # =====================================================

    def create_ui(self):

        # TITLE
        self.title_label = ctk.CTkLabel(
            self,
            text="EMERGENCY SOS",
            font=("Arial", 20, "bold"),
            text_color="#FFFFFF"
        )

        self.title_label.pack(
            pady=(25, 10)
        )

        # SOS BUTTON
        self.sos_button = ctk.CTkButton(
            self,
            text="SOS",
            width=180,
            height=130,
            corner_radius=65,
            fg_color="#C81E2A",
            hover_color="#E52B38",
            font=("Arial", 30, "bold"),
            text_color="white",
            command=self.handle_sos
        )

        self.sos_button.pack(
            pady=20
        )

        # HINT
        self.hint = ctk.CTkLabel(
            self,
            text="Press to initiate emergency response",
            font=("Arial", 11),
            text_color="#8995A3"
        )

        self.hint.pack()

    # =====================================================
    # HANDLE SOS CLICK
    # =====================================================

    def handle_sos(self):

        # Visual feedback
        self.sos_button.configure(
            text="PROCESSING...",
            state="disabled",
            fg_color="#FF3B30",
            hover_color="#FF3B30"
        )

        # Call the main application SOS function
        if self.sos_callback:
            self.sos_callback()

    # =====================================================
    # EMERGENCY ACTIVE
    # =====================================================

    def set_emergency_active(self):

        self.sos_button.configure(
            text="ACTIVE",
            state="disabled",
            fg_color="#FF3B30",
            hover_color="#FF3B30"
        )

        self.title_label.configure(
            text="🚨 EMERGENCY ACTIVE",
            text_color="#FF4B55"
        )

        self.hint.configure(
            text="Emergency response dispatched"
        )

    # =====================================================
    # RESET SOS
    # =====================================================

    def reset_sos(self):

        self.sos_button.configure(
            text="SOS",
            state="normal",
            fg_color="#C81E2A",
            hover_color="#E52B38"
        )

        self.title_label.configure(
            text="EMERGENCY SOS",
            text_color="#FFFFFF"
        )

        self.hint.configure(
            text="Press to initiate emergency response"
        )