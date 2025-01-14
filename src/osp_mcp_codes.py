import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP(
    "OSPEditingCodes",
    dependencies=[
        "pydantic>=2.0",
    ]
)

@server.resource("osp://editing-codes")
def get_osp_editing_codes() -> str:  # Changed return type to str
    """Get the OSP editing codes documentation
    
    Returns:
        str: The markdown content as a string
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, 'codes-llm.md'), 'r') as f:
            return f.read()  # Return the raw string content
    except FileNotFoundError:
        raise FileNotFoundError(
            "Required file 'codes-llm.md' not found. "
            "This file must be present in the same directory as the script."
        )

if __name__ == "__main__":
    try:
        server.run()
    except Exception as e:
        print(f"Server failed to start: {str(e)}")
        raise