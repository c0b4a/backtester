#csv_to_graph
import matplotlib.pyplot as plt
import pandas as pd
import sys

def plotCSV():
    data = pd.read_csv(input('Select file:'))
    data.Close.plot()
    plt.show()

def main():
    plotCSV()
    sys.exit()

if __name__ == '__main__':
    main()