# syntax=docker/dockerfile:1

# Use a slim Python base image
FROM python:3.10-slim AS base

# Stage for building dependencies
FROM base AS builder

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Create virtual environment
RUN uv venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv uv pip install -r requirements.txt

# Final stage
FROM base AS final

# Set working directory
WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application source code
COPY src/ ./src/

# Expose the port used by the application
EXPOSE 8000

# Define the command to run the application
CMD ["python", "src/osp_marketing_tools/server.py"]