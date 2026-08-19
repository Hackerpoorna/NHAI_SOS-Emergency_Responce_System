# 🚨 NHAI SOS
## Highway Emergency Surveillance & Response System

NHAI SOS is a Python-based **Highway Emergency Surveillance and Response System** designed to demonstrate a centralized approach to highway incident monitoring, emergency response coordination, CCTV surveillance, and map-based vehicle dispatch.

The current implementation focuses on **Andhra Pradesh highways** and provides an interactive emergency response simulation through a professional desktop dashboard.

---

## 📌 Project Overview

The system allows a user to trigger an **SOS emergency alert**. Once activated, the application simulates an emergency incident and performs the following operations:

- Generates an emergency scenario.
- Identifies the incident location.
- Finds and highlights the nearest CCTV camera.
- Selects the appropriate emergency response unit.
- Calculates the nearest available resource.
- Displays emergency response information.
- Dispatches a vehicle toward the incident.
- Animates the emergency vehicle on the map.
- Supports repeated SOS emergency simulations.

The project is designed using a **modular software architecture**, making it easier to maintain, extend, and integrate with future real-world systems.

---

# ✨ Features

## 🚨 Emergency SOS System

- One-click SOS activation.
- Multiple randomized emergency incidents.
- Repeated emergency handling.
- Incident ID generation.
- Emergency response workflow.

---

## 🗺️ Interactive Highway Monitoring

- Andhra Pradesh-focused highway monitoring.
- Interactive map visualization.
- Emergency location highlighting.
- Highway route visualization.
- CCTV location markers.
- Emergency vehicle movement simulation.

---

## 🚑 Intelligent Emergency Dispatch

The system automatically selects an emergency response unit based on the incident type.

| Incident | Response Unit |
|---|---|
| Medical Emergency | 🚑 Ambulance |
| Driver Medical Distress | 🚑 Ambulance |
| Vehicle Fire | 🚒 Fire & Rescue |
| Truck Fire | 🚒 Fire & Rescue |
| Accident | 🚓 Highway Patrol |
| Vehicle Breakdown | 🚓 Highway Patrol |
| Road Obstruction | 🚓 Highway Patrol |

---

## 📹 CCTV Surveillance

The system includes simulated CCTV monitoring locations across selected highway corridors.

When an incident occurs:

- The nearest CCTV is identified.
- CCTV markers are highlighted.
- CCTV information is displayed.
- CCTV locations can be selected from the map.
- Incident monitoring footage can be integrated with the surveillance interface.

---

## 🚗 Emergency Vehicle Tracking

After emergency processing:

1. The appropriate response unit is selected.
2. The nearest available vehicle is identified.
3. Distance to the incident is calculated.
4. The vehicle is dispatched.
5. The vehicle moves toward the emergency location.
6. Movement speed is based on the response distance.

The system supports visual emergency vehicle icons such as:

- 🚑 Ambulance
- 🚒 Fire & Rescue
- 🚓 Highway Patrol

---

# 🎲 Supported Emergency Incidents

The application includes multiple simulated emergency scenarios.

1. Road Accident
2. Medical Emergency
3. Vehicle Fire
4. Accident with Fire
5. Vehicle Breakdown
6. Multiple Vehicle Collision
7. Truck Fire
8. Driver Medical Distress
9. Overturned Vehicle
10. Road Obstruction

Each SOS activation can generate a different incident and dispatch the appropriate emergency response resource.

---

# 🔄 Emergency Response Workflow

```text
┌───────────────────┐
│   USER PRESSES    │
│       SOS         │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ INCIDENT GENERATED│
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ LOCATION SELECTED │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ NEAREST CCTV FOUND│
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ RESPONSE UNIT     │
│ SELECTED          │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ EMERGENCY DISPATCH│
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ VEHICLE MOVEMENT  │
│ ON LIVE MAP       │
└───────────────────┘
