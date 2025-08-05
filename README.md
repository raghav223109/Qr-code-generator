# Qr-code-generator
This is a simple yet powerful QR Code Generator built using Python, Streamlit, and qrcode. It allows users to input any URL, generate a QR code for it instantly, view it on the page, and download it as a .png file.

User Input: Enter any valid URL into the text box.

QR Code Generation: Dynamically generates a high-quality QR code.

Preview: Displays the generated QR code image on the web page.

Download Button: Allows you to download the QR code as a PNG file.

Browser-Based Interface: Runs entirely in your browser with Streamlit — no additional UI code needed.

# Tech Stack
 
🧠 Programming Language
Python – Core language used to build the backend logic for QR generation and UI control.

📦 Libraries / Frameworks
1. Streamlit
Used to build the web interface and run the app in a browser.

Enables interactive widgets, file downloads, and image display.

2. qrcode
Generates QR codes from text or URLs.

Offers error correction and customization options.

3. Pillow (PIL)
Python Imaging Library used for converting and handling image data (like converting to PNG format).

Required for displaying and downloading images.

4. [io (Standard Library)]
Used for in-memory file operations via BytesIO to support image downloads without saving to disk.

💻 IDE (Optional but Recommended)
PyCharm or VS Code – for writing and testing the Python code efficiently.

🌐 Execution Environment
Run locally using:
streamlit run qr_app.py
