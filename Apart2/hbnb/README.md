# HBnB Project

## Overview

This project implements a modular Flask application for the HBnB platform, with clear separation into:

- **Presentation Layer:** API endpoints organized under `app/api/v1/`.
- **Business Logic Layer:** Models in `app/models/` and Facade pattern in `app/services/`.
- **Persistence Layer:** In-memory repository pattern in `app/persistence/` (to be replaced by database later).

## Setup Instructions

1. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
