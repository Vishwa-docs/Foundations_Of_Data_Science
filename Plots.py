"""
pip3 install -r requirements.txt
Use scientific view and code recommendations in pycharm to find similar functions
Also look at other parameters in Documentation

Foundations of Data Science CS1704 Programs

Modules :
    Numpy
    Matplotlib
    StatsModels
    Scipy
    Scikit learn
    Pandas

Topics : 
    Data Visualization
    Charting Plot
    Statistical Models and Theory

Numpy is used for creating data and Matplotlib is used for plotting them.
Data is created in arrays (NOT lists), as speed is significantly higher
"""

# Importing Libraries and Modules within the library
import numpy as np
import matplotlib.pyplot as plt


def Plot_Functions():
    """
    For user Reference :
    plt.grid() # Generates a grid background
    plt.xlabel("Name") # Adds a Label to the axis
    plt.ylabel("Name") # Adds a Label to the axis
    plt.title("Name") # Gives a title to the Plot
    plt.show() # Display the plot
    plt.savefig("file.png") # Store the plot in your PWD
    plt.box() : Turns on the axis boxes for the plot
    :return:
    """


def Theory():
    """
    To draw a line b/w 2 points, we need infinite number of samples. We cannot do this practically.
    Hence, we only need to care about minimizing errors

    As an example, in speech synthesis, we only focus on retaining the frequency of the data and NOT the shape of the graph
    There can be multiple shapes, but frequency (i.e, Waves per second), can be inferred
    Hence, for 1 Hz frequency we need 2 points and for 2 Hz we need 4 points and so on

    :return:
    """


def List_to_Array():
    n = np.array(1000)
    # Or
    a = [1, 2, 3, 4]
    a1 = np.array(a)


def Line_Plot():  # To print 1D data in time series
    n = np.arange(1000)  # 1000 number samples in x axis (Time Series Index)
    # Generates array from 0 to 999

    type(n)  # Returns numpy.ndarray (n dimensional Array)

    # If you are using console, plt.plot(n) is enough
    plt.plot(n)  # Generates a y = x straight line
    plt.show()  # Displays the Plot
    print(np.shape(n))  # Returns the Dimensions of the array

    '''
    Sin Function Wave : 
        x(n) = sin (2 * pi * fm * n) / fs
    Where fs = Frequency of signal (SAMPLING RATE)
    Make sure that fs >= 2 * fm [At least 5x is better]
    
    We are finding the value of x(n) at every point in the plot
    '''

    # Sin wave plot
    s = np.sin(2 * np.pi * 100 * n / 1000)
    plt.plot(s)
    plt.show()

    plt.plot(s[1:100])  # Choosing specific sin waves
    plt.show()


def Stem_Plot():  # Sample Values are discrete
    n = np.arange(1000)
    s = np.sin(2 * np.pi * 100 * n / 1000)
    plt.stem(s[1:25])  # Select only required values
    plt.show()


def Histogram():  # To Generate Histogram plots
    # Mean, Variance, Sample Size as parameters
    x = np.random.normal(loc=5, scale=2, size=1000)  # Statistics works well with larger population sizes

    plt.hist(x, 10)  # Default bins is 10
    plt.show()

    plt.hist(x, 100)  # Creates Bins (Towers of histogram) to work with
    plt.show()


def Box_Plot():
    # We are creating 3 means and variances, the last bracket indicates that the sample size will be 300 (100, 3)
    x = np.random.normal((1, 3, 5), (0.5, 1, 1), (1000, 3))
    plt.boxplot(x)
    plt.show()


def Scatter_Plot():  # Used to create Clusters for Clustering algorithms like K-Means
    # Creating x and y of 2 different clusters
    x1 = np.random.normal(2, 1, 1000)
    y1 = np.random.normal(2, 1, 1000)

    x2 = np.random.normal(5, 4, 1000)
    y2 = np.random.normal(4, 1, 1000)
    # The 5 and 4 indicate the Average centers for the clusters

    plt.scatter(x1, y1)
    plt.scatter(x2, y2, c="red")
    plt.show()


def Signal_and_Noise():
    n = np.arange(1000)
    # Larger Number in Denominator, the closer the wave will be to sin wave
    signal = np.sin(2 * np.pi * 100 * n / 1000)
    plt.plot(signal[100:120])  # We are choosing samples to clear up the signal
    plt.show()

    # Denominator in signal and number of samples here must match
    noise = np.random.normal(2, 1, 1000)
    plt.hist(noise, 25)
    plt.show()

    # Combine Signal and Noise
    a = np.concatenate([signal, noise])
    '''
    The subplot will take the index position on a grid with nrows rows and ncols columns. 
    Index starts at 1 in the upper left corner and increases to the right. index can also be a two-tuple specifying the (first, last) indices
    '''
    plt.subplot(2, 1, 1)  # Create subplots to hold multiple graphs in same image
    plt.plot(a)
    plt.show()


if __name__ == '__main__':
    # Use args and kwargs
    print(Plot_Functions.__doc__)
    print(Theory.__doc__)
    Scatter_Plot()
