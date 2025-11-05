# -----------------------------
# Dockerfile for ovos-skill-http-demo
# -----------------------------
FROM docker.io/smartgic/ovos-skill-base:stable

# Copy your skill into the container
COPY . /opt/ovos/skills/ovos-skill-http-demo

# Install Python deps and the skill itself (registers entry point)
RUN pip install --no-cache-dir -r /opt/ovos/skills/ovos-skill-http-demo/requirements.txt && \
    pip install --no-cache-dir /opt/ovos/skills/ovos-skill-http-demo

WORKDIR /opt/ovos/skills/ovos-skill-http-demo

# Match setup.py SKILL_ID (without “skill-” prefix)
ENTRYPOINT ["ovos-skill-launcher", "ovos-skill-http-demo.meminn"]
