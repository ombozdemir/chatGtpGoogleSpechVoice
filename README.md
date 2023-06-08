

# Voice Chat with ChatGPT

This is a Python script that converts audio from the microphone to text using the Google Speech API and then processes the text with the ChatGPT API. With this script, you can interact with ChatGPT using voice and receive responses.

## Prerequisites

To run this script, the following prerequisites need to be fulfilled:

- Python 3.7 or a newer version
- The `google-cloud-speech` Python library installed. You can install it using the following command:
    ```
    pip install google-cloud-speech
    ```
- The `openai` Python library installed. You can install it using the following command:
    ```
    pip install openai
    ```

## Project Setup

1. Clone this project from GitHub or download it as a ZIP file.

2. Navigate to the project folder and install the required Python packages by running the following command:
    ```
    pip install -r requirements.txt
    ```

3. You need to have an API key to access the OpenAI API. Sign up for the OpenAI API and obtain an API key.

4. Update the `OPENAI_API_KEY` variable in the `main.py` file to use your obtained API key.

## Usage

1. Open a terminal and navigate to the project folder.

2. Start the script by running the following command:
    ```
    python main.py
    ```

3. When the script is running, the microphone will become available. When you speak, the script will use the Google Speech API to convert it to text and interact with ChatGPT to receive a response.

4. The script will query the ChatGPT API and read the response aloud each time it receives input.

5. Press `Ctrl+C` to exit.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Create a branch for this repository.

2. Make your changes in this branch.

3. Submit a pull request and explain your changes.

## License

This project is licensed under the MIT License.
