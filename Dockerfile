# --------------- Dockerfile for ovos-skill-http-demo -----------------
FROM python:3.13-slim

WORKDIR /skill

# Copy the skill source
COPY . /skill

# Install system and Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install ovos-workshop requests setuptools wheel \
    && pip install .

# Default CMD just shows it's built OK
CMD ["python", "-c", "print('ovos-skill-http-demo built successfully')"]
