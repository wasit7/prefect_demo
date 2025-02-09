from prefect import flow

@flow
def hello_flow():
    print("Hello, DIS321: Big Data Infrastructure!")

if __name__ == "__main__":
	hello_flow()
