import pickle
import numpy as np
import pandas as pd
import streamlit as st

#-------------------------------------------------------------------------------------

popular_books = pickle.load(open('popular_dict.pkl', 'rb'))

books_list = [popular_books[i]['Book-Title'] for i in range(len(popular_books))]

books = pd.DataFrame.from_dict(pickle.load(open('books.pkl', 'rb')))

df = pd.DataFrame.from_dict(pickle.load(open('ft.pkl', 'rb')))

CF_Similarity = pickle.load(open('cf_similarity.pkl', 'rb'))

# Creating Pivot Table

pt = df.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')

pt.fillna(0, inplace=True)

#-------------------------------------------------------------------------------------

st.title('Booksmania :book:')

#-------------------------------------------------------------------------------------

st.write('Top Rated')

num_cols = 10

num_books = min(len(popular_books), num_cols)

# Create columns dynamically
columns = st.columns(num_cols)

# Iterate through books and display images
for i in range(num_books):
    with columns[i]:
        st.image(popular_books[i]['Image-URL-L'])

#-------------------------------------------------------------------------------------

def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    print(index)
    similar_items = sorted(list(enumerate(CF_Similarity[index])), key=lambda x:x[1], reverse=True)[1:6]

    data = []

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return data

# ----------------------------------------------------------------------------------------------------

book_title = st.selectbox('Search your book here', books_list)

book = df.loc[df['Book-Title'] == book_title].iloc[0]

st.image(book['Image-URL-L'], caption=book['Book-Title'] + " by " + book['Book-Author'])

rec_books = recommend(book_title)

# ----------------------------------------------------------------------------------------------------

st.write('Similar Books')

# Create columns dynamically
columns = st.columns(5)

# Iterate through books and display images
for i in range(5):
    with columns[i]:
        st.image(rec_books[i][2])