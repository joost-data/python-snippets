import matplotlib.pyplot as plt

def scatter_plot(x, y, title="", xlabel="", ylabel=""):
    plt.scatter(x, y, alpha=0.6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

