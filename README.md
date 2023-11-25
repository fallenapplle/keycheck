# API Key Checker

## Overview

This script checks the validity of API keys for various services, such as Google Maps and ReCAPTCHA. It provides a convenient way to verify that your API keys are working correctly.

## Features

- **Google Maps API Key Check:** Verifies the status of a Google Maps API key by making requests to various Google Maps API endpoints.

- **ReCAPTCHA API Key Check:** Allows testing of ReCAPTCHA API keys by sending a ReCAPTCHA response to the ReCAPTCHA verification endpoint.

## Prerequisites

- Python 3.x installed on your machine.

## Usage

### Key Check

To check a  API key, run the following command:

```bash
python3 keycheck.py -api-key --type <your key type (recaptcha or google_maps)>  -v 
