import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pickle.load(open("processed_data.pickle","rb"))

x = np.asarray(data["data"])
y = np.asarray(data["labels"])

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
print(accuracy_score(ytest,ypred))

f = open("model.p","wb")
pickle.dump({"model":model},f)
f.close()