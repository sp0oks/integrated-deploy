FROM python:alpine

RUN pip install uv

WORKDIR /app

COPY requirements.txt .

RUN uv pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvx", "fastapi", "run", "main.py"]