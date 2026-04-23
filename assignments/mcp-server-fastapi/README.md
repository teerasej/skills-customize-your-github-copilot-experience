# 📘 Assignment: Build an MCP Server with FastAPI

## 🎯 Objective

Learn how to design and implement a basic Model Context Protocol (MCP) server using FastAPI, including creating tool endpoints and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Set Up the MCP Server

#### Description
Create a FastAPI application that runs as a local MCP server. Define a root route and one MCP-style endpoint that accepts a JSON request body.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Add a `GET /` route that returns a server status message
- Add a `POST /mcp/tool` route that accepts JSON input
- Run successfully with `uvicorn starter-code:app --reload`


### 🛠️	Implement and Test a Tool Handler

#### Description
Implement a simple tool handler in the `/mcp/tool` route, such as a text summarizer or word counter, and return a structured JSON response with the result.

#### Requirements
Completed program should:

- Read `tool` and `arguments` from the incoming JSON body
- Implement at least one tool (for example: `word_count`)
- Return success and error responses in clear JSON format
- Demonstrate at least two test requests and responses
