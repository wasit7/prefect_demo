from prefect import flow
from pathlib import Path

# Define your entrypoint (e.g., "register_prefect_flow.py:run_kedro_pipeline")
entrypoint = f"flow.py:hello_flow"
source=str(Path.cwd())
print(f'entrypoint:{entrypoint}, source:{source}')
if __name__ == "__main__":
    flow.from_source(
        source=source,
        entrypoint=entrypoint,
    ).deploy(
        name="local_deployment",
        parameters={
            'name': 'DSI: Big Data Infrastructure'
        },
        work_pool_name="default-agent-pool",
        cron="* * * * *",  # Run every munite
    )