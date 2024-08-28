# HTTPX Async Client with Concurrency Control

This project demonstrates how to use the `httpx` library in Python to perform asynchronous HTTP requests with concurrency control. The example limits the number of concurrent requests to 50 at a time using a semaphore.

## Features

- Uses `httpx` for asynchronous HTTP requests.
- Limits concurrent requests to a maximum of 50 using a semaphore.
- Measures and prints the total number of requests and time elapsed.

## Package Manager

This project uses [PDM](https://pdm.fming.dev/) as the package manager.

## Installation and Setup

### Prerequisites

- [PDM](https://pdm.fming.dev/) installed (for managing Python packages).

#### 1. Clone the repository:
   ```bash
   git clone https://github.com/patsaid/httpx-async-pooling.
   cd httpx-concurrency-example
   ```

#### 2. Install the required Python packages:
   ```bash
   pdm install
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for the full text of the license.

## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements!