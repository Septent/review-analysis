import re
# import nltk
# nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

def predict(model, corpus, text):
    corpus2 = []
    review2 = re.sub("[^a-zA-z]", ' ', text)
    review2 = review2.lower()
    review2 = review2.split()
    ps2 = PorterStemmer()
    review2 = [ps2.stem(word) for word in review2 if not word in set(stopwords.words('english'))]
    review2 = " ".join(review2)
    corpus2.append(review2)
    cv2 = CountVectorizer(max_features = 1500)
    X2 = cv2.fit_transform(corpus + corpus2).toarray()
    my = X2[-1].reshape(1, -1)
    result = model.predict(my)
    if result == 1:
        answear = "Positive"
    else:
        answear = "Negative"

    return answear