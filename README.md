# Patient Management Service

![Project Demo](docs/patient-service-demo.gif)

A Django-based patient management system designed to help healthcare professionals register, organize, search, and manage patient records through a web interface.

## Overview

Patient Management Service is a web application built to simplify patient information management. It provides a centralized interface for handling patient records, filtering information, and performing common administrative tasks.

The project uses Django with PostgreSQL and Docker to provide a structured development environment.

## Features

- **Patient Management:** Register new patients, view patient details, update records, and delete records.
- **Search and Filtering:** Search patient records and filter by gender and selected medical conditions.
- **Patient List:** View patient records in a structured table with pagination.
- **Bulk Deletion:** Select and delete multiple patient records in one operation.
- **Excel Export:** Export patient data, including the currently applied filters.
- **Database Backup:** Create database backups.
- **Database Restore:** Restore database information from a backup file.
- **Responsive Interface:** A clean interface designed for convenient patient record management.
- **Persian Date Display:** Display supported dates using the Jalali calendar.

## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Infrastructure:** Docker, Docker Compose
- **Version Control:** Git, GitHub

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Git
- Docker
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SAEED-ESK/Django-Patient-Service.git
   cd Django-Patient-Service
   ```

2. Configure the required environment variables according to the project's settings and Docker Compose configuration.

3. Build and start the application:

   ```bash
   docker compose up --build -d
   ```

4. Apply database migrations:

   ```bash
   docker compose exec patient_service_backend python manage.py migrate
   ```

5. Create a Django superuser:

   ```bash
   docker compose exec patient_service_backend python manage.py createsuperuser
   ```

6. Open the application in your browser using the local address configured in Docker Compose, typically:

   ```text
   http://localhost:8000/
   ```

> **Note:** The commands above assume the backend service is named `patient_service_backend` in `docker-compose.yml`.

## Project Structure

The application follows Django's project structure, separating application logic, database models, views, templates, and configuration.

The project is containerized to simplify local setup and provide a consistent development environment.

## Security Considerations

Patient records contain sensitive information. A deployment intended for real-world use should enforce server-side authentication and authorization, protect database credentials, validate backup files, and restrict access to backup and restore operations.

This repository is a software development project and should not be used with real patient data in an exposed environment without an appropriate security review.

## Author

**Saeed Eskandary**

- GitHub: [@SAEED-ESK](https://github.com/SAEED-ESK)

