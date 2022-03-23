import numpy as np

def Rad_to_st(rad):
    st = rad*(180.0/np.pi)
    return st

def Stdz_to_st_poj(stp):
    st = int(stp)
    min = int((stp - st)*60.0)
    sek = round((((stp - st )*60) -min)*60,6)

    gotowe = [st, min, sek]
    return gotowe

def File_open(path):

    source = open(path, 'r')
    lines = source.readlines()

    file_read = []

    for line in lines:
        #print(line)
        coord_X = line.split(';')[0]
        coord_Y = line.split(';')[1]
        file_read.append([coord_X, coord_Y])

    #print(file_read[0][0])
    source.close()
    return file_read


def Script_az():

    coords = File_open('pkt_cosinusy.txt')
    np.set_printoptions(threshold=np.inf)

    azimuth_final = []
    for i in range(0, len(coords)):     #i is for X and j for Y
        for j in range(i, len(coords)): #i to not repead calculated distances
            if i == j:                  #if to not write 0 between points
                continue
            else:
                az = Azimuth(coords[i], coords[j])
                azimuth_final.append([i, j, az])

    azimuth_final_array = np.array(azimuth_final)

    #print(azimuth_final)
    for i in range(0, len(azimuth_final_array)):
        print("Azimuth " + str(int(azimuth_final_array[i][0])) + " - " + str(
            int(azimuth_final_array[i][1])) + ": " + str(Stdz_to_st_poj(Rad_to_st(float(azimuth_final_array[i][2])))))
    #print("Azimuth " + str(int(azimuth_final_array[681][0])) + " - " + str(int(azimuth_final_array[681][1])) + ": " + str(Stdz_to_st_poj(Rad_to_st(float(azimuth_final_array[681][2])))))
    return azimuth_final_array

def Azimuth(p1, p2):

    delta_x = float(p2[0]) - float(p1[0])
    delta_y = float(p2[1]) - float(p1[1])

    if delta_x == 0 and delta_y >0:
        az = 2.0 / np.pi
    elif delta_x == 0 and delta_y <0:
        az = 1.5 / np.pi
    elif delta_x > 0 and delta_y == 0:
        az = 0
    elif delta_x < 0 and delta_y == 0:
        az = np.pi
    elif delta_x > 0 and delta_y > 0:
        az = np.arctan(delta_y / delta_x)
    elif delta_x < 0 and delta_y > 0:
        az = np.arctan(delta_y / delta_x) + np.pi
    elif delta_x < 0 and delta_y < 0:
        az = np.arctan(delta_y / delta_x) + np.pi
    elif delta_x > 0 and delta_y < 0:
        az = np.arctan(delta_y / delta_x) + 2 * np.pi
    else:
        az = "Wild error appeared"

    return az


if __name__ == '__main__':
    array = Script_az()

