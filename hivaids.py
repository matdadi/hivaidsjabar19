from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import numpy as np
import pandas as pd
from pandas import json_normalize
import urllib.request
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import json
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

def load_url(url: str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

get_animate = load_url('https://assets2.lottiefiles.com/packages/lf20_t2bpn6yt.json')
st_lottie(get_animate, speed=1, height=200, key='initial')

matplotlib.use('agg')
_lock=RendererAgg.lock

sns.set_style('darkgrid')
row0_space1, row0_1, row0_space2, row0_2, row0_space3 = st.columns(
    (.1, 2, .2, 1, .1)
)

row0_1.title('HIV/AIDS Provinsi Jabar 2019')

with row0_2:
    st.write('')

row0_2.subheader(
    'Tugas akhir Data sains dan teknologi web oleh Dadi Rahmat 23220336'
)

@st.cache
def get_datahiv():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17570_jumlah_kasus_hiv_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

def get_dataaids():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17572_jumlah_kasus_aids_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

contents_hiv = json.loads(get_datahiv())
data_hiv = contents_hiv['data']
df = pd.DataFrame(data_hiv)

contents_aids = json.loads(get_dataaids())
data_aids = contents_aids['data']
df2 = pd.DataFrame(data_aids)

# hiv gender
gender = df.copy(deep=True)
gender = gender.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan'], axis=1)
gender['total'] = gender.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
gender = gender.groupby(['nama_kabupaten_kota'], as_index=False).head(2).reset_index(drop=True)
has_gender = any(gender)

# hiv age
age = df.copy(deep=True)
age['total'] = age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
age = age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
age = age.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
has_age = any(age)

# aids gender
gender2 = df2.copy(deep=True)
gender2['kode_kabupaten_kota'] = gender2['kode_kabupaten_kota'].astype('str').astype(int)
gender2 = gender2.drop(['id', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan'], axis=1)
gender2['total'] = gender2.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
gender2 = gender2.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False).head(1).reset_index(drop=True).sort_values(by=['kode_kabupaten_kota','jenis_kelamin'])
has_gender2 = any(gender2)

# aids age
age2 = df2.copy(deep=True)
age2['total'] = age2.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
age2 = age2.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
age2 = age2.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
has_age2 = any(age2)

st.write('')
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (.1, 1, .1, 1, .1))

with row3_1, _lock:
    st.subheader('Statistik HIV sesuai gender')
    if has_gender:
        fig = plt.figure()
        ax = fig.subplots()
        sns.set(style='white')
        sns.barplot(x=gender['nama_kabupaten_kota'],
                    y=gender['total'], hue=gender['jenis_kelamin'], ax=ax)
        ax.set_xlabel('Kabupaten/Kota')
        ax.set_ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.markdown(
            "We do not have information to find out _when_ you read your books")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))

with row3_2, _lock:
    st.subheader('Statistik HIV sesuai kelompok umur')
    if has_age:
        fig = plt.figure()
        ax = fig.subplots()
        sns.set(style='white')
        sns.barplot(x=age['nama_kabupaten_kota'],
                    y=age['total'], hue=age['kelompok_umur'], ax=ax)
        ax.set_xlabel('Kabupaten/Kota')
        ax.set_ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.markdown(
            "We do not have information to find out _when_ you read your books")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))

st.write('')
row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (.1,1,.1,1,.1)
)

with row4_1, _lock:
    st.subheader('Statistik AIDS sesuai gender')
    if has_gender2:
        fig = plt.figure()
        ax = fig.subplots()
        sns.set(style='white')
        sns.barplot(x=gender2['nama_kabupaten_kota'],
                    y=gender2['total'], hue=gender2['kelompok_umur'], ax=ax)
        ax.set_xlabel('Kabupaten/Kota')
        ax.set_ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.markdown(
            "We do not have information to find out _when_ you read your books")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))

with row4_2, _lock:
    st.subheader('Statistik AIDS sesuai kelompok umur')
    if has_age2:
        fig = plt.figure()
        ax = fig.subplots()
        sns.set(style='white')
        sns.barplot(x=age2['nama_kabupaten_kota'],
                    y=age2['total'], hue=age2['kelompok_umur'], ax=ax)
        ax.set_xlabel('Kabupaten/Kota')
        ax.set_ylabel('Jumlah')
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.markdown(
            "We do not have information to find out _when_ you read your books")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))
