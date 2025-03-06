FROM python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . /app

RUN uv sync --all-extras --frozen

ENTRYPOINT ["uv", "run", "-m", "prowl"]
CMD ["--help"]