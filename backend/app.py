import sys
from pathlib import Path

# Ensure the project root is on the Python path so we can import the existing actions package.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict, Optional

# Import only cross-platform actions
try:
    from actions.web_search import web_search as web_search_action
except ImportError:
    web_search_action = None

try:
    from actions.weather_report import weather_action
except ImportError:
    weather_action = None

try:
    from actions.flight_finder import flight_finder
except ImportError:
    flight_finder = None

# Windows-only actions (will skip on Linux/cloud)
try:
    from actions.open_app import open_app
except ImportError:
    open_app = None

try:
    from actions.send_message import send_message
except ImportError:
    send_message = None

try:
    from actions.reminder import reminder
except ImportError:
    reminder = None

try:
    from actions.computer_settings import computer_settings
except ImportError:
    computer_settings = None

try:
    from actions.browser_control import browser_control
except ImportError:
    browser_control = None

try:
    from actions.file_controller import file_controller
except ImportError:
    file_controller = None

try:
    from actions.youtube_video import youtube_video
except ImportError:
    youtube_video = None

try:
    from actions.cmd_control import cmd_control
except ImportError:
    cmd_control = None

try:
    from actions.desktop import desktop_control
except ImportError:
    desktop_control = None

try:
    from actions.code_helper import code_helper
except ImportError:
    code_helper = None

try:
    from actions.dev_agent import dev_agent
except ImportError:
    dev_agent = None

try:
    from actions.computer_control import computer_control
except ImportError:
    computer_control = None


class ToolRequest(BaseModel):
    name: str
    parameters: Optional[Dict[str, Any]] = None


class ToolResponse(BaseModel):
    tool: str
    result: str
    error: Optional[str] = None


class _DummyPlayer:
    def __init__(self) -> None:
        self.logs = []

    def write_log(self, text: str) -> None:
        self.logs.append(text)


app = FastAPI(title="Jarvis API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    return {"message": "Jarvis backend is running. POST to /api/tool to call actions."}


@app.post("/api/tool", response_model=ToolResponse)
def call_tool(req: ToolRequest):
    tool_name = req.name
    parameters = req.parameters or {}
    player = _DummyPlayer()

    tool_map = {
        "web_search": (web_search_action, lambda: web_search_action(parameters=parameters, player=player)),
        "weather_report": (weather_action, lambda: weather_action(parameters=parameters, player=player)),
        "flight_finder": (flight_finder, lambda: flight_finder(parameters=parameters, player=player)),
        "open_app": (open_app, lambda: open_app(parameters=parameters, response=None, player=player)),
        "send_message": (send_message, lambda: send_message(parameters=parameters, response=None, player=player, session_memory=None)),
        "reminder": (reminder, lambda: reminder(parameters=parameters, response=None, player=player)),
        "computer_settings": (computer_settings, lambda: computer_settings(parameters=parameters, response=None, player=player)),
        "browser_control": (browser_control, lambda: browser_control(parameters=parameters, player=player)),
        "file_controller": (file_controller, lambda: file_controller(parameters=parameters, player=player)),
        "youtube_video": (youtube_video, lambda: youtube_video(parameters=parameters, response=None, player=player)),
        "cmd_control": (cmd_control, lambda: cmd_control(parameters=parameters, player=player)),
        "desktop_control": (desktop_control, lambda: desktop_control(parameters=parameters, player=player)),
        "code_helper": (code_helper, lambda: code_helper(parameters=parameters, player=player, speak=lambda text: None)),
        "dev_agent": (dev_agent, lambda: dev_agent(parameters=parameters, player=player, speak=lambda text: None)),
        "computer_control": (computer_control, lambda: computer_control(parameters=parameters, player=player)),
    }

    if tool_name not in tool_map:
        raise HTTPException(status_code=400, detail=f"Unknown tool: {tool_name}")

    handler, executor = tool_map[tool_name]
    
    if handler is None:
        # Tool not available on this platform (e.g., Windows-only tool on Linux)
        return ToolResponse(
            tool=tool_name, 
            result=f"Tool '{tool_name}' is not available on this platform. This is usually a Windows-only tool."
        )

    try:
        result = executor()
        if result is None:
            result = "Tool executed successfully." if player.logs == [] else "\n".join(player.logs)
        return ToolResponse(tool=tool_name, result=str(result))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

