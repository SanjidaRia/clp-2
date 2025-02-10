import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temperatures = [18, 25, 21, 14, 23, 26, 20]
plt.plot(days, temperatures, marker='s', color='darkgreen', linestyle='--', linewidth=2, markersize=8, markerfacecolor='red')
plt.title('Weekly Temperature Trends', fontsize=14, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=30)  
plt.grid(True, linestyle=':', linewidth=0.7)
plt.show()

