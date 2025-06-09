# Multi-Agent System with MCP (Multi-Agent Communication Protocol)

## Overview
This project implements a multi-agent system using the Multi-Agent Communication Protocol (MCP), focusing on browser-based agent interactions and autonomous task execution.

## Features
- Multi-agent architecture for distributed problem solving
- MCP-based communication protocol for agent interaction
- Autonomous decision-making capabilities
- Task distribution and coordination between agents
- Real-time agent communication and collaboration

## Project Structure
```
MCP-AI_Agent/
├── app.py              # Main application entry point
├── main.py             # Secondary entry point
├── browser_mcp.json    # MCP configuration for browser interactions
├── pyproject.toml      # Project dependencies and metadata
├── .python-version     # Python version specification
├── uv.lock             # Dependency lock file
└── .venv/              # Virtual environment directory
```

## Technical Stack
- Python (version specified in .python-version)
- Project dependencies managed through pyproject.toml
- Virtual environment using .venv
- Browser-based MCP implementation (browser_mcp.json)

## Getting Started

### Prerequisites
- Python (version specified in .python-version)
- Virtual environment support

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/MCP-AI_Agent.git
cd MCP-AI_Agent
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -e .
```

## Usage
The project can be run using either:
```bash
python app.py
# or
python main.py
```

## Configuration
The `browser_mcp.json` file contains the configuration for browser-based agent interactions. This file defines the communication protocol and agent behavior settings.

## Development
- The project uses a modern Python project structure with `pyproject.toml` for dependency management
- Dependencies are locked using `uv.lock` for reproducible builds
- Virtual environment is managed through `.venv`

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License



## Contact
ssujair@gmail.com