def decorator(fun):
    def wrapper():
        print("Validating auth")
        print("Checking rate limits")
        print("Logging request")
        fun()
        print("Processing request")

    return wrapper


@decorator
def handle_request():
    print("Handling the core request")


def main():
    handle_request()


if __name__ == "__main__":
    main()
