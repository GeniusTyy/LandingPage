# Simple Email Collection Landing Page with Python and Flask

## Overview

This repository contains a simple landing page developed using Python and Flask for the purpose of collecting email addresses. The project is designed to be a straightforward solution for creating a sign-up form and storing collected email data in a database.

## Features

- **User-Friendly Interface**: The landing page provides a clean and user-friendly interface for visitors to submit their email addresses.
- **Data Storage**: Collected email addresses are stored securely in a database for future reference.
- **Easy Integration**: The project is built with Flask, making it easy to integrate with other Flask applications or deploy on various platforms.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python (version 3.6 or higher)
- Flask (install using `pip install flask`)
- SQLite (for the default database; can be customized to other databases)

## Setup and Run

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navigate to the project directory:

    ```bash
    LandingPage
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and visit [http://localhost:5000](http://localhost:5000) to access the landing page.

## Configuration

- The default configuration uses SQLite for data storage. You can customize the database configuration in the `config.py` file.
- Modify the HTML templates in the `templates` directory to match your branding and design preferences.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note**: Update the placeholders such as `seu-usuario` e `nome-do-repositorio` with your GitHub username and repository name.
