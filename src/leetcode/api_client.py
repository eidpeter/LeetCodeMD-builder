import requests
import json


class LeetCodeAPIClient:
    """
    A class for interacting with the LeetCode GraphQL API
    """

    def __init__(self, cookie, base_url="https://leetcode.com/graphql"):
        """Initialize a new instance of the LeetCodeAPIClient class with the base GraphQL URL
        Parameters
        ----------
        base_url : String
            The base URL for the LeetCode GraphQL API
        cookie : String
            The cookie to use for authentication
        """
        self.base_url = base_url
        self.cookie = cookie

    def send_query(self, query):
        """Send a GraphQL query to the LeetCode API

        Parameters
        ----------
        query : String
            The GraphQL query

        Returns
        -------
        dict
            The JSON response from the API

        """

        headers = {
            "Cookie": self.cookie,
            "Content-Type": "application/json",
        }

        response = requests.post(
            self.base_url,
            json=query,
            headers=headers,
        )

        if response.status_code != 200:
            raise Exception(
                f"Query failed with status code {response.status_code}: {response.text}"
            )

        result = response.json()
        if "errors" in result:
            raise Exception(f"API returned errors: {result['errors']}")

        return result["data"]
