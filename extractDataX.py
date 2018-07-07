import numpy as np
def make_flat(datam_copy):
    final_datam = []
    for lol in datam_copy:
        hulala = []
        for item in lol:
            if isinstance(item, list):
                for sub in item:
                    hulala.append(sub)
            else:
                hulala.append(item)
        final_datam.append(hulala)
    return np.array(final_datam)


final_datam = np.array(final_datam)
temp_data = np.concatenate((final_datag, final_datab), axis = 0)
X = np.concatenate((temp_data, final_datam), axis = 0)


np.save("X", X)
