# MCP Reddit Server
[![smithery badge](https://smithery.ai/badge/@adhikasp/mcp-reddit)](https://smithery.ai/server/@adhikasp/mcp-reddit)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that provides tools for fetching and analyzing Reddit content.

<a href="https://glama.ai/mcp/servers/3cg9gdyors"><img width="380" height="200" src="https://glama.ai/mcp/servers/3cg9gdyors/badge" alt="mcp-reddit MCP server" /></a>

## Features

- Fetch hot threads from any subreddit
- Get detailed post content including comments
- Support for different post types (text, link, gallery)

## Installation

### Installing via Smithery

To install Reddit Content for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@adhikasp/mcp-reddit):

```bash
npx -y @smithery/cli install @adhikasp/mcp-reddit --client claude
```

### Manual Installation
```json
{
  "reddit": {
    "command": "uvx",
    "args": ["--from", "git+https://github.com/adhikasp/mcp-reddit.git", "mcp-reddit"],
    "env": {}
  }
}
```

### Docker Installation

The easiest way to run the MCP Reddit server is using Docker and Docker Compose.

1. Clone the repository:
```bash
git clone https://github.com/adhikasp/mcp-reddit.git
cd mcp-reddit
```

2. Create a `.env` file from the example:
```bash
cp .env.example .env
```

3. Edit `.env` and add your Reddit API credentials:
```bash
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_REFRESH_TOKEN=your_refresh_token_here
```

4. Start the server using Docker Compose:
```bash
docker-compose up -d
```

The server will be available at `http://localhost:8000` by default.

#### Docker Configuration

The Docker setup supports multiple transport modes via environment variables:

- **SSE Mode** (default): `TRANSPORT=sse` - Server-Sent Events over HTTP
- **Streamable HTTP Mode**: `TRANSPORT=streamable-http`
- **Standard HTTP Mode**: `TRANSPORT=http`
- **Stdio Mode**: `TRANSPORT=stdio` - For direct pipe communication

You can override the port by setting `PORT` in your `.env` file.

#### Building and Running Manually

If you prefer to build and run the Docker container manually:

```bash
# Build the image
docker build -t reddit-mcp .

# Run with SSE transport (HTTP mode)
docker run -p 8000:8000 \
  -e TRANSPORT=sse \
  -e REDDIT_CLIENT_ID=your_id \
  -e REDDIT_CLIENT_SECRET=your_secret \
  -e REDDIT_REFRESH_TOKEN=your_token \
  reddit-mcp

# Or run with stdio transport (for piping)
docker run -i \
  -e TRANSPORT=stdio \
  -e REDDIT_CLIENT_ID=your_id \
  -e REDDIT_CLIENT_SECRET=your_secret \
  -e REDDIT_REFRESH_TOKEN=your_token \
  reddit-mcp
```

## Usage

Using [mcp-client-cli](https://github.com/adhikasp/mcp-client-cli):

```
$ llm what are latest hot thread in r/victoria3

I'll fetch the latest hot threads from the Victoria 3 subreddit for you.

Tool Calls:
  fetch_hot_threads
  Args:
    subreddit: victoria3


Based on the hot threads, here are the key highlights from the Victoria 3 subreddit:

1. Dev Diary #126 - Update 1.8 Overview
   - Major updates planned for the game, including:
     - Political Movement Rework (Ideological Forces)
     - Discrimination Rework
     - Food Availability, Famines, and Harvest Incidents
     - Additional features like Companies owning buildings and Bulk Nationalization

2. Dev Diary #138 - Pivot of Empire Update
   - Update 1.8 "Masala Chai" has been released
   - Focuses on India with new Journal Entries, Events, and Immersion Pack
   - 10 new achievements added
   - Save games from 1.7.7 are not compatible with 1.8

3. Interesting Community Discussions:
   - A player shared a detailed experience of retaking Constantinople as Greece, highlighting the complex population dynamics
   - Humorous posts about game mechanics, such as investment rights and political movements
   - Various memes and gameplay screenshots showcasing unique game situations

The most upvoted thread is the Dev Diary #126, which provides an in-depth look at the upcoming game mechanics improvements, particularly the reworks to political movements and discrimination systems.

Would you like me to elaborate on any of these points or provide more details about the Victoria 3 update?
``` 
