
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


all_df = pd.read_csv("all_data.csv")


customers_df = all_df[['customer_city', 'customer_state']].dropna()
product_df = all_df[['product_category_name']].dropna()


with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")


st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('E-Commerce Public')


# Distribusi produk per kategori
st.markdown("### Distribusi Produk Per Kategori")
product_category_counts = product_df['product_category_name'].value_counts()

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x=product_category_counts.values, y=product_category_counts.index, palette="viridis", ax=ax3)
ax3.set_title('Distribusi Produk per Kategori')
ax3.set_xlabel('Jumlah Produk', fontsize=12)
ax3.set_ylabel('Kategori Produk', fontsize=12)
ax3.set_yticklabels(product_category_counts.index, rotation=45)
st.pyplot(fig3)  # Pastikan plt.show() tidak digunakan, gunakan st.pyplot


# Top 10 kota dengan pelanggan terbanyak
st.markdown("### 10 Kota dengan Jumlah Pelanggan Terbanyak")
city_counts = customers_df['customer_city'].value_counts().head(10)

fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, palette="coolwarm", ax=ax1)
ax1.set_title('10 Kota dengan Jumlah Pelanggan Terbanyak', fontsize=16)
ax1.set_xlabel('Kota', fontsize=12)
ax1.set_ylabel('Jumlah Pelanggan', fontsize=12)
ax1.set_xticklabels(city_counts.index, rotation=45)
st.pyplot(fig1)  

# Distribusi pelanggan berdasarkan negara bagian (state)
st.markdown("### Distribusi Pelanggan Berdasarkan Wilayah")
state_counts = customers_df['customer_state'].value_counts()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(x=state_counts.values, y=state_counts.index, palette="magma", ax=ax2)
ax2.set_title('Distribusi Pelanggan Berdasarkan Wilayah', fontsize=16)
ax2.set_xlabel('Wilayah (customer_state)', fontsize=12)
ax2.set_ylabel('Jumlah Pelanggan', fontsize=12)
ax2.set_xticklabels(state_counts.index, rotation=45)
st.pyplot(fig2)  



