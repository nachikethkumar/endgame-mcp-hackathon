# Implementation Guide

## Architecture

The architecture of the Crypto News Scraper is designed to leverage the MASA API for scraping the latest cryptocurrency news. It is split into two main components:

1. **Server**: This is an asynchronous service that communicates with the MASA API to retrieve the latest news related to a specified cryptocurrency. The server is built using the `FastMCP` framework and handles client requests to fetch the relevant data. It integrates MCP tools for efficient interaction with the MASA API and provides a response in the form of news articles.

2. **Client**: The client is a terminal-based application that allows the user to query the server by providing a cryptocurrency name. It sends the request to the server and returns the latest news articles based on the user's input.

Both components work together in a client-server model, where the client sends the request and the server handles the logic of fetching data from the MASA API and returning it.

## Components

1. **Server**:
   - Built using the `FastMCP` framework.
   - Handles HTTP requests to interact with the MASA API.
   - Provides tools to search for the latest news about a given cryptocurrency using the MASA API.
   - Uses asynchronous calls to ensure non-blocking operations.

2. **Client**:
   - Terminal-based application that allows the user to enter the name of a cryptocurrency.
   - Sends the request to the server for the latest news.
   - Displays the news articles returned by the server.

3. **MASA API**:
   - Used for scraping the latest cryptocurrency news.
   - Provides an endpoint to fetch the latest news based on a keyword (cryptocurrency name).
   - Provides structured data that the server processes and sends to the client.

## Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-repo-name/crypto-news-scraper.git
cd crypto-news-scraper
```

### 2. **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. **Install Dependencies**

Install the required dependencies:

```bash
pip install aiohttp requests python-dotenv mcp
```

### 4. **Create a `.env` File**

Create a `.env` file in the project root and add your MASA API key and base URL:

```
MASA_DATA_API_KEY=your_api_key_here
MASA_BASE_URL=https://data.dev.masalabs.ai
```

### 5. **Run the Server**

Run the server using FastMCP:

```bash
python server.py
```

The server will be up and running to process requests from the client.

## Usage

Once the server is running, you can use the client to query the server for the latest cryptocurrency news.

1. **Run the Client**:

The client can be executed via the terminal. For example:

```bash
python client.py "Bitcoin"
```

This will send a request to the server for the latest news articles related to "Bitcoin."

2. **Response**:

The client will display a list of the latest news articles related to the specified cryptocurrency.

## Performance

- **Asynchronous Execution**: The server utilizes asynchronous programming to make non-blocking API calls to the MASA API, enabling the system to handle multiple requests efficiently.
- **Scalability**: The system is designed to be scalable, able to process numerous requests concurrently, making it suitable for production use.
- **Latency**: The performance of news retrieval is dependent on the MASA API's response time, which can be influenced by network conditions and API load.

## Testing

### Approach

Testing focuses on ensuring that the system functions as expected and that the server can successfully retrieve the latest news for a given cryptocurrency.

1. **Unit Tests**:
   - Mock MASA API responses to test the server’s handling of data.
   - Verify that the server correctly processes valid and invalid queries.
   
2. **Integration Tests**:
   - Test the interaction between the client and server to ensure that the correct data is returned from the MASA API.

3. **Performance Tests**:
   - Load test the server to ensure it can handle a large number of requests without degradation.
   - Test response times to measure how quickly the system retrieves and returns data for various cryptocurrencies.

