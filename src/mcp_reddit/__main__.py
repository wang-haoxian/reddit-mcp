#!/usr/bin/env python3
"""
Entry point for running the MCP Reddit server.
Supports both stdio and HTTP/SSE modes.
"""
import argparse
import os
from mcp_reddit.reddit_fetcher import mcp


def main():
    parser = argparse.ArgumentParser(description="Reddit MCP Server")
    parser.add_argument(
        "--transport",
        type=str,
        default=os.getenv("TRANSPORT", "stdio"),
        choices=["stdio", "sse", "streamable-http", "http"],
        help="Transport protocol to use (default: stdio, set via TRANSPORT env var)",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.getenv("HOST", "127.0.0.1"),
        help="Host address to bind to for HTTP/SSE mode (default: 127.0.0.1, set via HOST env var)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("PORT", "8000")),
        help="Port to bind to for HTTP/SSE mode (default: 8000, set via PORT env var)",
    )
    
    args = parser.parse_args()
    
    # Run with appropriate transport
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(
            transport=args.transport,
            host=args.host,
            port=args.port,
        )


if __name__ == "__main__":
    main()
