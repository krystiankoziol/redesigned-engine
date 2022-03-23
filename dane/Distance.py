import numpy as np


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

def Distance(p1, p2):
    ans = np.sqrt((float(p1[0]) - float(p2[0]))**2 + (float(p1[1]) - float(p2[1]))**2)
    return ans

def Script_dst():

    coords = File_open('pkt_cosinusy.txt')
    np.set_printoptions(threshold=np.inf)

    x_sum = 0
    y_sum = 0

    for k in range(len(coords)):    #for calculation x,y mean

        x_temp = float(coords[k][0])
        x_sum = x_sum + x_temp
        y_temp = float(coords[k][1])
        y_sum = y_sum + y_temp

    x_mean = x_sum / (k+1)
    y_mean = y_sum / (k+1)
    coord_mean = [x_mean,y_mean]

    #print(x_mean, y_mean)

    distance_final = []
    for i in range(0, len(coords)):
        dst = Distance(coord_mean, coords[i])
        distance_final.append([i, dst])

    distance_final_array = np.array(distance_final)

    #print(distance_final_array)
    for j in range(0, len(distance_final_array)):
        print("Distance between center point - " + str(int(distance_final_array[j][0])) + ": " + str(distance_final_array[j][1]))
    return distance_final_array



if __name__ == '__main__':
    Script_dst()

