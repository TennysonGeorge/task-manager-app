# Task Manager API

A modern task management application built with Flask, SQLAlchemy, and a clean web interface. This application allows users to create, read, update, and delete tasks through both a web interface and REST API endpoints.

## Features

- Clean and responsive web interface
- RESTful API endpoints
- SQLite database for data persistence
- Task status tracking
- Real-time updates without page refresh

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TennysonGeorge/task-manager-app.git
cd task-manager-api
```

2. Create a virtual environment:
```bash
# For macOS/Linux
python3 -m venv task-manager
source task-manager/bin/activate

# For Windows
python -m venv task-manager
task-manager\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
# For macOS/Linux
source task-manager/bin/activate

# For Windows
task-manager\Scripts\activate
```

2. Start the Flask application:
```bash
python app.py
```

3. Access the application:
- Web Interface: Open `http://127.0.0.1:5001` in your browser
- API Endpoints: Available at `http://127.0.0.1:5001/tasks`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web interface |
| GET | `/tasks` | Retrieve all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/<id>` | Retrieve a specific task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

### Example API Usage

Create a new task:
```bash
curl -X POST http://127.0.0.1:5001/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "description": "Task description"}'
```

## Project Structure

```
task-manager-api/
├── api/
│   ├── __init__.py
│   ├── models.py      # Database models
│   └── routes.py      # API routes
├── static/
│   ├── css/
│   │   └── style.css  # Application styles
│   └── js/
│       └── script.js  # Frontend JavaScript
├── templates/
│   └── index.html     # Main HTML template
├── app.py            # Application entry point
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Development

To run the application in development mode with debug features:
```bash
python app.py
```

The application will automatically reload when you make changes to the code.

## Docker Support

The application includes Docker support for containerized deployment.

1. Build the Docker image:
```bash
docker build -t task-manager-api .
```

2. Run the container:
```bash
docker run -p 5001:5000 task-manager-api
```

Or use Docker Compose:
```bash
docker-compose up
```

## Testing

Run the test suite:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.