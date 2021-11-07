import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy wyzdrowiejesz po tygodniu leczenia?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://th.bing.com/th/id/R.ebb2ef74c3f7e2e2419ceae98a0a13d6?rik=fbJiI0O7g7QgAg&pid=ImgRaw&r=0")

	with overview:
		st.title("Czy wyzdrowiejesz po tygodniu leczenia?")

	with left:
		sympts_slider = st.slider("Objawy", value=0, min_value=1, max_value=5)
		diseases_slider = st.slider( "Choroby", value=0, min_value=0, max_value=5)

	with right:
		age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
		height_slider = st.slider( "Wzrost", value=180, min_value=0, max_value=250)

	data = [[sympts_slider, age_slider, diseases_slider, height_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy wyzdrowiejesz w ciągu tygodnia? {0}".format("Tak" if survival[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga