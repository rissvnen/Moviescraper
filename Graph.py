import matplotlib.pyplot as plt

def graph(leffat, sija):
    y_mean = sum(leffat) / len(sija)

    lowest = min(leffat)
    highest = max(leffat)

    plt.figure(figsize=(10, 8))

    plt.plot(sija, leffat, ".", markersize=15)
    plt.axhline(y_mean, color='r', linestyle='-')
    plt.vlines(sija, lowest-10, leffat)
    plt.title("IMDB top 100", fontsize=15)
    plt.xlabel("Sija listalla", fontsize=15)
    plt.ylabel("Julkaisuvuosi", fontsize=15)

    plt.figtext(0.05, 0.98, f'highest = {highest}', fontsize=15, ha='left', va='center')
    plt.figtext(0.05, 0.94, f'lowest = {lowest}', fontsize=15, ha='left', va='center')
    plt.figtext(0.05, 0.9, f'mean = {y_mean:.0f}', fontsize=15, ha='left', va='center')

    plt.xlim(sija[0] - 1.5, sija[-1] + 1.5)
    plt.show()