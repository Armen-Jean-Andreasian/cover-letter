import time
import base64
from source import CoverLetterGenerator
import streamlit as st


def get_base64_image(image_path: str):
	with open(image_path, "rb") as img_file:
		return base64.b64encode(img_file.read()).decode()


def st_color_picker(text: str) -> tuple:
	def hex_to_rgb(hex_value):
		hex_value = hex_value.lstrip('#')
		rgb = tuple(int(hex_value[i:i + 2], 16) for i in (0, 2, 4))
		return rgb

	hex_color: str = st.color_picker(text)
	return hex_to_rgb(hex_color)


def st_text_input(text: str) -> str:
	return st.text_input(text).strip()


def compare_chosen_colors(background_color: tuple, text_color: tuple):
	if background_color == text_color:
		st.error("The selected text and background colors are too similar.")
		return False
	else:
		bg_r, bg_g, bg_b = background_color
		text_r, text_g, text_b = text_color
		# calculating color difference with Euclidean distance
		color_diff = ((bg_r - text_r) ** 2 + (bg_g - text_g) ** 2 + (bg_b - text_b) ** 2) ** 0.5
		similarity_threshold = 50

		if color_diff < similarity_threshold:
			st.warning("The background and text colors appear to be quite similar, "
			           "which may result in a less satisfying outcome.")
			return False
		return True


image_base64 = get_base64_image("resources/binaries/cover.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{image_base64}");
background-size: 130%;
}}
</style>
"""

st.set_page_config(page_icon="resources/binaries/icon.png")
st.markdown(page_bg_img, unsafe_allow_html=True)

applicant_name = st_text_input("Enter your full name: ")
hr_name = st_text_input("HR name: ")
company = st_text_input("Enter the company name: ")
position = st_text_input("Enter the position you're applying for:")
email = st_text_input("Enter your email address: ")
phone = st_text_input("Enter your phone number: ")
website = st_text_input("Enter your website URL for a QR code:")
custom_body_text = st_text_input("Enter custom body message (optional):")

background_color = st_color_picker("Pick the background color for the cover letter.")
text_color = st_color_picker("Pick the cover letter text color.")


generate_button = st.button("Generate!")

if generate_button:
	cover_letter = CoverLetterGenerator(applicant_name=applicant_name,
	                                    hr_name=hr_name,
	                                    email=email,
	                                    phone=phone,
	                                    company=company,
	                                    position=position,
	                                    website=website,
	                                    background_color=background_color,
	                                    text_color=text_color,
	                                    custom_body_text=custom_body_text
	                                    )

	if compare_chosen_colors(background_color, text_color):

		cover_letter.generate()

		filepath = cover_letter.full_file_path

		time.sleep(1)

		with open(filepath, 'rb') as file:
			content = file.read()

			st.download_button(
				label="Download Cover Letter",
				data=content,
				file_name="cover_letter.pdf",
				mime="application/pdf"
			)
