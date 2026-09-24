import pickle
import numpy as np

with open("similarity.pkl", "rb") as f:
    sim = pickle.load(f)

sim = np.asarray(sim, dtype=np.float16)

with open("similarity.pkl", "wb") as f:
    pickle.dump(sim, f, protocol=4)