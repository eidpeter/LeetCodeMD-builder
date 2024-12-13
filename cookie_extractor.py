import json
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def transform_to_json(cookie_string, output_file):
    """
    Transforms a cookie string into a JSON file with the specified format.

    Parameters:
        cookie_string (str): The input string containing cookies in 'key=value;' format.
        domain (str): The domain to associate with each cookie.
        path (str): The path to associate with each cookie.
        output_file (str): The file path where the JSON output will be saved.
    """
    # Split the input string into individual key-value pairs
    pairs = cookie_string.split(";")

    # Transform into the desired JSON structure
    result = []
    for pair in pairs:
        if "=" in pair:  # Ensure the pair has a valid format
            name, value = pair.split("=", 1)
            result.append(
                {
                    "name": name.strip(),
                    "value": value.strip(),
                    "domain": ".leetcode.com",
                    "path": "/",
                }
            )

    # Save as JSON file
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"JSON saved to {output_file}")


def main():
    # Example input data
    cookie_string = os.getenv("LEETCODE_COOKIES")

    domain = ".leetcode.com"
    path = "/"
    output_file = "cookies.json"

    # Transform the string into JSON and save it
    transform_to_json(cookie_string, output_file)


if __name__ == "__main__":
    main()
