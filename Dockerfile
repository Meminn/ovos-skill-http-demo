# -----------------------------
# Dockerfile for ovos-skill-http-demo
# -----------------------------
FROM docker.io/smartgic/ovos-skill-base:stable

# Ensure the ovos user owns the skill sources so pip can build the wheel
COPY --chown=ovos:ovos . /opt/ovos/skills/ovos-skill-http-demo

# deps + install the skill (registers entry point)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r /opt/ovos/skills/ovos-skill-http-demo/requirements.txt && \
    pip install --no-cache-dir --force-reinstall /opt/ovos/skills/ovos-skill-http-demo

WORKDIR /opt/ovos/skills/ovos-skill-http-demo

# Match your SKILL_ID (no "skill-" prefix since your setup.py doesn’t have it)
ENTRYPOINT ["ovos-skill-launcher", "ovos-skill-http-demo.meminn"]
