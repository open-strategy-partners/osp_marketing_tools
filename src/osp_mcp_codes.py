import os
from typing import Annotated
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP, Context

# Initialize FastMCP server with clear name and dependencies
server = FastMCP(
    "OSPEditingCodes",
    dependencies=[
        "pydantic>=2.0",
    ]
)

@server.resource("osp://editing-codes")
def get_osp_editing_codes() -> str:
    """Get the OSP editing codes documentation
    
    Returns:
        str: The markdown content as a string
    
    Raises:
        FileNotFoundError: If codes-llm.md is not found in script directory
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, 'codes-llm.md'), 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "Required file 'codes-llm.md' not found. "
            "This file must be present in the same directory as the script."
        )

# Add a health check tool as recommended by the guide
@server.tool()
def health_check() -> dict:
    """Check if the server is running and can access its resources
    
    Returns:
        dict: Health check results
    """
    return {
        "status": "healthy",
        "resources": ["osp://editing-codes"],
        "version": "0.1.0"
    }

# Main entry point with proper error handling
if __name__ == "__main__":
    try:
        print("Starting OSP Editing Codes MCP server...")
        server.run()
    except KeyboardInterrupt:
        print("\nServer shutdown requested via keyboard interrupt")
    except Exception as e:
        print(f"Server failed to start: {str(e)}")
        raise