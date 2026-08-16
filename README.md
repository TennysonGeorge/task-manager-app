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
cd task-manager-app/task-manager-api
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
DEBUG=true python app.py
```

The application will automatically reload when you make changes to the code.

## Configuration

The application is configured through environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Interface the server binds to |
| `PORT` | `5001` | Port the server listens on |
| `DEBUG` | unset (off) | Set to `true`, `1`, `yes`, or `on` to enable debug mode |
| `SQLALCHEMY_DATABASE_URI` | `sqlite:///tasks.db` | Database connection string |

`DEBUG` defaults to **off**. Debug mode enables the Werkzeug interactive
debugger, which permits arbitrary code execution by anyone who can reach the
server, so it must never be enabled in a deployed environment. The Compose setup
sets `DEBUG=true` for local development only.

## Docker Support

The application includes Docker support for containerized deployment.

### Using Docker Compose (recommended)

```bash
docker compose up -d --build
```

The app is then available at `http://localhost:5001`.

Useful commands:
```bash
docker compose logs -f        # follow logs
docker compose down           # stop and remove the container
```

### Using Docker directly

1. Build the image:
```bash
docker build -t task-manager-api .
```

2. Run the container:
```bash
docker run -p 5001:5000 -e PORT=5000 task-manager-api
```

The `-e PORT=5000` is required — see "Container port configuration" below.

### Container port configuration

`app.py` defaults to port `5001`, but the Dockerfile exposes `5000` and the
published port mapping is `5001:5000`. Without an explicit `PORT`, the app binds
to `5001` inside the container while the mapping forwards to `5000`, so nothing
is reachable on the host.

`docker-compose.yml` therefore sets `PORT=5000` so the app binds to the port that
is actually mapped. Keep this in mind if you change the port mapping: the
container-side port in `ports:` and the `PORT` environment variable must match.

### Dependency pinning

`Flask-SQLAlchemy==2.5.1` is not compatible with SQLAlchemy 2.x. With
`SQLAlchemy` left unpinned, pip resolves to 2.x and the app crashes on import:

```
AttributeError: module 'sqlalchemy' has no attribute '__all__'
```

`requirements.txt` pins `SQLAlchemy==1.4.54` to avoid this, and
`Flask-Migrate==3.1.0` to stay compatible with `Flask-SQLAlchemy` 2.x. These pins
should be updated together if `Flask-SQLAlchemy` is upgraded to 3.x.

### Database persistence

The Compose setup bind-mounts `./data` into `/app/data` and sets
`SQLALCHEMY_DATABASE_URI=sqlite:///data/tasks.db`, so tasks survive container
restarts. The `data/` directory is created on first run and should not be
committed.

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