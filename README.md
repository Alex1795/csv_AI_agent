# CSV AI agent

A lightweight AI agent that analyzes CSV data through natural language queries using LangChain and Ollama. The agent converts your questions into data operations and provides human-readable answers. 

## Dataset
The demo uses a car price dataset containing vehicle characteristics and prices.
Dataset source: [Car Price Dataset on Kaggle](https://www.kaggle.com/datasets/asinow/car-price-dataset)

## Sample usage

It can answer questions such as: 

### Question: 
I want an electric car, which models can I get?

### Answer: 
The electric car models available are Audi Q5, Honda Civic, Kia Sportage, Hyundai Elantra, Volkswagen Tiguan.

### Question: 
I'm looking for a car brand chevrolet or ford, what are my model options and what is the average price?
### Answer: 
The car models from Chevrolet or Ford are ['Malibu', 'Equinox'
, 'Explorer', 'Impala'
, 'Fiesta'
, 'Focus'] and the average price is approximately

## Setup and Configuration
The default configuration uses the Llama 3.2 model via Ollama, but you can easily switch to any LLM supported by LangChain:
- Local models through Ollama
- Cloud-based models
- Other LangChain-compatible models

## Future Improvements
- Support for multiple CSV files
- Data visualization capabilities
