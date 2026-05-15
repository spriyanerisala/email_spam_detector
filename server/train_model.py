import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle



data = [
  
    ("Win cash prize now", 1),
    ("Congratulations you won a lottery", 1),
    ("Free recharge offer click now", 1),
    ("Claim your free iPhone now", 1),
    ("You have been selected for prize", 1),
    ("Earn money fast without effort", 1),
    ("Limited offer act now", 1),
    ("Get loan approved instantly", 1),
    ("Win 10000 rupees today", 1),
    ("Free gift card waiting for you", 1),
    ("Congratulations you are lucky winner", 1),
    ("Click here to claim reward", 1),
    ("You won a jackpot prize", 1),
    ("Urgent offer expires today", 1),
    ("Get rich quick scheme", 1),
    ("Free subscription activated click", 1),
    ("Best loan offer available now", 1),
    ("Win big rewards instantly", 1),
    ("Exclusive offer just for you", 1),
    ("Claim your cashback reward now", 1),

  
    ("Hello how are you", 0),
    ("Let's meet tomorrow", 0),
    ("Are you coming to college", 0),
    ("Good morning have a nice day", 0),
    ("I will call you later", 0),
    ("What are you doing now", 0),
    ("Happy birthday to you", 0),
    ("See you at the meeting", 0),
    ("Please send me notes", 0),
    ("Where are you now", 0),
    ("I am going home", 0),
    ("Let's go for dinner", 0),
    ("Thank you so much", 0),
    ("Talk to you later", 0),
    ("Can you help me with assignment", 0),
    ("We have class today", 0),
    ("I will come in 10 minutes", 0),
    ("Take care of yourself", 0),
    ("See you tomorrow morning", 0),
    ("Good night sweet dreams", 0),
]


df = pd.DataFrame(data, columns=["text", "label"])
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully with expanded dataset!")