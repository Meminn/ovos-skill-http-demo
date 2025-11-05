# -----------------------------
# Dockerfile for ovos-skill-http-demo
# -----------------------------
FROM docker.io/smartgic/ovos-skill-base:stable

# Copy skill source into the standard skills dir
COPY . /opt/ovos/skills/ovos-skill-http-demo

# Install the skill's Python deps
RUN pip install --no-cache-dir -r /opt/ovos/skills/ovos-skill-http-demo/requirements.txt

# Work from the skill folder (optional)
WORKDIR /opt/ovos/skills/ovos-skill-http-demo

# IMPORTANT: skill id must match your setup.py SKILL_ID
# Your setup.py makes SKILL_ID: "ovos-skill-http-demo.meminn"
# ovos-skill-launcher convention is: `skill-<SKILL_ID>`
ENTRYPOINT ["ovos-skill-launcher", "skill-ovos-skill-http-demo.meminn"]
