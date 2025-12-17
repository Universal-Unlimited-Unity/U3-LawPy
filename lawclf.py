from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv('lawdata.csv')

x = list(df['sentence'])
y = list(df['law'])

LawClf = Pipeline([('tfidf', TfidfVectorizer()),
                ('model', LogisticRegression()
               )])

LawClf.fit(x, y)
