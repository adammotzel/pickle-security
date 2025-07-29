import pickle as pkl


with open("container/sample.pkl", "wb") as file:
    pkl.dump("Hello World!", file)
    