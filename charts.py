import matplotlib.pyplot as plt 

def generate_bar_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f"./imgs/{name}.png")

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels= labels)
    ax.axis("equal")
    plt.savefig("pie_chart.png")

if __name__ == "__main__":
    labels = ["a","b","c"]
    values = [100,30,80]
    generate_pie_chart(labels,values)