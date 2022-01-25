import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats

def tlak_zrychleni(data):

    zrychleni = []
    for zrychleni_row in data[289]:
        #zrychleni.append([zrychleni_row[0], math.sqrt(zrychleni_row[1][0]**2 + zrychleni_row[1][1]**2 + zrychleni_row[1][2]**2)])
        zrychleni.append([zrychleni_row[0], zrychleni_row[1][0] + zrychleni_row[1][1] + zrychleni_row[1][2]])

    tlaky= []
    for tlak_row in data[322]:
        tlaky.append([tlak_row[0], tlak_row[1][0], tlak_row[1][3]])

    zrychleni_np = np.array(zrychleni)
    tlaky_np = np.array(tlaky)

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Zavislost zrychleni na tlaku')
    ax1.plot(zrychleni_np[:, 0], zrychleni_np[:, 1])
    ax1.set_title('Zrychleni')
    ax2.plot(tlaky_np[:, 0], tlaky_np[:, 1])
    ax2.set_title('Tlak front')
    ax3.plot(tlaky_np[:, 0], tlaky_np[:, 2])
    ax3.set_title('Tlak back')
    plt.show()

    zrychleni_tlaky_boxes = []
    for i in range (350):
        zrychleni_box = []
        for zrychleni_row in zrychleni_np:
            if(zrychleni_row[0]>=i and zrychleni_row[0]<i+1):
                zrychleni_box.append(zrychleni_row[1])
        tlak1_box = []
        tlak2_box = []
        for tlaky_row in tlaky_np:
            if(tlaky_row[0]>=i and tlaky_row[0]<i+1):
                tlak1_box.append(tlaky_row[1])
                tlak2_box.append(tlaky_row[2])
        zrychleni_tlaky_boxes.append([i, np.average(zrychleni_box), np.average(tlak1_box), np.average(tlak2_box)])

    zrychleni_tlaky_boxes = np.array(zrychleni_tlaky_boxes)

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Zavislost zrychleni na tlaku')
    ax1.plot(zrychleni_tlaky_boxes[:, 0], zrychleni_tlaky_boxes[:, 1])
    ax1.set_title('Zrychleni')
    ax2.plot(zrychleni_tlaky_boxes[:, 0], zrychleni_tlaky_boxes[:, 2])
    ax2.set_title('Tlak front')
    ax3.plot(zrychleni_tlaky_boxes[:, 0], zrychleni_tlaky_boxes[:, 3])
    ax3.set_title('Tlak back')
    plt.show()

    result = scipy.stats.linregress(zrychleni_tlaky_boxes[1], zrychleni_tlaky_boxes[2])
    print("slope: " + str(result.slope))
    print("intercept: " + str(result.intercept))
    print("rvalue: " + str(result.rvalue))
    print("pvalue: " + str(result.pvalue))
    print("stderr: " + str(result.stderr))

    r = np.corrcoef(zrychleni_tlaky_boxes[:, 1], zrychleni_tlaky_boxes[:, 2])
    result1 = scipy.stats.pearsonr(zrychleni_tlaky_boxes[:, 1], zrychleni_tlaky_boxes[:, 2])
    result2 = scipy.stats.spearmanr(zrychleni_tlaky_boxes[:, 1], zrychleni_tlaky_boxes[:, 2])
    result3 = scipy.stats.kendalltau(zrychleni_tlaky_boxes[:, 1], zrychleni_tlaky_boxes[:, 2])
    print("corrcoef: " + str(r))
    print("pearsonr: " + str(result1))
    print("spearmanr: " + str(result2))
    print("kendalltau: " + str(result3))