import tempfile 
import streamlit as st
import openai
import whisper
import io
# page configuration 
st.set_page_config(page_title="Subtitle App", page_icon="🌀",layout="wide")

# API key
openai.api_key = st.secrets["API_SECRET"]
# function to call api to generate text from input 
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt+ '\n\n###\n\n',
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message # Creating the chatbot interface



# Page title
st.title("Ketto GPT")
st.info('Try : cancer crowdfunding with Ketto , monthly donation with Ketto SIP , benefits of crowdfunding with Ketto', icon="ℹ️")

# Whisper transcription functions
# ----------------
# @lru_cache(maxsize=1)
# def get_whisper_model(whisper_model: str):
#     """Get a whisper model from the cache or download it if it doesn't exist"""
#     model = whisper.load_model(whisper_model)
#     return model


@st.experimental_memo
def process_audio(audio_file: io.BytesIO) -> str:
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(audio_file.read())
        whisper.load_model("tiny")
        result = model.transcribe(tmp.name)  # type: ignore

    return result["text"]  # type: ignore
# @st.cache_resource 
# def process_audio(audio_file: io.BytesIO) -> str:
#     with tempfile.NamedTemporaryFile() as tmp:
#         tmp.write(audio_file.read())
#         model = get_whisper_model("base")
#         result = model.transcribe(tmp.name)  # type: ignore

#     return result["text"]  # type: ignore

# audio = st.file_uploader("Upload an audio file", type=["mp3"])
# audio_file_path = st.text_input("audio file path")
# if audio is not None:
#     # audio_bytes = audio.read()
#     # audio_loaded = whisper.load_audio(audio_bytes)
#     # st.write(np.frombuffer(audio.getbuffer()))
#     # st.audio(audio_bytes)
#     # here, input_wav is a bytes object representing the wav object
#     # rate, data = (np.frombuffer(audio.read()))

#     # data is a numpy ND array representing the audio data. Let's do some stuff with it
#     # reversed_data = data[::-1] #reversing it
#     # st.write(reversed_data)
#     # with NamedTemporaryFile(suffix="mp3") as temp:
#     #     temp.write(audio.getvalue())
#     #     temp.seek(0)
#         # """MP3 to numpy array"""
#         # a = pydub.AudioSegment.from_mp3(audio.getvalue())
#         # y = np.array(a.get_array_of_samples())
#         # if a.channels == 2:
#         #     y = y.reshape((-1, 2))
#     model = get_whisper_model("base") 
#     # options = dict(beam_size=5, best_of=5)
#     # translate_options = dict(task="translate", **options)
#     # # result = model.transcribe('/content/audio_1.mp3',**translate_options)
#     # # print(result["text"])
#     # result = model.transcribe(audio_file_path,**translate_options,fp16=False)
#     # st.write(result["text"])

#     with tempfile.NamedTemporaryFile() as tmp:
#         tmp.write(audio.read())

#         result = model.transcribe(tmp.name,fp16=False)  # type: ignore
#     st.write(result["text"])

st.title("Scribe")

audio_file = st.file_uploader("Upload a file")

if audio_file:
    st.audio(audio_file)

    result = process_audio(audio_file)

    st.header("Result")
    st.write(result)  # type: ignore




