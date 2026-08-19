# =========================================================
# NHAI SOS - MAIN DASHBOARD
# =========================================================

import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # Dashboard should fill the application
        self.pack(
            fill="both",
            expand=True
        )

    # =====================================================
    # CREATE MAIN CONTENT AREA
    # =====================================================

    def create_main_container(self):

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

        return main

    # =====================================================
    # CREATE LEFT MAP PANEL
    # =====================================================

    def create_map_panel(self, parent):

        map_panel = ctk.CTkFrame(
            parent,
            fg_color="#0D141D",
            corner_radius=15
        )

        map_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        return map_panel

    # =====================================================
    # CREATE RIGHT CONTROL PANEL
    # =====================================================

    def create_control_panel(self, parent):

        right_panel = ctk.CTkFrame(
            parent,
            width=330,
            fg_color="transparent"
        )

        right_panel.pack(
            side="right",
            fill="y"
        )

        right_panel.pack_propagate(False)

        return right_panel

    # =====================================================
    # CREATE MAP TITLE
    # =====================================================

    def create_map_title(self, parent):

        map_title = ctk.CTkLabel(
            parent,
            text="ANDHRA PRADESH • HIGHWAY MONITORING",
            font=("Arial", 17, "bold"),
            text_color="#E8EDF3"
        )

        map_title.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        return map_title