<h1 align="center" id="title">Review Sentiment Analyzer</h1>

<p id="description">The Review Sentiment Analyzer project is focused on developing a Python-based API to analyze customer reviews. It utilizes sentiment analysis powered by a Large Language Model (LLM) to return structured results, categorizing reviews into positive, negative, and neutral sentiments.</p>

<!--<h2>🚀 Documentation</h2>-->

<!--[Postman-documentation](https://www.postman.com)-->

  
<h2>🛠️ Installation Steps:</h2>

1. Clone the repository:

```CMD
git clone https://github.com/aditya-Kumar421/Sentiment_Analysis
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install and Create a virtual environment:

```CMD
python -m venv env
```

3. Activate the virtual environment

```CMD
env\Scripts\activate
cd reviews_analyzer
```

4. Install the dependencies:

```CMD
pip install -r requirements.txt
```

5. Set Up Database:

```
python manage.py migrate
```

6. Run the Development Server:

```
python manage.py runserver
```

7. Access the Endpoints:

```
http://127.0.0.1:8000/api/analysis/
```

<h2>🍰 Contribution Guidelines:</h2>

Please contribute using GitHub Flow. Create a branch add commits and open a pull request
