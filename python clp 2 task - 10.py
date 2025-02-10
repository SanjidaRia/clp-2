import matplotlib.pyplot as plt
plt.style.use('ggplot')
regions = ['Dhaka', 'Rajshahi', 'Sylhet', 'Chattogram']
sales_revenue = [50000, 70000, 60000, 55000]
colors = ['midnightblue', 'royalblue', 'purple', 'darkorchid']
plt.bar(regions, sales_revenue, color=colors, edgecolor='black', linewidth=1.2)
plt.title('Sales Revenue Comparison by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue (BDT)', fontsize=12)
plt.xticks(rotation=20)  
plt.show()
