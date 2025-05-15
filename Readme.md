# Real-Time News Fetcher

A simple Streamlit application that lets you fetch and display the latest news articles by topic in real time, using DuckDuckGo search.

## Features

* Select a news topic from a dropdown menu.
* Fetch up to 5 of the most recent articles for the selected topic.
* Display article titles, URLs, and summaries in expandable sections.
* Show timestamp of the most recent fetch.

## Prerequisites

* Python 3.7 or higher
* [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone this repository (or download `new.py` directly):

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install streamlit duckduckgo-search
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run new.py
   ```

2. In your browser, navigate to the local URL provided (usually [http://localhost:8501](http://localhost:8501)).

3. Select a news topic from the dropdown menu.

4. Click **Fetch News** to retrieve and display the latest articles.

## Configuration

* **Topics**: By default, the app fetches news under the following categories:

  ```python
  topics = ["Technology", "Politics", "Sports", "Entertainment", "Business"]
  ```

  Feel free to modify or extend this list in `new.py`.

* **Results Limit**: The app fetches up to 5 articles. Adjust `max_results` in the `search_news` function if you need more or fewer.

## Project Structure

```
├── new.py        # Streamlit app source code
└── README.md     # Project documentation
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Happy news fetching!*
