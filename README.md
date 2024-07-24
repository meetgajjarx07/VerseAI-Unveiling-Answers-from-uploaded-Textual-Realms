# VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms


```markdown
# VerseAI: Unveiling Answers from Uploaded Textual Realms

VerseAI is an intelligent chatbot that leverages advanced large language models (LLMs) to provide answers based on the content of uploaded text files. Users can upload various text files and ask questions, to which VerseAI will respond by analyzing the uploaded content.

## Features

- **Supports Multiple File Types**: Upload text files in formats such as TXT, PDF, DOCX, PPTX, XLSX, and more.
- **Advanced Embeddings**: Uses the `BAAI/bge-large-en-v1.5` model from HuggingFace for generating embeddings.
- **Powerful LLM**: Leverages `llama3-70b-8192` from Groq for answering questions.
- **Streamlit Interface**: User-friendly interface for uploading files and asking questions.
- **Respectful Responses**: Answers questions in a polite and respectful manner.

## Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Python 3.8 or later

## Installation

To run this project, you need to have Conda installed. Follow these steps to set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/verseai.git
    cd verseai
    ```

2. **Create a Conda environment**:
    ```bash
    conda create -n verseai python=3.8
    conda activate verseai
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add your Groq API Key**:
    Replace `'ADD YOUR GROQ API KEY'` in the `load_llm` function in `main.py` with your actual Groq API key.

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run main.py
    ```

2. **Upload Files**: Use the file uploader to select and upload your text files.

3. **Ask Questions**: Type your question in the text input box and receive answers based on the content of your uploaded files.

## Project Structure

- **main.py**: Contains the main application logic and Streamlit interface.
- **doc_em.py**: Handles loading and processing of documents, including splitting text and generating embeddings.

## Example

Here's a brief example to get you started:

1. Start the Streamlit app:
    ```bash
    streamlit run main.py
    ```

2. Upload your text files (e.g., PDF, DOCX).

3. Enter a question in the text input box.

4. Get a response based on the uploaded files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Enjoy using VerseAI! Let the answers to your inquiries be unveiled from your textual realms.
```

Additionally, you'll need a `requirements.txt` file to list the dependencies. Here's a basic example:

```plaintext
streamlit
langchain
huggingface_hub
chroma
```

Ensure to include any other dependencies your project requires. Adjust the versions as necessary for compatibility.
