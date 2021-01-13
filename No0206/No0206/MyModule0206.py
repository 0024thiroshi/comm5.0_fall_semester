def drawS(S1,S2):
    import matplotlib.pyplot as plt

    if len(S1)==len(S2):
        plt.scatter(S1,S2)
        plt.show()
    else:
        print("2つのSeriesのサイズが異なります")
