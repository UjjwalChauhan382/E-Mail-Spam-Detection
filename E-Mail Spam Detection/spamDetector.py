
import pickle
import streamlit as st
#pip install -U pypiwin32 
#from win32com.client import Dispatch

#def speak(text):
#	speak=Dispatch(("SAPI.SpVoice"))
#	speak.Speak(text)

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))

def main():
	st.title("Email Spam Classification :")
	st.subheader("Made By Ujjwal Chauhan")
	msg=st.text_input("Enter a text: ")
	if st.button("Predict"):
			data=[msg]
			vect=cv.transform(data).toarray()
			prediction=model.predict(vect)
			result=prediction[0]
			if result==1:
				st.error("This is a SPAM mail")
#				speak("This is a SPAM mail")
			else:
				st.success("This is NOT a SPAM mail")
#				speak("This is NOT a SPAM mail")
main()