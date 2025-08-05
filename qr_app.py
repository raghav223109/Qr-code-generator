import streamlit as st
import qrcode
from io import BytesIO

# Streamlit app title
st.title("🔗 QR Code Generator")
st.write("Enter a URL or any text below to generate its QR Code.")

# User input
url = st.text_input("Enter URL or text")

# Generate QR when button is clicked
if st.button("Generate QR Code"):
    if url.strip() == "":
        st.warning("Please enter a valid URL or text.")
    else:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Get image and convert to a compatible format
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # Display QR code
        st.image(qr_img, caption="Generated QR Code", use_column_width=True)

        # Convert image to BytesIO for download
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)

        # Download button
        st.download_button(
            label="📥 Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
