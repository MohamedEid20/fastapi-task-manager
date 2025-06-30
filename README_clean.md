# Task Management API

A FastAPI-based REST API for managing tasks with CRUD operations, filtering, and pagination.

## Setup

### Option 1: Local Setup

```bash
pip install -r requirements.txt
python main.py
```

### Option 2: Docker

```bash
# Build the image
docker build -t task-api .

# Run the container
docker run -p 8000:8000 task-api
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /tasks` - Create task
- `GET /tasks` - List tasks (supports filtering and pagination)
- `GET /tasks/{id}` - Get specific task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `GET /tasks/status/{status}` - Filter by status
- `GET /tasks/priority/{priority}` - Filter by priority

## Documentation

Visit http://localhost:8000/docs for interactive API documentation.

## Examples

Create a task:

```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Test task", "priority": "high"}'
```

Get all tasks:

```bash
curl http://localhost:8000/tasks
```

Filter tasks:

```bash
curl http://localhost:8000/tasks?status=pending&priority=high&skip=0&limit=10
```
