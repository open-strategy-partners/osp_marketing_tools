import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP(
    "OSPEditingServer",
    dependencies=[
        "pydantic>=2.0",
    ]
)

@server.resource("osp://editing-codes")
def get_osp_editing_codes() -> str:
    """Get the OSP editing codes documentation"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, 'osp_editing_codes.md'), 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "Required file 'osp_editing_codes.md' not found. "
            "This file must be present in the same directory as the script."
        )

if __name__ == "__main__":
    try:
        import mcp
        mcp.run()
    except Exception as e:
        print(f"Server failed to start: {str(e)}")
        raise
