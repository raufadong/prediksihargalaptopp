import pickle
import streamlit as st

model = pickle.load(open('estimasi_laptop.sav', 'rb'))

st.title('Estimasi Laptop')

ram = st.number_input('RAM(GB)')
layar = st.number_input('Ukuran Layar(Inch)')
simpan = st.number_input('Penyimpanan(GB)')

predict = ''

if st.button('Estimasi Harga Laptop'):
    predict = model.predict(
        [[ram, layar, simpan,]]
    )
    st.write('Estimasi Harga Laptop : ', predict)