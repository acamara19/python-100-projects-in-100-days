import requests
import json
import html


def fetch_data(api_url):
    """Fetch data from the specified API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def save_data(data, file_path):
    """Save the formatted data to a Python file, after cleaning and removing unwanted keys."""
    if "results" in data:
        questions = data["results"]
        cleaned_questions = []
        for question in questions:
            # Correcting HTML entities and other grammar issues in the question text.
            question['question'] = html.unescape(question['question']).replace("&#039;", "'").replace("&quot;", '"')
            # Remove unwanted keys within each question, if any (for demonstration, assuming none needed)
            cleaned_questions.append(question)

        with open(file_path, 'w') as file:
            file.write("question_data = ")
            json.dump(cleaned_questions, file, indent=4)


def main(api_url, output_file):
    """Main function to fetch data and save it."""
    data = fetch_data(api_url)
    if data is not None:
        save_data(data, output_file)


if __name__ == "__main__":
    API_URL = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=boolean"  # Replace with your actual API URL
    OUTPUT_FILE = "data.py"
    main(API_URL, OUTPUT_FILE)
