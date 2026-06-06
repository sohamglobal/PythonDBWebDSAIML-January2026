# pip install scikit-learn

import joblib

model=joblib.load("movierecomodel.joblib")

prediction=model.predict([[2,41,1]])
print(prediction)