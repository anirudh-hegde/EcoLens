import google.generativeai as genai
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
	page_title="EcoLens", page_icon="🧿"
)

with st.sidebar:
	pages = option_menu("Go to",
						["Intro", "About", "Get started"]
						)
	API_KEY = st.sidebar.text_input("Enter your API Key "
									"(Get your Google Gemini API key from "
									"[here](https://makersuite.google.com/app/apikey)) : ",
									type="password")


def main():
	if pages == "Intro":
		st.snow()
		l, c, r = st.columns(3)
		with c:
			st.image("images/green.jpeg", width=240)
		
		st.subheader(":rainbow[Welcome to EcoLens]")
		st.write(
			"""
			**EcoLens** is a web app utilizing power of **Generative AI** by offering
			image uploads feature. In waste management, AI plays a critical role
			by introducing smart recycling solutions that enhance efficiency and
			sustainability.
			About 400 million tons of plastic waste are produced globally every
			year — so another 30 Eiffel Towers might seem like a drop in the ocean.
			But the United Nations has warned that if historic growth trends continue,
			that figure will almost treble to 1.1 billion tons in 2050.
			With the uploads feature, users can upload an image for
			detection, and the app will provide a caption beneath the uploaded
			picture whether it can be recyclable or garbage.
			"""
		)
		
		st.write(
			"""
				**1. AI-Powered Image Recognition for Waste Classification**:
				EcoLens utilizes AI to analyze uploaded images and classify
				them as either recyclable or garbage. This feature leverages
				generative AI capabilities to provide quick and accurate assessments
				of waste items.
				
				**2. Potential for Increased Recycling Rates**:
				By accurately identifying recyclable materials, EcoLens aims to enhance
				recycling rates. Higher-quality recycled materials can drive up overall
				recycling percentages, supporting sustainability goals.
				
				**3. Real-Time Decision Making for Users**:
				The app provides instant feedback on uploaded images, allowing users to
				make informed decisions about what can be recycled versus what should go
				in the trash. This real-time guidance helps reduce contamination and improves
				recycling practices.
				
				**4. Data-Driven Insights for Waste Management**:
				While not explicitly mentioned, EcoLens' image analysis could contribute to
				broader waste management strategies. By analyzing patterns in uploaded images,
				the app could generate insights about common recyclables, contamination rates,
				and other trends in local waste streams.
				
				**5. Contribution to Circular Economy Goals**:
				By empowering individuals to better identify and recycle materials,
				EcoLens supports the transition towards a circular economy. This aligns
				with global efforts to reduce plastic waste and promote sustainable consumption
				practices .
				<br><br>
			"""
		)
	
	elif pages == "About":
		st.write(
			"""
			<h3>
			<a href="https://www.unep.org/news-and-stories/press-release/world-must-move-beyond-waste-era-and-turn-rubbish-resource-un-report">
			<b>World must move beyond waste era and turn rubbish into resource: UN Report</b>
			</a>
			</h3>
			""", unsafe_allow_html=True
		)
		
		# waste=Image.open("images/waste.png")
		st.image("images/waste.png")
		st.write("""<br>""", unsafe_allow_html=True)
		st.subheader(":red[Key Findings]")
		
		st.write("""
                1. Municipal solid waste generation is predicted to grow from
                2.1 billion tonnes in 2023 to 3.8 billion tonnes by 2050.
                In 2020, the global direct cost of waste management was an
                estimated USD 252 billion. When factoring in the hidden costs
                of pollution, poor health and climate change from poor waste
                disposal practices, the cost rises to USD 361 billion.
                
                2. Without urgent action on waste management, by 2050 this global annual
                cost could almost double to a staggering USD 640.3 billion.
                The report’s modelling shows that getting waste under control by
                taking waste prevention and management measures could limit net annual
                costs by 2050 to USD 270.2 billion.

                3. However, projections show that a circular economy model, where waste generation
                and economic growth are decoupled by adopting waste avoidance, sustainable business
                practices, and full waste management, could in fact lead to a full net gain of
                USD 108.5 billion per year.
                
                We need to act now in order to avoid the worst scenario. The report provides
                guidance and suggested actions for Multinational development banks, national governments,
                municipalities, producers and retailers, the waste management sector as well as citizens.
                """, unsafe_allow_html=True
				 )
		
		st.write("""
                <span style="color:black" >
                With municipal waste set to rise by two thirds and its
                costs to almost double within a generation, only a drastic
                reduction in waste generation will secure a liveable and
                affordable future, according to a new United Nations Environment
                (Programme (UNEP) report).
                """, unsafe_allow_html=True)
	
	elif pages == "Get started":
		
		# to center the image
		l, c, r = st.columns(3)
		with c:
			st.image("images/glens.png", width=200)
		image_upload = st.file_uploader("Choose the image: ", type=["jpg", "jpeg", "png"])
		
		if image_upload:
			if st.button("Check Recyclability"):
				img = Image.open(image_upload)
				
				genai.configure(api_key=API_KEY)
				model = genai.GenerativeModel("gemini-1.5-flash")
				
				content_on_image = model.generate_content(
					["Classify the uploaded image as: "
					 "1) Recyclability: Is the material Recyclable or UnRecyclable? "
					 "Provide a confidence score (in percentage)."
					 "2) Presence of Harmful Chemicals: Identify harmful chemicals are present. "
					 "List them if possible and also provide a confidence score."
					 "3) Environmental Harm: How is this material harmful to the environment? "
					 "List 2-3 main impacts."
					 "4) Waste Management: Provide 4-5 suggestions on how to manage or dispose of "
					 "this material responsibly."
					 "Please provide the response in 5-6 points, with each classification and advice "
					 "supported by a confidence score.", img]
				)
				
				st.image(img)
				st.markdown(content_on_image.text)


if __name__ == "__main__":
	main()
