import matplotlib.pyplot as plt

def plotTimes(inputs, times, checkTimes):
    fig = plt.figure()
    ax = plt.subplot()

    plt.xlabel("Prime inputs")
    plt.ylabel("Runtime (secs)")
    plt.title("Runtimes for generation and verification of Pratt Certificates")
    plt.xscale("log")
    plt.yscale("log")

    ax.plot(inputs, times, "-o", alpha=0.7, label="generation times")
    ax.plot(inputs, checkTimes, "-o", alpha=0.7, label="verification times")
    ax.legend()
    plt.show()

def main():
    inputs = open("prime.input", "r").readlines()
    primes = [int(prime.strip()) for prime in inputs]

    # fileName = input("Enter the file name to read: ")
    # times = open(fileName, "r").readlines()
    times = open("times.txt", "r").readlines()
    times = [float(time.strip()) for time in times]

    # fileName = input("Enter the file name to read: ")
    # checkTimes = open(fileName, "r").readlines()
    checkTimes = open("checkTimes.txt", "r").readlines()
    checkTimes = [float(time.strip()) for time in checkTimes]

    plotTimes(primes, times, checkTimes)

main()
