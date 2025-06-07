import multiprocessing
import uvicorn
import sys


def run_api():
    uvicorn.run("v1.src.api.rest.lifespan:app", host="0.0.0.0", port=8000)


def main():
    sys.path.insert(0, "C:/Users/ramaz/Development/PetProjects/testarch")

    api_proc = multiprocessing.Process(target=run_api)
    api_proc.start()

    try:
        print("Entrypoint: Both processes started. [Ctrl+C to exit]")
        api_proc.join()
    except KeyboardInterrupt:
        print("Entrypoint: SIGINT received, terminating children.")
        api_proc.terminate()
        api_proc.join()
        print("Entrypoint: Shutdown complete.")
        sys.exit(0)


if __name__ == "__main__":
    main()
