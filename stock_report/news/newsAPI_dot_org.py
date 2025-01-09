import requests
import os

class NewsAPI:
    BASE_URL = "https://newsapi.org/v2/"

    def __init__(self, api_key):
        """
        Initialize the NewsAPI class with the provided API key.
        """
        self.api_key = api_key

    def fetch_everything(self, **kwargs):
        """
        Fetch articles using the /v2/everything endpoint.
        
        :param kwargs: Dictionary of parameters to customize the request.
        :return: JSON response containing the search results.
        """
        return self._make_request("everything", kwargs)

    def fetch_top_headlines(self, **kwargs):
        """
        Fetch top headlines using the /v2/top-headlines endpoint.
        
        :param kwargs: Dictionary of parameters to customize the request.
        :return: JSON response containing the top headlines.
        """
        return self._make_request("top-headlines", kwargs)

    def advanced_query(self, base_query="", include=[], exclude=[], exact=False, logical=""):
        """
        Create an advanced query string for complex searches.
        
        :param base_query: Base keyword or phrase.
        :param include: List of keywords/phrases to include.
        :param exclude: List of keywords/phrases to exclude.
        :param exact: Whether to use an exact match for the base query.
        :param logical: Additional logical expressions (AND/OR/NOT).
        :return: A formatted query string.
        """
        query = f'"{base_query}"' if exact else base_query
        if include:
            query += " " + " ".join(f"+{word}" for word in include)
        if exclude:
            query += " " + " ".join(f"-{word}" for word in exclude)
        if logical:
            query += f" {logical}"
        return query

    def _make_request(self, endpoint, params):
        """
        Make a GET request to the specified endpoint with the provided parameters.
        
        :param endpoint: The endpoint to send the request to (e.g., "everything").
        :param params: Dictionary of query parameters for the request.
        :return: JSON response from the API.
        """
        url = self.BASE_URL + endpoint
        headers = {"X-Api-Key": self.api_key}
        valid_params = self._filter_params(endpoint, params)

        response = requests.get(url, params=valid_params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _filter_params(self, endpoint, params):
        """
        Filter parameters based on the endpoint-specific requirements.
        
        :param endpoint: The endpoint to send the request to (e.g., "everything").
        :param params: Dictionary of query parameters for the request.
        :return: Filtered parameters.
        """
        allowed_keys = {
            "everything": [
                "q", "searchIn", "sources", "domains", "excludeDomains",
                "from", "to", "language", "sortBy", "pageSize", "page"
            ],
            "top-headlines": [
                "country", "category", "sources", "q", "pageSize", "page"
            ]
        }
        return {key: params[key] for key in allowed_keys[endpoint] if key in params}


# # Example Usage
# if __name__ == "__main__":
#     # Replace with your actual API key
#     api_key = os.getenv("NEWS_DOT_ORG_API_KEY")
#     news_api = NewsAPI(api_key)

#     try:
#         # Fetching articles from /v2/everything
#         everything_response = news_api.fetch_everything(**{
#             "q": "indian stock market, BSE , NSE",
#             "language": "en",
#             "from": "2025-01-01",
#             "to": "2025-01-09",
#             "sortBy": "publishedAt",
#             "pageSize": 5
#             }
#         )
#         print("Everything endpoint results:")
#         for article in everything_response.get("articles", []):
#             # print(article.keys())
#             print(f"- {article['description']} ({article['content']})")

#         # Fetching top headlines from /v2/top-headlines
#         headlines_response = news_api.fetch_top_headlines(
#             country="us",
#             q="biden",
#             pageSize=5
#         )
#         print("\nTop headlines:")
#         for article in headlines_response.get("articles", []):
#             print(f"- {article['title']} ({article['source']['name']})")

#         # Advanced query example for /v2/everything
#         advanced_query = news_api.advanced_query(
#             base_query="technology",
#             include=["AI", "machine learning"],
#             exclude=["blockchain"],
#             exact=True,
#             logical="AND (AI OR ML)"
#         )
#         advanced_response = news_api.fetch_everything(q=advanced_query, language="en")
#         print("\nAdvanced query results:")
#         for article in advanced_response.get("articles", []):
#             print(f"- {article['title']} ({article['source']['name']})")

#     except Exception as e:
#         print("Error:", e)
