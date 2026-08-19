# =========================================================
# NHAI SOS - DATABASE SERVICE
# =========================================================

import sqlite3

from config import DATABASE_NAME


class Database:

    def __init__(self):

        self.database_name = DATABASE_NAME

        self.create_tables()

    # =====================================================
    # CREATE DATABASE TABLES
    # =====================================================

    def create_tables(self):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS incidents (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                incident_id TEXT,

                incident_type TEXT,

                incident_title TEXT,

                description TEXT,

                latitude REAL,

                longitude REAL,

                response_unit TEXT,

                response_distance REAL,

                hospital TEXT,

                hospital_distance REAL,

                status TEXT,

                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()

        connection.close()

    # =====================================================
    # SAVE INCIDENT
    # =====================================================

    def save_incident(self, emergency_data):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO incidents (

                incident_id,
                incident_type,
                incident_title,
                description,
                latitude,
                longitude,
                response_unit,
                response_distance,
                hospital,
                hospital_distance,
                status

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (
                emergency_data.get("incident_id"),

                emergency_data.get("type"),

                emergency_data.get("title"),

                emergency_data.get("description"),

                emergency_data.get("latitude"),

                emergency_data.get("longitude"),

                emergency_data
                .get("response_unit", {})
                .get("id"),

                emergency_data
                .get("response_distance"),

                emergency_data
                .get("hospital", {})
                .get("name"),

                emergency_data
                .get("hospital_distance"),

                emergency_data
                .get("status")
            )
        )

        connection.commit()

        connection.close()

    # =====================================================
    # GET ALL INCIDENTS
    # =====================================================

    def get_all_incidents(self):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM incidents
            ORDER BY id DESC
            """
        )

        incidents = cursor.fetchall()

        connection.close()

        return incidents

    # =====================================================
    # GET INCIDENT COUNT
    # =====================================================

    def get_incident_count(self):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM incidents
            """
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count

    # =====================================================
    # UPDATE INCIDENT STATUS
    # =====================================================

    def update_status(
        self,
        incident_id,
        status
    ):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE incidents

            SET status = ?

            WHERE incident_id = ?
            """,

            (
                status,
                incident_id
            )
        )

        connection.commit()

        connection.close()

    # =====================================================
    # GET LATEST INCIDENT
    # =====================================================

    def get_latest_incident(self):

        connection = sqlite3.connect(
            self.database_name
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM incidents

            ORDER BY id DESC

            LIMIT 1
            """
        )

        incident = cursor.fetchone()

        connection.close()

        return incident