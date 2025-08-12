# API : Predict Heart Disease
Build a simple FastAPI app that serves predictions from a machine learning classifier trained on the Heart Disease Dataset, Dockerize it, and deploy to Render (or any cloud host of your choice). Focus on Docker and deployment, not on achieving high accuracy.

A FastAPI-based machine learning API for predicting heart disease, containerized with Docker, and deployed on Render.

## Features
- `/health` - API health check
- `/info` - Model info and feature list
- `/predict` - Heart disease prediction


## Run AI Locally
```bash
### preferred way
uvicorn app.main:app --reload

### another way
python -m app.main



## Run Locally
```bash
docker-compose build
docker-compose up
