# Starter Code: Build an MCP Server with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="MCP Server Starter")


class MCPRequest(BaseModel):
    tool: str
    arguments: dict


@app.get("/")
def root() -> dict:
    return {"status": "ok", "message": "MCP server is running"}


@app.post("/mcp/tool")
def call_tool(request: MCPRequest) -> dict:
    tool = request.tool
    args = request.arguments

    if tool == "word_count":
        text = args.get("text", "")
        if not isinstance(text, str):
            raise HTTPException(status_code=400, detail="'text' must be a string")
        return {
            "tool": tool,
            "result": {
                "word_count": len(text.split())
            }
        }

    raise HTTPException(status_code=400, detail=f"Unknown tool: {tool}")
