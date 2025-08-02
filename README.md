# Excalibur: AI Infrastructure Backend

Backbone for the hybrid AI system integrating Mixtral 8x22B (local) and Grok 4 (API), with persistent memory and OS tools.

## Setup
- Install dependencies: `pip install -r requirements.txt`
- Start Ollama: `ollama serve`
- Pull Mixtral: `ollama pull mixtral:8x22b`
- Generate protobuf (if using gRPC): Run `generate_proto.ps1`
- Run server: `python excalibur/server/excalibur_server.py`
- Run tests: `pytest excalibur/test/`

## Deployment
- Build Docker image: `docker build -t excalibur .`
- Deploy to Fly.io: `fly deploy`
