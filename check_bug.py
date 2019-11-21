import numpy as np
import subprocess

data_input=np.zeros((20,20))
data_input[-1, :]=1

expected = np.zeros(20)
expected[-1] = 1

np.savetxt("../brain_sample.csv", data_input, fmt='%d')

subprocess.run(["python3", "sagital_brain.py"])

result = np.loadtxt('brain_average.csv', delimiter=',')

np.testing.assert_array_equal(result, expected)