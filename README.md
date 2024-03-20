# Pasting-By-Python

This is a simple web application that allows you to paste the contents of a file and generate a unique URL for accessing the pasted file. The application is built using Python and Flask.

## Features

- Paste the contents of a file and generate a unique URL
- Access the pasted file using the generated URL
- Simple and intuitive user interface
- Tested successfully on macOS and Linux

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Flask (Python web framework)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/inabakumori/pasting-by-python
   ```

2. Navigate to the project directory:

   ```
   cd pasting-by-python
   ```

3. Install the required dependencies:

   ```
   pip install flask
   ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the project directory:

   ```
   cd pasting-by-python
   ```

3. Run the application:

   ```
   python app.py paste.py
   ```

   Replace `paste.py` with the path to the file you want to paste.

4. The application will generate a unique URL for accessing the pasted file. The URL will be displayed in the terminal.

5. Open a web browser and visit the generated URL to view the pasted file.

   Example URL: `http://localhost:55554/paste/1234567890`

6. If you are running the application on a local machine, you can also access the pasted file using the local IP address. The local IP address will be displayed in the terminal if available.

   Example local URL: `http://192.168.0.10:55554/paste/1234567890`

   Note: If you are behind a NAT (Network Address Translation), you may need to use the local IP address to access the pasted file.

7. The pasted files will be stored in the `uploads` directory within the project.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Author

- [inabakumori](https://github.com/inabakumori)

## Acknowledgements

- This application was built using the Flask web framework.
- The code for generating unique filenames and handling file uploads was inspired by various online resources.

## Disclaimer

This application is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any misuse or damage caused by this application.

---
