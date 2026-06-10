import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("MATPLOTLIB - LINE PLOT")
print("="*60)

#simple line plot
x = np.linspace(0,10,100)
y = np.sin(x)

plt.figure(figsize=(10,6))
plt.plot(x,y,linewidth=2,color='blue',label="sin(x)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple line plot: Sin wave")
plt.grid(True,alpha=0.3)
plt.legend()
plt.savefig("plot_1_line.png")
plt.close()
print("✓ Plot 1 saved: plot_1_line.png")

print("\n"+"="*60)
print("MATPLOTLIB - BAR CHART")
print("="*60)

categories = ['Python','Javascript','Java','C++','Go']
popularity = [85,72,65,58,45]

plt.figure(figsize=(10,6))
plt.bar(categories,popularity,color="green",edgecolor="black")
plt.xlabel("Programming Language")
plt.ylabel("Popularity Score")
plt.title("Programming Language popularity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_2_bar.png")
plt.close()
print("✓ Plot 2 saved: plot_2_bar.png")

print("\n"+"="*60)
print("MATPLOTLIB - SCATTER PLOT")
print("="*60)

#scatter plot
np.random.seed(42)
x = np.random.randn(100)
y = 2*y + np.random.randn(100)

plt.figure(figsize=(10,6))
plt.scatter(x,y,alpha=0.6,s=100,color='red')
plt.xlabel("X Values")
plt.xlabel("Y Values")
plt.title("Scatter plot: Relationship")
plt.grid(True,alpha=0.3)
plt.savefig("plot_3_scatter.png")
plt.close()
print("✓ Plot 3 saved: plot_3_scatter.png")

print("\n"+"="*60)
print("MATPLOTLIB - HISTOGRAM")
print("="*60)

#HISTOGRAM
data = np.random.normal(loc=100,scale=15,size=1000)

plt.figure(figsize=(10,6))
plt.hist(data,bins=30,color="purple",edgecolor="black",alpha=0.7)
plt.xlabel("Values")
plt.ylabel("Frequancy")
plt.title("Histogram: Normal Disrubution")
plt.axvline(np.mean(data),color="red",linestyle="--",linewidth=2,label="Mean")
plt.legend()
plt.savefig("plot_4_histogram.png")
plt.close()
print("✓ Plot 4 saved: plot_4_histogram.png")

print("\n"+"="*60)
print("MATPLOTLIB - SUBPLOTS (Multiple plots)")
print("="*60)

fig, axes = plt.subplots(2,2,figsize=(12,10))

#plot 1: Line
x =np.linspace(0,10,100)
axes[0,0].plot(x,np.sin(x),color="blue")
axes[0,0].set_title("Sin Wave")

# Plot 2: Cos
axes[0,1].plot(x,np.cos(x),color="red")
axes[0,1].set_title("Cos Wave")

# Plot 3: Scatter
np.random.seed(42)
axes[1,0].scatter(np.random.randn(50),np.random.randn(50),color="green")
axes[1,0].set_title("Random Scatter")


#Plot 4: Bar
categories = ['A','B','C']
values = [10,20,15]
axes[1,1].bar(categories,values,color="orange")
axes[1,1].set_title('Bar Chart')

plt.tight_layout()
plt.savefig("plot_5_subplots.png")
plt.close()
print("✓ Plot 5 saved: plot_5_subplots.png")

print("\n"+"="*60)
print("MATPLOTLIB - STYLING")
print("="*60)

x = np.linspace(0,10,100)
plt.figure(figsize=(12,6))
plt.plot(x,np.sin(x),'b-',linewidth=2,label="sin(x)",marker="o",markersize=4)
plt.plot(x,np.cos(x),'r--',linewidth=2,label="cos(x)",marker="s",markersize=4)
plt.plot(x,np.tan(x),'g:',linewidth=2,label="tan(x)")

plt.xlabel("X Axis",fontsize=12)
plt.ylabel("Y Axis",fontsize=12)
plt.title("Trogonometric Functions,",fontsize=14,fontweight="bold")
plt.legend(fontsize=10)
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("plot_6_styling.png")
plt.close()
print("✓ Plot 6 saved: plot_6_styling.png")

print("\n Plotting complete!")
