<div align="center">
<h1 align="center">VerseAI: Unveiling Answers from Uploaded Textual Realms</h1>

[![Languages][language-shield]][language-url]
[![Contributors][contri-shield]][contri-url]
[![Size][size-shield]][size-url]
[![Issues][issues-shield]][issues-url]


</div>

## About The Project

https://github.com/user-attachments/assets/3c2dd89c-7436-495e-93a4-1dbad709491d

VerseAI is an intelligent chatbot that leverages advanced large language models (LLMs) to provide answers based on the content of uploaded text files. Users can upload various text files and ask questions, to which VerseAI will respond by analyzing the uploaded content.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [HuggingFace](https://huggingface.co/)
* [Groq](https://groq.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites

Make sure that you have the following:
- [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Python 3.8 or later

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms.git
    cd verseai
    ```

2. **Create a Conda environment**:
    ```sh
    conda create -n verseai 
    conda activate verseai
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Add your Groq API Key**:
    Replace `'ADD YOUR GROQ API KEY'` in the `load_llm` function in `main.py` with your actual Groq API key.

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run main.py
    ```

2. **Upload Files**: Use the file uploader to select and upload your text files.

3. **Ask Questions**: Type your question in the text input box and receive answers based on the content of your uploaded files.

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Structure

- **main.py**: Contains the main application logic and Streamlit interface.
- **doc_em.py**: Handles loading and processing of documents, including splitting text and generating embeddings.

<p align="right">(<a href="#top">back to top</a>)</p>

## Example

Here's a brief example to get you started:

1. **Start the Streamlit app**:
    ```sh
    streamlit run main.py
    ```

2. **Upload your text files (e.g., PDF, DOCX).**

3. **Enter a question in the text input box.**

4. **Get a response based on the uploaded files.**

<p align="right">(<a href="#top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>

[contri-shield]: https://img.shields.io/github/contributors/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms?style=for-the-badge
[contri-url]: https://github.com/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms/graphs/contributors
[size-shield]: https://img.shields.io/github/repo-size/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms?style=for-the-badge
[size-url]: https://github.com/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms
[issues-shield]: https://img.shields.io/github/issues/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms?style=for-the-badge
[issues-url]: https://github.com/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms/issues
[language-shield]: https://img.shields.io/github/languages/count/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms?style=for-the-badge
[language-url]: https://github.com/meetgajjarx07/VerseAI-Unveiling-Answers-from-uploaded-Textual-Realms


