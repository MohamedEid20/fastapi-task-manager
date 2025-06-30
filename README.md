# Task Management API

A FastAPI-based REST API for managing tasks with CRUD operations, filtering, and pagination.

## Setup

### Installation

```bash
pip install -r requirements.txt
```

### Environment Configuration

The application uses environment variables for configuration. Copy the example file and adjust as needed:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file as needed
```

Environment variables include:

- `DATABASE_URL`: Connection string for the database
- `API_HOST`: Host to bind the server to
- `API_PORT`: Port to bind the server to
- `DEBUG`: Enable/disable debug mode
- `APP_TITLE`: Application title
- `APP_DESCRIPTION`: Application description
- `APP_VERSION`: Application version

### Run the application

```bash
python main.py
```

### Access API documentation

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Docker Support

### Build and run with Docker

```bash
# Build the image
docker build -t task-api .

# Run the container
docker run -p 8000:8000 task-api

# Run with custom environment variables
docker run -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./tasks.db \
  -e DEBUG=false \
  task-api
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /tasks` - Create task
- `GET /tasks` - List tasks (supports filtering, pagination, and sorting)
- `GET /tasks/{id}` - Get specific task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `GET /tasks/status/{status}` - Filter by status (supports pagination and sorting)
- `GET /tasks/priority/{priority}` - Filter by priority (supports pagination and sorting)

## Example API calls

Create a task:

```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

Get all tasks:

```bash
curl -X GET "http://localhost:8000/tasks"
```

Filter tasks:

```bash
curl -X GET "http://localhost:8000/tasks?status=pending&priority=high&skip=0&limit=10"
```

Sort tasks:

```bash
# Sort by due date (ascending)
curl -X GET "http://localhost:8000/tasks?sort_by=due_date&sort_order=asc"

# Sort by priority (descending)
curl -X GET "http://localhost:8000/tasks?sort_by=priority&sort_order=desc"

# Combine filtering and sorting
curl -X GET "http://localhost:8000/tasks?status=pending&sort_by=created_at&sort_order=desc"
```
