from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/wasit7/prefect_demo.git",
        entrypoint="01_hello/flow.py:hello_flow",
    ).deploy(
        name="remote-deployment",
        parameters={
            'name': 'DSI: Big Data Infrastructure'
        },
        work_pool_name="default-agent-pool",
        cron="* * * * *",  # Run every munite
    )