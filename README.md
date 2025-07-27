## NINA - Nice Intelligent Network Assistant

🤖 **Nice Intelligent Network Assistant (NINA)** is a modern AI-driven customer support chatbot framework.  
Powered by **intent recognition**, NINA enables businesses to automate and streamline customer interactions across platforms with ease.

---

<p align="center">
  <a href="https://github.com/crispengari/nina/actions/workflows/ci.yml">
    <img src="https://github.com/crispengari/nina/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  </a>
   <a href="https://github.com/crispengari/nina/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/language-python-blue.svg" alt="Language: Python">
  </a>
</p>

NINA supports seamless integration through **REST** and **GraphQL APIs**.

---

## Dataset

The dataset used to train the model was obtained from Kaggle:  
[Chatbot Intent Classification Dataset](https://www.kaggle.com/datasets/sahideseker/chatbot-intent-classification-dataset)

---

## Tech Stack

- **Ariadne** (GraphQL)
- **Flask** (REST API)
- **PyTorch** (Deep Learning)
- **Python** (Core programming language)

---

## Features

- **AI-driven intent classification** for customer messages.
- **Multi-language detection** (supports language code in response).
- **REST and GraphQL APIs** for flexible communication.
- **Pre-trained model** for quick setup.
- **Integration-ready** for customer support platforms.

---

## API Usage

### Get Meta Data (REST)

Send a GET request to:

```
http://127.0.0.1:3001/
```

**Response:**

```json
{
  "description": "Nice Intelligent Network Assistant (NINA) is a modern customer support chatbot framework powered by AI-driven intent recognition. Nina provides seamless integration through REST and GraphQL APIs, enabling businesses to automate and streamline customer interactions across platforms.",
  "language": "python",
  "libraries": ["pytorch", "googletrans"],
  "main": "Nice Intelligent Network Assistant (NINA)",
  "programmer": "@crispengari"
}
```

### Get Meta Data (GraphQL)

Make a query to:

```
http://127.0.0.1:3001/api/v1/graphql
```

**Query Example:**

```graphql
fragment MetaFragment on Meta {
  programmer
  main
  description
  language
  libraries
}

query Meta {
  meta {
    ...MetaFragment
  }
}
```

**Response:**

```json
{
  "data": {
    "meta": {
      "description": "Nice Intelligent Network Assistant (NINA) is a modern customer support chatbot framework powered by AI-driven intent recognition. Nina provides seamless integration through REST and GraphQL APIs, enabling businesses to automate and streamline customer interactions across platforms.",
      "language": "python",
      "libraries": ["pytorch", "googletrans"],
      "main": "Nice Intelligent Network Assistant (NINA)",
      "programmer": "@crispengari"
    }
  }
}
```

---

## Communicating with the Bot

### REST POST Request

Send a POST request to:

```
http://127.0.0.1:3001/api/v1/ask
```

**Request Body:**

```json
{
  "message": "Rhoxisa umrhumo wam, nceda."
}
```

**Response:**

```json
{
  "language": "xh",
  "prediction": {
    "predictions": [
      { "class": "business_hours", "label": 0, "probability": 0.0012478231 },
      { "class": "cancellation", "label": 2, "probability": 0.8154424428 },
      { "class": "order_status", "label": 4, "probability": 0.1550436467 }
    ],
    "top": {
      "class": "cancellation",
      "label": 2,
      "probability": 0.8154424428
    }
  },
  "response": "Ukubhaliswa kokubhalwa kokubhalwa kunokucelwa ngeZiko loNcedo phantsi 'izicwangciso zam ". 🔓",
  "success": true
}
```

### GraphQL Mutation

Make a mutation request to:

```
http://127.0.0.1:3001/api/v1/graphql
```

**Mutation Example:**

```graphql
fragment PredictionFragment on Prediction {
  class
  label
  probability
}

mutation AskBot($input: AskBotInput!) {
  askBot(input: $input) {
    success
    lang
    prediction {
      top {
        ...PredictionFragment
      }
      predictions {
        ...PredictionFragment
      }
    }
  }
}
```

**Input Example:**

```json
{
  "input": {
    "message": "Rhoxisa umrhumo wam, nceda."
  }
}
```

---

## Getting Started Locally

### 1. Clone the Repository

```shell
git clone https://github.com/CrispenGari/nina
cd nina/api
```

### 2. Create a Virtual Environment

```shell
virtualenv venv
.\env\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

```shell
pip install -r requirements.txt
```

### 4. Run the Application

```shell
python app.py
```

> The default port is `3001`. You can change it in `app.py`.

### 5. Run Tests

```shell
pytest
```

---

## Training Notebook

The notebook used to train the user intent classification model can be found here:  
[17_SUBSCRIPTION_PLATFORM_CHATBOT/00_USER_INTENT.ipynb](https://github.com/CrispenGari/nlp-pytorch/blob/main/17_SUBSCRIPTION_PLATFORM_CHATBOT/00_USER_INTENT.ipynb)

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for details.
