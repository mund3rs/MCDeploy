# Minecraft Server Deployment App

This Python application leverages the AWS Python SDK Boto3 and Streamlit to deploy a Minecraft server on an AWS t3.medium EC2 instance. Users can add their email address, select 'Deploy', and receive the server's IP via email to connect through their Minecraft client.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

The project provides a user-friendly interface (built with Streamlit) to facilitate the deployment of a Minecraft server on an AWS EC2 instance. Upon user input (email address and 'Deploy' action), the application provisions the EC2 instance, installs the Minecraft server, and then emails the user the server's IP for connection.

## Features

- Streamlit-based frontend for user interaction.
- Boto3 integration to manage AWS resources.
- Automatic provisioning and setup of a Minecraft server.
- Email notification of the server IP to the user.

## Prerequisites 

- Minecraft client needs to be running version 18.2
- AWS account, to avoid charges use t3.micro instance type in the config.ini. Performance on t3.micro is fine for upt to 3 players.
- Create AWS Image with minecraft server set to auto run at start up

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mund3rs/MCDeploy.git

2. Create and navigate to the project directory:

    ```bash
    mkdir minecraft-server-app
    cd minecraft-server-app

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up AWS credentials with Boto3

    Ensure you have configure AWS credentials (access key, secret key) with the appropriate permissions. Refer to the AWS documentation on how to set up and configure AWS credentials.

5. Complete configuration.ini

## Usage

1. Run the Streamlit app:
    
    ```bash
    streamlit run home.py

2. Access via the provided URL (usually http://localhost:8501) in you browser

3. Enter your email address in the field provided and select 'Launch'

4. You should recieve an email with the EC2 public IPv4 once the server is up

## Contributing

Contributions are welcome. This was just a simple app to get to know the basics of Boto3. Please follow the below guidelines if you wish to contribute.

- Fork the repository
- Create a new branch
- Make your changes
- Test your changes
- Submit a pull request

## License

This project is licensed under the MIT license see license.txt

## Acknowledgments

- Boto3 - AWS SDK for Python
- Streamlit - Python library for creating web apps