import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():

    fig_names = [
    "HD68450_chart.png",
    "HD68450_2020-03-12_197_orig.png",
    "HD68450_2020-03-12_208_orig.png",
    "HD68450_2020-03-12_197.png",
    "HD68450_2020-03-12_208.png",
     ]

    fig_images = []

    img_chart = mpimg.imread(fig_names[0])
    img_197_orig = mpimg.imread(fig_names[1])
    img_208_orig = mpimg.imread(fig_names[2])
    img_197 = mpimg.imread(fig_names[3])
    img_208 = mpimg.imread(fig_names[4])

    fig = plt.figure(1, (10, 5))

    print(fig.get_size_inches())

    ax1 = fig.add_subplot(121)

    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)

    ax1.imshow(img_chart)

    ax2 = fig.add_subplot(243)

    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    ax2.imshow(img_197_orig)

    ax2.set_title("Original orientation")

    ax3 = fig.add_subplot(247)

    ax3.axes.get_xaxis().set_visible(False)
    ax3.axes.get_yaxis().set_visible(False)

    ax3.imshow(img_208_orig)

    ax4 = fig.add_subplot(244)

    ax4.axes.get_xaxis().set_visible(False)
    ax4.axes.get_yaxis().set_visible(False)

    ax4.imshow(img_197)

    ax4.set_title("Computed orientation")

    ax5 = fig.add_subplot(248)

    ax5.axes.get_xaxis().set_visible(False)
    ax5.axes.get_yaxis().set_visible(False)

    ax5.imshow(img_208)

    plt.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.96, wspace=0.05, hspace=0.)
    # plt.show()

    fig.savefig("HD68450.png")

if __name__ == "__main__":
    main()
