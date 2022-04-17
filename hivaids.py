from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import pandas as pd
import urllib.request
import seaborn as sns
import matplotlib
from streamlit_lottie import st_lottie
import requests
import json
import geopandas as gpd
import altair as alt
import numpy as np

st.set_page_config(layout='wide')

def load_url(url: str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

@st.cache
def get_datahiv():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17570_jumlah_kasus_hiv_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_dataaids():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17572_jumlah_kasus_aids_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_datamortal():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17575_jumlah_kematian_akibat_aids_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_datapenduduk():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/disdukcapil-2/od_18305_jml_penduduk__kelompok_umur_kabupatenkota?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

contents_hiv = json.loads(get_datahiv())
data_hiv = contents_hiv['data']
df = pd.DataFrame(data_hiv)

contents_aids = json.loads(get_dataaids())
data_aids = contents_aids['data']
df2 = pd.DataFrame(data_aids)

contents_mortal = json.loads(get_datamortal())
data_mortal = contents_mortal['data']
df3 = pd.DataFrame(data_mortal)

contents_penduduk = json.loads(get_datapenduduk())
data_penduduk = contents_penduduk['data']
df4 = pd.DataFrame(data_penduduk)

get_animate = load_url('https://assets2.lottiefiles.com/packages/lf20_t2bpn6yt.json')
st_lottie(get_animate, speed=1, height=200, key='initial')

matplotlib.use('agg')
_lock=RendererAgg.lock

sns.set_style('darkgrid')
row0_space1, row0_1, row0_space2, row0_2, row0_space3 = st.columns(
    (.1, 2, .2, 1, .1)
)

row0_1.title('Ikhtisar HIV/AIDS Provinsi Jawa Barat tahun 2019')

with row0_2:
    st.write('')

with row0_2:
    st.subheader('Tugas akhir data sains dan teknologi web oleh Dadi Rahmat 23220336')
    st.write('sumber: https://satudata.jabarprov.go.id')

st.write('')
row1_space1, row1_col1, row1_space2, row1_col2, row1_space3, row1_col3, row1_space4 = st.columns(
    (.1, 1, .1, 1, .1, 1, .1)
)

odha = df['jumlah_kasus'].sum()+df2['jumlah_kasus'].sum()
mortal = df3['jumlah_kasus'].sum()
pend = df4['jumlah_penduduk'].sum()/1000000

with row1_col1, _lock:
    st.title("Jumlah penduduk")
    st.markdown(f"<p style='font-size: 36px; !important'>{str('{:.2f}'.format(pend))} juta orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)
with row1_col2, _lock:
    st.title("Orang dengan HIV/AIDS")
    st.markdown(f"<p style='font-size: 36px; !important'>{str(odha)} orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)
with row1_col3, _lock:
    st.title("Kematian akibat HIV/AIDS")
    st.markdown(f"<p style='font-size: 36px; !important'>{str(mortal)} orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)

st.write('')
row2_space1, row2, row2_space2 = st.columns(
    (.1, 3.2, .1)
)

with row2, _lock:
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">HIV merupakan virus yang melemahkan sistem kekebalan tubuh manusia,
                sedangkan AIDS adalah sekumpulan gejala yang timbul karena infeksi HIV. Orang hidup dengan HIV/AIDS memerlukan
                pengobatan Antiretrovial (ARV) untuk menurunkan jumlah virus HIV di dalam tubuh agar tidak masuk ke dalam stadium AIDS,
                atau ARV untuk mencegah terjadinya infeksi yang destruktif. HIV merupakan wabah berstatus endemik karena jumlah populasi
                orang dengan HIV/AIDS (ODHA) masih termasuk dalam tingkat yang tinggi di Indonesia. Kejadian HIV/AIDS yang terus
                tinggi disebabkan oleh penularan virus yang dengan mudah menginfeksi seseorang melalui cairan tubuh seperti darah, ASI,
                cairan reproduksi, serta penularan dari ibu hamil ke anak dalam kandungannya. Namun penyakit ini tidak akan menginfeksi
                seseorang dengan kontak langsung ataupun penggunaan benda pribadi secara bersamaan.</p>''', unsafe_allow_html=True)
    st.write('')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Di Indonesia, HIV pertama kali di identifikasi pada tahun
                1987. Hingga saat ini, jumlah kasus HIV/AIDS cukup fluktuatif namun cenderung terus meningkat. Tingginya jumlah ODHA
                mengharuskan Indonesia lebih waspada terhadap penularan yang lebih besar lagi. Termasuk provinsi Jawa Barat yang tergolong
                ke dalam wilayah yang melaporkan jumlah infeksi HIV terbanyak ketiga di Indonesia. Berikut adalah ringkasan mengenai
                kondisi HIV/AIDS di provinsi Jawa Barat tahun 2019.             
                </p>''', unsafe_allow_html=True)

st.write('')
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))


with row3_1, _lock:
    st.subheader('Statistik HIV sesuai gender')
    gender_hiv = df.copy(deep=True)
    gender_hiv = gender_hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan'], axis=1)
    gender_hiv['nama_kabupaten_kota'] = gender_hiv['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)
    gender_hiv['total'] = gender_hiv.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
    gender_hiv = gender_hiv.groupby(['nama_kabupaten_kota'], as_index=False).head(2).reset_index(drop=True)

    color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                        range=['#4287f5', '#e377c2'])

    left = alt.Chart(gender_hiv).transform_filter(
        alt.datum.jenis_kelamin=='PEREMPUAN'
    ).mark_bar().encode(
        x=alt.X('total:Q', sort=alt.SortOrder('descending'), scale=alt.Scale(domain=[0, np.max(gender_hiv['total'])])),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='PEREMPUAN')

    middle = alt.Chart(gender_hiv).encode(
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        text=alt.Text('nama_kabupaten_kota:O'),
    ).mark_text().properties(width=130)

    right = alt.Chart(gender_hiv).transform_filter(
        alt.datum.jenis_kelamin=='LAKI-LAKI'
    ).mark_bar().encode(
        x=alt.X('total:Q', scale=alt.Scale(domain=[0, np.max(gender_hiv['total'])])),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='LAKI-LAKI')

    fig1 = alt.concat(left, middle, right, spacing=5)
    st.altair_chart(fig1, use_container_width=True)

with row3_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Populasi penderita HIV cukup beragam di masing-masing
                wilayah. Tingkat infeksi terbanyak berada pada Kota Bogor, dan dua wilayah yaitu Kab. Cianjur dan Kab. Garut
                mencatatkan bebas dari kasus HIV pada tahun 2019.</p>''', unsafe_allow_html=True)


st.write('')
row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))

with row4_1, _lock:
    st.subheader('Statistik HIV sesuai usia')
    age_hiv = df.copy(deep=True)
    age_hiv['total'] = age_hiv.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
    age_hiv = age_hiv.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
    age_hiv = age_hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
    age_hiv['nama_kabupaten_kota'] = age_hiv['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    bars = alt.Chart(age_hiv).mark_bar().encode(
    x=alt.X('total:Q', stack='zero'),
    y=alt.Y('nama_kabupaten_kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
    color=alt.Color('kelompok_umur')
    )

    text = alt.Chart(age_hiv).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X('total:Q', stack='zero'),
        y=alt.Y('nama_kabupaten_kota:N'),
        detail='kelompok_umur:N',
        # text=alt.Text('total:Q', format='.1f')
    )

    fig2 = bars + text
    st.altair_chart(fig2, use_container_width=True)

with row4_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Kondisi populasi HIV di Provinsi Jawa Barat tahun 2019
                didominasi oleh usia produktif yaitu pada kelompok usia 25-49 tahun. Di Kabupaten Subang terdapat populasi usia dini 0-4 tahun
                penderita HIV sebanyak 149 orang.</p>''', unsafe_allow_html=True)


st.write('')
row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))


with row5_1, _lock:
    st.subheader('Statistik AIDS sesuai gender')
    aids_gender = df2.copy(deep=True)
    aids_gender = aids_gender.drop(['id', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan'], axis=1)
    aids_gender['total'] = aids_gender.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
    aids_gender = aids_gender.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False).head(1).reset_index(drop=True).sort_values(by=['kode_kabupaten_kota','jenis_kelamin'])
    aids_gender['nama_kabupaten_kota'] = aids_gender['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                            range=['#4287f5', '#e377c2'])

    left = alt.Chart(aids_gender).transform_filter(
        alt.datum.jenis_kelamin=='PEREMPUAN'
    ).mark_bar().encode(
        x=alt.X('total:Q', sort=alt.SortOrder('descending')),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='PEREMPUAN')

    middle = alt.Chart(aids_gender).encode(
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        text=alt.Text('nama_kabupaten_kota:O'),
    ).mark_text().properties(width=140)

    right = alt.Chart(aids_gender).transform_filter(
        alt.datum.jenis_kelamin=='LAKI-LAKI'
    ).mark_bar().encode(
        x=alt.X('total:Q'),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='LAKI-LAKI')

    fig3 = alt.concat(left, middle, right, spacing=5)
    st.altair_chart(fig3, use_container_width=True)

with row5_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Penyakit AIDS merupakan fase akhir dari infeksi HIV, 
                namun beberapa data AIDS yang tercatat di beberapa Kabupaten/Kota tampak lebih besar dibandingkan dengan data HIV
                yang tercatat. Hal ini mungkin terjadi akibat misintegrasi pemantauan orang dengan HIV/AIDS pada kota tersebut.
                Untuk masing-masing wilayah yang tidak memiliki jumlah AIDS memiliki dua kemungkinan, yaitu kurangnya pemantauan
                atau fungsi kontrol yang baik oleh dinas kesehatan setempat untuk menekan infeksi HIV sehingga tidak menjadi AIDS.
                Kota Bandung tercatat memiliki jumlah penderita AIDS terbanyak.</p>''', unsafe_allow_html=True)



st.write('')
row6_space1, row6_1, row6_space2, row6_2, row6_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))

with row6_1, _lock:
    st.subheader('Statistik AIDS sesuai usia')
    aids_age = df2.copy(deep=True)
    aids_age['total'] = aids_age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
    aids_age = aids_age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
    aids_age = aids_age.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
    aids_age['nama_kabupaten_kota'] = aids_age['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    bars = alt.Chart(aids_age).mark_bar().encode(
    x=alt.X('total:Q', stack='zero'),
    y=alt.Y('nama_kabupaten_kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
    color=alt.Color('kelompok_umur')
    )

    text = alt.Chart(aids_age).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X('total:Q', stack='zero'),
        y=alt.Y('nama_kabupaten_kota:N'),
        detail='kelompok_umur:N',
        # text=alt.Text('total:Q', format='.1f')
    )

    fig4 = bars + text
    st.altair_chart(fig4, use_container_width=True)

with row6_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Kondisi populasi AIDS di Provinsi Jawa Barat tahun 2019 didominasi
            oleh usia produktif yaitu pada kelompok usia 25-49 tahun. Di Kota Bandung terdapat populasi usia remaja 15-19 tahun
            penderita HIV sebanyak 850 orang.</p>''', unsafe_allow_html=True)


st.write('')
row5_space1, row5, row5_space3 = st.columns(
    (.1,4,.1)
)

hiv = df.copy(deep=True)
hiv['total'] = hiv.groupby(['nama_kabupaten_kota'], as_index=False)['jumlah_kasus'].transform('sum')
hiv = hiv.groupby(['nama_kabupaten_kota'], as_index=False).head(1).reset_index(drop=True)
hiv = hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus', 'kelompok_umur'], axis=1)
hiv.rename(columns={'nama_kabupaten_kota':'wilayah'}, inplace=True)
has_hiv = any(hiv)

# Load the json file with county coordinates
geoData = gpd.read_file('Jabar_By_Kab.geojson')

# Make sure the "id" column is an integer
geoData.OBJECTID = geoData.OBJECTID.astype(str).astype(int)
geoData.ID_KAB = geoData.ID_KAB.astype(float).astype(int)

with row5, _lock:
    st.subheader('Peta Sebaran HIV Per Wilayah')
    if has_hiv:
        fullData = geoData.merge(hiv, left_on=['ID_KAB'], right_on=['kode_kabupaten_kota']).set_index('wilayah')
        import plotly.express as px
        fig = px.choropleth(fullData,
                        geojson=fullData.geometry,
                        locations=fullData.index,
                        color="total", color_continuous_scale="blues",
                        projection="mercator")
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(height=1000)
        fig.update_traces(
            marker_line_width=.2, marker_line_color = 'gray'
        )
        # plt.title('Peta Sebaran HIV di Provinsi Jawa Barat 2019', fontsize=13);
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.markdown(
            "We do not have information")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import pandas as pd
import urllib.request
import seaborn as sns
import matplotlib
from streamlit_lottie import st_lottie
import requests
import json
import geopandas as gpd
import altair as alt
import numpy as np

st.set_page_config(layout='wide')

def load_url(url: str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

@st.cache
def get_datahiv():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17570_jumlah_kasus_hiv_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_dataaids():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17572_jumlah_kasus_aids_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_datamortal():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/dinkes/od_17575_jumlah_kematian_akibat_aids_berdasarkan_kelompok_umur?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

@st.cache
def get_datapenduduk():
    url = 'https://satudata.jabarprov.go.id/api-backend/bigdata/disdukcapil-2/od_18305_jml_penduduk__kelompok_umur_kabupatenkota?limit=1000'
    contents = urllib.request.urlopen(url).read()
    return(contents)

contents_hiv = json.loads(get_datahiv())
data_hiv = contents_hiv['data']
df = pd.DataFrame(data_hiv)

contents_aids = json.loads(get_dataaids())
data_aids = contents_aids['data']
df2 = pd.DataFrame(data_aids)

contents_mortal = json.loads(get_datamortal())
data_mortal = contents_mortal['data']
df3 = pd.DataFrame(data_mortal)

contents_penduduk = json.loads(get_datapenduduk())
data_penduduk = contents_penduduk['data']
df4 = pd.DataFrame(data_penduduk)

get_animate = load_url('https://assets2.lottiefiles.com/packages/lf20_t2bpn6yt.json')
st_lottie(get_animate, speed=1, height=200, key='initial')

matplotlib.use('agg')
_lock=RendererAgg.lock

sns.set_style('darkgrid')
row0_space1, row0_1, row0_space2, row0_2, row0_space3 = st.columns(
    (.1, 2, .2, 1, .1)
)

row0_1.title('Ikhtisar HIV/AIDS Provinsi Jawa Barat tahun 2019')

with row0_2:
    st.write('')

with row0_2:
    st.subheader('Tugas akhir data sains dan teknologi web oleh Dadi Rahmat 23220336')
    st.write('sumber: https://satudata.jabarprov.go.id')

st.write('')
row1_space1, row1_col1, row1_space2, row1_col2, row1_space3, row1_col3, row1_space4 = st.columns(
    (.1, 1, .1, 1, .1, 1, .1)
)

odha = df['jumlah_kasus'].sum()+df2['jumlah_kasus'].sum()
mortal = df3['jumlah_kasus'].sum()
pend = df4['jumlah_penduduk'].sum()/1000000

with row1_col1, _lock:
    st.title("Jumlah penduduk")
    st.markdown(f"<p style='font-size: 36px; !important'>{str('{:.2f}'.format(pend))} juta orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)
with row1_col2, _lock:
    st.title("Orang dengan HIV/AIDS")
    st.markdown(f"<p style='font-size: 36px; !important'>{str(odha)} orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)
with row1_col3, _lock:
    st.title("Kematian akibat HIV/AIDS")
    st.markdown(f"<p style='font-size: 36px; !important'>{str(mortal)} orang</p>", unsafe_allow_html=True)
    st.markdown("<h3>di Provinsi Jawa Barat pada 2019</h3>", unsafe_allow_html=True)

st.write('')
row2_space1, row2, row2_space2 = st.columns(
    (.1, 3.2, .1)
)

with row2, _lock:
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">HIV merupakan virus yang melemahkan sistem kekebalan tubuh manusia,
                sedangkan AIDS adalah sekumpulan gejala yang timbul karena infeksi HIV. Orang hidup dengan HIV/AIDS memerlukan
                pengobatan Antiretrovial (ARV) untuk menurunkan jumlah virus HIV di dalam tubuh agar tidak masuk ke dalam stadium AIDS,
                atau ARV untuk mencegah terjadinya infeksi yang destruktif. HIV merupakan wabah berstatus endemik karena jumlah populasi
                orang dengan HIV/AIDS (ODHA) masih termasuk dalam tingkat yang tinggi di Indonesia. Kejadian HIV/AIDS yang terus
                tinggi disebabkan oleh penularan virus yang dengan mudah menginfeksi seseorang melalui cairan tubuh seperti darah, ASI,
                cairan reproduksi, serta penularan dari ibu hamil ke anak dalam kandungannya. Namun penyakit ini tidak akan menginfeksi
                seseorang dengan kontak langsung ataupun penggunaan benda pribadi secara bersamaan.</p>''', unsafe_allow_html=True)
    st.write('')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Di Indonesia, HIV pertama kali di identifikasi pada tahun
                1987. Hingga saat ini, jumlah kasus HIV/AIDS cukup fluktuatif namun cenderung terus meningkat. Tingginya jumlah ODHA
                mengharuskan Indonesia lebih waspada terhadap penularan yang lebih besar lagi. Termasuk provinsi Jawa Barat yang tergolong
                ke dalam wilayah yang melaporkan jumlah infeksi HIV terbanyak ketiga di Indonesia. Berikut adalah ringkasan mengenai
                kondisi HIV/AIDS di provinsi Jawa Barat tahun 2019.             
                </p>''', unsafe_allow_html=True)

st.write('')
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))


with row3_1, _lock:
    st.subheader('Statistik HIV sesuai gender')
    gender_hiv = df.copy(deep=True)
    gender_hiv = gender_hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan'], axis=1)
    gender_hiv['nama_kabupaten_kota'] = gender_hiv['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)
    gender_hiv['total'] = gender_hiv.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
    gender_hiv = gender_hiv.groupby(['nama_kabupaten_kota'], as_index=False).head(2).reset_index(drop=True)

    color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                        range=['#4287f5', '#e377c2'])

    left = alt.Chart(gender_hiv).transform_filter(
        alt.datum.jenis_kelamin=='PEREMPUAN'
    ).mark_bar().encode(
        x=alt.X('total:Q', sort=alt.SortOrder('descending'), scale=alt.Scale(domain=[0, np.max(gender_hiv['total'])])),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='PEREMPUAN')

    middle = alt.Chart(gender_hiv).encode(
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        text=alt.Text('nama_kabupaten_kota:O'),
    ).mark_text().properties(width=130)

    right = alt.Chart(gender_hiv).transform_filter(
        alt.datum.jenis_kelamin=='LAKI-LAKI'
    ).mark_bar().encode(
        x=alt.X('total:Q', scale=alt.Scale(domain=[0, np.max(gender_hiv['total'])])),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='LAKI-LAKI')

    fig1 = alt.concat(left, middle, right, spacing=5)
    st.altair_chart(fig1, use_container_width=True)

with row3_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Populasi penderita HIV cukup beragam di masing-masing
                wilayah. Tingkat infeksi terbanyak berada pada Kota Bogor, dan dua wilayah yaitu Kab. Cianjur dan Kab. Garut
                mencatatkan bebas dari kasus HIV pada tahun 2019.</p>''', unsafe_allow_html=True)


st.write('')
row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))

with row4_1, _lock:
    st.subheader('Statistik HIV sesuai usia')
    age_hiv = df.copy(deep=True)
    age_hiv['total'] = age_hiv.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
    age_hiv = age_hiv.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
    age_hiv = age_hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
    age_hiv['nama_kabupaten_kota'] = age_hiv['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    bars = alt.Chart(age_hiv).mark_bar().encode(
    x=alt.X('total:Q', stack='zero'),
    y=alt.Y('nama_kabupaten_kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
    color=alt.Color('kelompok_umur')
    )

    text = alt.Chart(age_hiv).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X('total:Q', stack='zero'),
        y=alt.Y('nama_kabupaten_kota:N'),
        detail='kelompok_umur:N',
        # text=alt.Text('total:Q', format='.1f')
    )

    fig2 = bars + text
    st.altair_chart(fig2, use_container_width=True)

with row4_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Kondisi populasi HIV di Provinsi Jawa Barat tahun 2019
                didominasi oleh usia produktif yaitu pada kelompok usia 25-49 tahun. Di Kabupaten Subang terdapat populasi usia dini 0-4 tahun
                penderita HIV sebanyak 149 orang.</p>''', unsafe_allow_html=True)


st.write('')
row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))


with row5_1, _lock:
    st.subheader('Statistik AIDS sesuai gender')
    aids_gender = df2.copy(deep=True)
    aids_gender = aids_gender.drop(['id', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan'], axis=1)
    aids_gender['total'] = aids_gender.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False)['jumlah_kasus'].transform('sum')
    aids_gender = aids_gender.groupby(['nama_kabupaten_kota', 'jenis_kelamin'], as_index=False).head(1).reset_index(drop=True).sort_values(by=['kode_kabupaten_kota','jenis_kelamin'])
    aids_gender['nama_kabupaten_kota'] = aids_gender['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    color_scale = alt.Scale(domain=['LAKI-LAKI', 'PEREMPUAN'],
                            range=['#4287f5', '#e377c2'])

    left = alt.Chart(aids_gender).transform_filter(
        alt.datum.jenis_kelamin=='PEREMPUAN'
    ).mark_bar().encode(
        x=alt.X('total:Q', sort=alt.SortOrder('descending')),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='PEREMPUAN')

    middle = alt.Chart(aids_gender).encode(
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        text=alt.Text('nama_kabupaten_kota:O'),
    ).mark_text().properties(width=140)

    right = alt.Chart(aids_gender).transform_filter(
        alt.datum.jenis_kelamin=='LAKI-LAKI'
    ).mark_bar().encode(
        x=alt.X('total:Q'),
        y=alt.Y('nama_kabupaten_kota:O', axis=None),
        color=alt.Color('jenis_kelamin:N', scale=color_scale, legend=None)
    ).mark_bar().properties(title='LAKI-LAKI')

    fig3 = alt.concat(left, middle, right, spacing=5)
    st.altair_chart(fig3, use_container_width=True)

with row5_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Penyakit AIDS merupakan fase akhir dari infeksi HIV, 
                namun beberapa data AIDS yang tercatat di beberapa Kabupaten/Kota tampak lebih besar dibandingkan dengan data HIV
                yang tercatat. Hal ini mungkin terjadi akibat misintegrasi pemantauan orang dengan HIV/AIDS pada kota tersebut.
                Untuk masing-masing wilayah yang tidak memiliki jumlah AIDS memiliki dua kemungkinan, yaitu kurangnya pemantauan
                atau fungsi kontrol yang baik oleh dinas kesehatan setempat untuk menekan infeksi HIV sehingga tidak menjadi AIDS.
                Kota Bandung tercatat memiliki jumlah penderita AIDS terbanyak.</p>''', unsafe_allow_html=True)



st.write('')
row6_space1, row6_1, row6_space2, row6_2, row6_space3 = st.columns(
    (.1, 2, .1, 0.7, .1))

with row6_1, _lock:
    st.subheader('Statistik AIDS sesuai usia')
    aids_age = df2.copy(deep=True)
    aids_age['total'] = aids_age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False)['jumlah_kasus'].transform('sum')
    aids_age = aids_age.groupby(['nama_kabupaten_kota', 'kelompok_umur'], as_index=False).head(1).reset_index(drop=True)
    aids_age = aids_age.drop(['id', 'kode_provinsi', 'nama_provinsi', 'kode_kabupaten_kota', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus'], axis=1)
    aids_age['nama_kabupaten_kota'] = aids_age['nama_kabupaten_kota'].str.replace(r'KABUPATEN','KAB.', regex=True)

    bars = alt.Chart(aids_age).mark_bar().encode(
    x=alt.X('total:Q', stack='zero'),
    y=alt.Y('nama_kabupaten_kota:N', axis=alt.Axis(format='', title='Kabupaten/Kota')),
    color=alt.Color('kelompok_umur')
    )

    text = alt.Chart(aids_age).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X('total:Q', stack='zero'),
        y=alt.Y('nama_kabupaten_kota:N'),
        detail='kelompok_umur:N',
        # text=alt.Text('total:Q', format='.1f')
    )

    fig4 = bars + text
    st.altair_chart(fig4, use_container_width=True)

with row6_2, _lock:
    st.subheader('Ringkasan')
    st.markdown('''<p style="text-align: justify; font-size: 18px; !important">Kondisi populasi AIDS di Provinsi Jawa Barat tahun 2019 didominasi
            oleh usia produktif yaitu pada kelompok usia 25-49 tahun. Di Kota Bandung terdapat populasi usia remaja 15-19 tahun
            penderita HIV sebanyak 850 orang.</p>''', unsafe_allow_html=True)


st.write('')
row5_space1, row5, row5_space3 = st.columns(
    (.1,4,.1)
)

hiv = df.copy(deep=True)
hiv['total'] = hiv.groupby(['nama_kabupaten_kota'], as_index=False)['jumlah_kasus'].transform('sum')
hiv = hiv.groupby(['nama_kabupaten_kota'], as_index=False).head(1).reset_index(drop=True)
hiv = hiv.drop(['id', 'kode_provinsi', 'nama_provinsi', 'tahun', 'satuan', 'jenis_kelamin', 'jumlah_kasus', 'kelompok_umur'], axis=1)
hiv.rename(columns={'nama_kabupaten_kota':'wilayah'}, inplace=True)
has_hiv = any(hiv)

# Load the json file with county coordinates
geoData = gpd.read_file('Jabar_By_Kab.geojson')

# Make sure the "id" column is an integer
geoData.OBJECTID = geoData.OBJECTID.astype(str).astype(int)
geoData.ID_KAB = geoData.ID_KAB.astype(float).astype(int)

with row5, _lock:
    st.subheader('Peta Sebaran HIV Per Wilayah')
    if has_hiv:
        fullData = geoData.merge(hiv, left_on=['ID_KAB'], right_on=['kode_kabupaten_kota']).set_index('wilayah')
        import plotly.express as px
        fig = px.choropleth(fullData,
                        geojson=fullData.geometry,
                        locations=fullData.index,
                        color="total", color_continuous_scale="blues",
                        projection="mercator")
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(height=1000)
        fig.update_traces(
            marker_line_width=.2, marker_line_color = 'gray'
        )
        # plt.title('Peta Sebaran HIV di Provinsi Jawa Barat 2019', fontsize=13);
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.markdown(
            "We do not have information")

    # st.markdown("It looks like you've read a grand total of **{} books with {} authors,** with {} being your most read author! That's awesome. Here's what your reading habits look like since you've started using Goodreads.".format(
    #     u_books, u_authors, df['book.authors.author.name'].mode()[0]))
