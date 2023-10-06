# Survey Backend

![GitHub issues](https://img.shields.io/github/issues/shafa45/survey-backend)
![GitHub forks](https://img.shields.io/github/forks/shafa45/survey-backend)
![GitHub stars](https://img.shields.io/github/stars/shafa45/survey-backend)

## Description

This repository contains the backend code for a survey application. It's built with Flask and uses Firebase for data storage.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/shafa45/survey-backend.git
```

2. Navigate to the project directory:
```bash
cd survey-backend
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

4. Copy the `.env.example` file and create a new `.env` file:
```bash
cp .env.example .env
```

5. Update the `.env` file with your Firebase credentials.

## Running the Application

To run the application, use the following command:
```bash
flask run
```

## Usage

This application provides a backend for a survey system. It exposes several endpoints for creating, retrieving, updating, and deleting surveys.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)