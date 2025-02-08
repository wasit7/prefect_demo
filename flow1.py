from prefect import flow

@flow
def my_flow():
    print("Hello, Prefect!")

if __name__ == "__main__":
    my_flow.deploy(
        name="my-first-deployment",
        work_pool_name="default-agent-pool",
        # image="my-image",
        push=False,
        cron="* * * * *",
    )
