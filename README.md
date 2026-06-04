# Python Desktop Scheduler Application

## Project Overview
This is a lightweight desktop GUI application built during my software engineering internship at the Nigerian Civil Aviation Authority (NCAA) within the Directorate of Aerodrome and Airspace Standards (DAAS). The tool was designed to replace error-prone manual spreadsheets and logbooks used by staff to track inspection timelines, team meetings, and regulatory deadlines.

## Features
- **User-Friendly GUI:** Built using Python's Tkinter library for clean, straightforward navigation by non-technical administrative staff.
- **Local Data Persistence:** Utilizes structured JSON file storage to save, retrieve, and update schedule entries locally without requiring external server infrastructure.
- **Automated Alerts:** Implements Python's `datetime` and `os` modules to trigger automatic 24-hour deadline reminder popups.

## Tech Stack
- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Data Format:** JSON
- **Core Modules:** datetime, os
