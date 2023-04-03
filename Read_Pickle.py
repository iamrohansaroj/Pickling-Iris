#To read this pickle fike you can use this code
import pickle
with open("myiris.pkl","rb") as f:
    print(pickle.load(f))