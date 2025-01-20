# Start with a base image that has Python and uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

# Set the working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Specify the UV link mode
ENV UV_LINK_MODE=copy

# Copy the pyproject.toml file to the working directory
COPY pyproject.toml /app/

# Use uv to install dependencies
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-install-project --no-dev --no-editable

# Copy the entire project into the working directory
ADD . /app

# Use uv to finalize the installation
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-dev --no-editable

# Start a new stage to keep the final image small
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the necessary files from the uv stage
COPY --from=uv /root/.local /root/.local
COPY --from=uv --chown=app:app /app/.venv /app/.venv

# Update the PATH environment variable to include the virtual environment binaries
ENV PATH="/app/.venv/bin:$PATH"

# Set the entry point to run the MCP server
ENTRYPOINT ["python", "src/osp_marketing_tools/server.py"]