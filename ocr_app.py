import sys # System-specific parameters and functions
import easyocr as ocr  # OCR
import streamlit as st  # web app
from streamlit.web import cli as stcli # cli web app
from streamlit import runtime
from PIL import Image  # opening images
import numpy as np  # for array conversions


st.set_page_config(
    page_title="EasyOCR Text Recognition App With Streamlit",
    page_icon="🔍",
    layout="wide",
    menu_items={
         'Get Help': None,
         'Report a bug': None,
         
         'About': "# Text recognition in different languages ​​of the world."
    }
)


@st.cache
def load_model(lang):
    return ocr.Reader([lang], model_storage_directory=".")


def main():
    st.title("🔍✔ EasyOCR Text Recognition App")
    st.write("For optical character recognition, you must select from the list on the left side the language corresponding to the language of the text")
    image = st.file_uploader(
        label="Upload Your Image Please 😊", type=["png", "jpg", "jpeg"]
    )


    langs = {
"Afrikaans" :	"af",
"Angika" :	"ang",
"Arabic" : 	"ar",
"Chechen" :	"che",
"English" :	"en",
"Spanish" :	"es",
"Persian (Farsi)" :	"fa",
"French" :	"fr",
"Irish"	: "ga",
"Latin" :	"la",
"Nagpuri" :	"sck",
"Slovak" :	"sk",
"Slovenian" : 	"sl",
"Albanian" : "sq",
"Swedish" :	"sv",
"Swahili" :	"sw",
"Tamil" :	"ta",
"Tabassaran" :	"tab",
"Telugu" :	"te",
"Thai" :	"th",
"Tajik"	: "tjk",
"Tagalog"	: "tl",
"Turkish"	: "tr",
"Uyghur" :"ug",
"Ukranian"	: "uk",
"Urdu"	: "ur",
"Uzbek"	: "uz",
"Vietnamese" :	"vi"
}


    label_langs = st.sidebar.title('📝🗺️Select Your Language')
    feature_choice = st.sidebar.selectbox(
        "Specify the language of the text for recognition ", list(langs.keys())
    )


    info_text = st.sidebar.text('Multiple Languages Available')
    if image is not None:
        input_image = Image.open(image)
        st.image(input_image)
        reader = load_model(lang=langs.get(feature_choice))
        with st.spinner("🤖 Recognising... "):
            result = reader.readtext(
                np.array(input_image)
            )
            out_str = " "
            list_text = [ftext[1] for ftext in result]
            st.title("Loading Your Result....:")
            with open(".txt", 'w') as file:
                file.write(out_str.join(list_text))
            result_file = open(".txt", 'r')
            st.download_button('Download recognized text', result_file)

            st.title("Recognized Image as Text:")

  
            futext = st.write(out_str.join(list_text))
            st.title("Recognized Image in the List:")
            result_text = [text[1] for text in result]
            st.write(result_text)
    else:
        st.info(
            "Please select a language and upload an image for recognition..."
        )
    st.caption("Have Fun..! 😁")


if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())