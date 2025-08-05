import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("🔗 QR Code Generator")

# User input for the link
url = st.text_input("Enter the URL to generate QR Code:")

# Button to generate
if st.button("Generate QR Code") and url:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Display the image in Streamlit
    st.image(img, caption="Generated QR Code", use_column_width=True)

    # Download option
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    st.download_button(
        label="📥 Download QR Code",
        data=buffer.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
