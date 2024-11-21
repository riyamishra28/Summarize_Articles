import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt_tab')

url = 'https://www.thehindu.com/education/schools/cbse-class-10-12-exams-to-begin-from-february-15-board-announces-datesheet/article68891329.ece'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')



