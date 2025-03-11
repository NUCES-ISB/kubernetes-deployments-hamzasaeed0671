# Kubernetes Flask PostgreSQL Deployment

This repository contains configuration files to deploy a Flask application with PostgreSQL on Kubernetes using Minikube.

## Project Structure

The project follows the required structure for submission:

```
k8s-flask-app/
│── manifests/
│   │── deployment/
│   │   │── flask-deployment.yaml
│   │   │── postgres-deployment.yaml
│   │── service/
│   │   │── flask-service.yaml
│   │   │── postgres-service.yaml
│   │── configmap/
│   │   │── postgres-configmap.yaml
│   │── secret/
│   │   │── postgres-secret.yaml
│── app/
│   │── Dockerfile
│   │── requirements.txt
│   │── app.py
│── README.md
```

## Deployment Instructions

See the step-by-step deployment instructions in this document.
