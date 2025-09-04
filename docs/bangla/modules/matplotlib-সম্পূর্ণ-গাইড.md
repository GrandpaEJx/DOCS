# 📊 Matplotlib - সম্পূর্ণ বাংলা গাইড

## 🌟 Matplotlib কি?

Matplotlib হলো Python এর সবচেয়ে জনপ্রিয় **data visualization library** যা দিয়ে আপনি professional quality এর charts, graphs ও plots তৈরি করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Multiple plot types** - Line, bar, scatter, histogram, pie
- ✅ **Customization** - Colors, styles, annotations
- ✅ **Subplots** - Multiple plots in one figure
- ✅ **Export formats** - PNG, PDF, SVG, EPS
- ✅ **Interactive plots** - Zoom, pan, save
- ✅ **3D plotting** - Three-dimensional visualizations

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# Matplotlib install
pip install matplotlib>=3.7.0

# Additional dependencies
pip install numpy>=1.24.0      # Numerical data
pip install pandas>=2.1.0      # Data manipulation
```

### ✅ **Installation Verify:**
```python
# test_matplotlib.py
import matplotlib.pyplot as plt
import numpy as np

def test_matplotlib():
    print("🧪 Matplotlib installation test...")
    
    # Simple plot
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o')
    plt.title('Test Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)
    
    # Save plot
    plt.savefig('test_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Plot created and saved")
    print("🎉 Matplotlib working perfectly!")

test_matplotlib()
```

---

## 📈 Basic Plotting

### 📊 **Line Plots:**
```python
import matplotlib.pyplot as plt
import numpy as np

def line_plots():
    """Line plot examples"""
    
    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # Basic line plot
    plt.figure(figsize=(12, 8))
    
    # Single line
    plt.subplot(2, 2, 1)
    plt.plot(x, y1)
    plt.title('Basic Line Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)
    
    # Multiple lines
    plt.subplot(2, 2, 2)
    plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
    plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')
    plt.plot(x, y3, label='sin(x)*cos(x)', color='green', marker='o', markersize=3)
    plt.title('Multiple Lines')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Styled line plot
    plt.subplot(2, 2, 3)
    plt.plot(x, y1, 'b-', linewidth=3, alpha=0.7)
    plt.fill_between(x, y1, alpha=0.3)
    plt.title('Filled Area Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    # Custom styling
    plt.subplot(2, 2, 4)
    plt.plot(x, y1, color='purple', linestyle=':', marker='s', 
             markersize=4, markerfacecolor='yellow', markeredgecolor='black')
    plt.title('Custom Styling')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    plt.tight_layout()
    plt.savefig('line_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

line_plots()
```

### 📊 **Bar Charts:**
```python
def bar_charts():
    """Bar chart examples"""
    
    # Sample data
    categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
    values = [85, 70, 60, 45, 30]
    colors = ['#3776ab', '#f7df1e', '#ed8b00', '#00599c', '#00add8']
    
    plt.figure(figsize=(15, 10))
    
    # Vertical bar chart
    plt.subplot(2, 3, 1)
    bars = plt.bar(categories, values, color=colors)
    plt.title('Programming Languages Popularity')
    plt.xlabel('Languages')
    plt.ylabel('Popularity Score')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                str(value), ha='center', va='bottom')
    
    # Horizontal bar chart
    plt.subplot(2, 3, 2)
    plt.barh(categories, values, color=colors)
    plt.title('Horizontal Bar Chart')
    plt.xlabel('Popularity Score')
    plt.ylabel('Languages')
    
    # Grouped bar chart
    plt.subplot(2, 3, 3)
    x = np.arange(len(categories))
    width = 0.35
    
    frontend = [60, 90, 20, 10, 15]
    backend = [95, 40, 80, 70, 85]
    
    plt.bar(x - width/2, frontend, width, label='Frontend', alpha=0.8)
    plt.bar(x + width/2, backend, width, label='Backend', alpha=0.8)
    plt.title('Frontend vs Backend Usage')
    plt.xlabel('Languages')
    plt.ylabel('Usage Score')
    plt.xticks(x, categories, rotation=45)
    plt.legend()
    
    # Stacked bar chart
    plt.subplot(2, 3, 4)
    plt.bar(categories, frontend, label='Frontend')
    plt.bar(categories, backend, bottom=frontend, label='Backend')
    plt.title('Stacked Bar Chart')
    plt.xlabel('Languages')
    plt.ylabel('Total Score')
    plt.xticks(rotation=45)
    plt.legend()
    
    # Pie chart
    plt.subplot(2, 3, 5)
    plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', 
            startangle=90, explode=(0.1, 0, 0, 0, 0))
    plt.title('Market Share')
    
    # Donut chart
    plt.subplot(2, 3, 6)
    plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%',
            startangle=90, wedgeprops=dict(width=0.5))
    plt.title('Donut Chart')
    
    plt.tight_layout()
    plt.savefig('bar_charts.png', dpi=300, bbox_inches='tight')
    plt.show()

bar_charts()
```

### 🔵 **Scatter Plots:**
```python
def scatter_plots():
    """Scatter plot examples"""
    
    # Generate sample data
    np.random.seed(42)
    n = 100
    
    x = np.random.randn(n)
    y = 2 * x + np.random.randn(n) * 0.5
    colors = np.random.rand(n)
    sizes = 1000 * np.random.rand(n)
    
    plt.figure(figsize=(15, 10))
    
    # Basic scatter plot
    plt.subplot(2, 3, 1)
    plt.scatter(x, y)
    plt.title('Basic Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    # Colored scatter plot
    plt.subplot(2, 3, 2)
    scatter = plt.scatter(x, y, c=colors, cmap='viridis', alpha=0.7)
    plt.colorbar(scatter)
    plt.title('Colored Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    # Sized scatter plot
    plt.subplot(2, 3, 3)
    plt.scatter(x, y, s=sizes, alpha=0.5, c=colors, cmap='plasma')
    plt.title('Variable Size Scatter')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    # Multiple categories
    plt.subplot(2, 3, 4)
    categories = ['A', 'B', 'C']
    for i, category in enumerate(categories):
        mask = np.random.choice([True, False], n)
        plt.scatter(x[mask], y[mask], label=f'Category {category}', alpha=0.7)
    
    plt.title('Categorical Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Correlation with trend line
    plt.subplot(2, 3, 5)
    plt.scatter(x, y, alpha=0.6)
    
    # Add trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2)
    
    plt.title('Scatter with Trend Line')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    # Bubble chart
    plt.subplot(2, 3, 6)
    bubble_sizes = sizes / 10  # Scale down for better visualization
    scatter = plt.scatter(x, y, s=bubble_sizes, c=colors, 
                         cmap='coolwarm', alpha=0.6, edgecolors='black', linewidth=0.5)
    plt.colorbar(scatter)
    plt.title('Bubble Chart')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    plt.tight_layout()
    plt.savefig('scatter_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

scatter_plots()
```

---

## 📊 Statistical Plots

### 📈 **Histograms:**
```python
def histograms():
    """Histogram examples"""
    
    # Generate sample data
    np.random.seed(42)
    data1 = np.random.normal(100, 15, 1000)  # Normal distribution
    data2 = np.random.exponential(2, 1000)   # Exponential distribution
    data3 = np.random.uniform(0, 10, 1000)   # Uniform distribution
    
    plt.figure(figsize=(15, 10))
    
    # Basic histogram
    plt.subplot(2, 3, 1)
    plt.hist(data1, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Normal Distribution')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Multiple histograms
    plt.subplot(2, 3, 2)
    plt.hist(data1, bins=30, alpha=0.5, label='Normal', color='blue')
    plt.hist(data2, bins=30, alpha=0.5, label='Exponential', color='red')
    plt.title('Multiple Distributions')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Density histogram
    plt.subplot(2, 3, 3)
    plt.hist(data1, bins=30, density=True, alpha=0.7, color='green')
    plt.title('Density Histogram')
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.grid(True, alpha=0.3)
    
    # Cumulative histogram
    plt.subplot(2, 3, 4)
    plt.hist(data1, bins=30, cumulative=True, alpha=0.7, color='orange')
    plt.title('Cumulative Histogram')
    plt.xlabel('Values')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True, alpha=0.3)
    
    # 2D histogram
    plt.subplot(2, 3, 5)
    x = np.random.randn(1000)
    y = 2 * x + np.random.randn(1000)
    plt.hist2d(x, y, bins=30, cmap='Blues')
    plt.colorbar()
    plt.title('2D Histogram')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    
    # Box plot
    plt.subplot(2, 3, 6)
    data_list = [data1, data2[:500], data3]
    labels = ['Normal', 'Exponential', 'Uniform']
    
    box_plot = plt.boxplot(data_list, labels=labels, patch_artist=True)
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
    
    plt.title('Box Plot Comparison')
    plt.ylabel('Values')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('histograms.png', dpi=300, bbox_inches='tight')
    plt.show()

histograms()
```

---

## 🎨 Customization ও Styling

### 🎨 **Advanced Styling:**
```python
def advanced_styling():
    """Advanced plot styling"""
    
    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Set style
    plt.style.use('seaborn-v0_8')  # Use seaborn style
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Advanced Styling Examples', fontsize=16, fontweight='bold')
    
    # Custom colors and fonts
    ax1 = axes[0, 0]
    ax1.plot(x, y1, color='#FF6B6B', linewidth=3, label='sin(x)')
    ax1.plot(x, y2, color='#4ECDC4', linewidth=3, label='cos(x)')
    ax1.set_title('Custom Colors', fontsize=14, fontweight='bold')
    ax1.set_xlabel('X values', fontsize=12)
    ax1.set_ylabel('Y values', fontsize=12)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_facecolor('#F8F8F8')
    
    # Annotations
    ax2 = axes[0, 1]
    ax2.plot(x, y1, 'b-', linewidth=2)
    ax2.annotate('Maximum', xy=(np.pi/2, 1), xytext=(2, 1.2),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red')
    ax2.annotate('Minimum', xy=(3*np.pi/2, -1), xytext=(5, -1.2),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                fontsize=12, color='blue')
    ax2.set_title('Annotations', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Custom markers and styles
    ax3 = axes[1, 0]
    markers = ['o', 's', '^', 'D', 'v']
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    
    for i in range(5):
        y_offset = i * 0.2
        ax3.plot(x[::10], y1[::10] + y_offset, 
                marker=markers[i], color=colors[i], 
                markersize=8, linewidth=2, label=f'Style {i+1}')
    
    ax3.set_title('Custom Markers', fontsize=14, fontweight='bold')
    ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax3.grid(True, alpha=0.3)
    
    # Subplots with different scales
    ax4 = axes[1, 1]
    ax4_twin = ax4.twinx()
    
    line1 = ax4.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
    line2 = ax4_twin.plot(x, y1*100, 'r-', linewidth=2, label='sin(x)*100')
    
    ax4.set_xlabel('X values')
    ax4.set_ylabel('sin(x)', color='blue')
    ax4_twin.set_ylabel('sin(x)*100', color='red')
    ax4.set_title('Dual Y-axis', fontsize=14, fontweight='bold')
    
    # Combine legends
    lines1, labels1 = ax4.get_legend_handles_labels()
    lines2, labels2 = ax4_twin.get_legend_handles_labels()
    ax4.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('advanced_styling.png', dpi=300, bbox_inches='tight')
    plt.show()

advanced_styling()
```

---

## 📊 Data Visualization with Pandas

### 🐼 **Pandas Integration:**
```python
import pandas as pd

def pandas_integration():
    """Matplotlib with Pandas"""
    
    # Create sample dataset
    dates = pd.date_range('2023-01-01', periods=365, freq='D')
    
    np.random.seed(42)
    data = {
        'Date': dates,
        'Sales': np.random.normal(1000, 200, 365).cumsum(),
        'Marketing': np.random.normal(500, 100, 365),
        'Profit': np.random.normal(300, 50, 365).cumsum(),
        'Category': np.random.choice(['A', 'B', 'C'], 365)
    }
    
    df = pd.DataFrame(data)
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    
    plt.figure(figsize=(16, 12))
    
    # Time series plot
    plt.subplot(2, 3, 1)
    df.set_index('Date')['Sales'].plot(kind='line', color='blue', alpha=0.7)
    plt.title('Sales Over Time')
    plt.ylabel('Sales')
    plt.grid(True, alpha=0.3)
    
    # Monthly aggregation
    plt.subplot(2, 3, 2)
    monthly_sales = df.groupby('Month')['Sales'].mean()
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Average Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    
    # Category comparison
    plt.subplot(2, 3, 3)
    category_profit = df.groupby('Category')['Profit'].sum()
    category_profit.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Profit by Category')
    plt.ylabel('')
    
    # Correlation heatmap
    plt.subplot(2, 3, 4)
    correlation = df[['Sales', 'Marketing', 'Profit']].corr()
    im = plt.imshow(correlation, cmap='coolwarm', aspect='auto')
    plt.colorbar(im)
    plt.xticks(range(len(correlation.columns)), correlation.columns)
    plt.yticks(range(len(correlation.columns)), correlation.columns)
    plt.title('Correlation Heatmap')
    
    # Add correlation values
    for i in range(len(correlation.columns)):
        for j in range(len(correlation.columns)):
            plt.text(j, i, f'{correlation.iloc[i, j]:.2f}', 
                    ha='center', va='center', color='white', fontweight='bold')
    
    # Quarterly trends
    plt.subplot(2, 3, 5)
    quarterly_data = df.groupby('Quarter').agg({
        'Sales': 'sum',
        'Marketing': 'sum',
        'Profit': 'sum'
    })
    
    quarterly_data.plot(kind='bar', ax=plt.gca())
    plt.title('Quarterly Performance')
    plt.xlabel('Quarter')
    plt.ylabel('Amount')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=0)
    
    # Distribution plot
    plt.subplot(2, 3, 6)
    df['Sales'].hist(bins=30, alpha=0.7, color='green', edgecolor='black')
    plt.axvline(df['Sales'].mean(), color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {df["Sales"].mean():.0f}')
    plt.axvline(df['Sales'].median(), color='blue', linestyle='--', 
                linewidth=2, label=f'Median: {df["Sales"].median():.0f}')
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pandas_integration.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Summary statistics
    print("📊 Dataset Summary:")
    print(df.describe())

pandas_integration()
```

---

## 💾 Saving ও Export

### 💾 **Export Options:**
```python
def export_options():
    """Different export formats"""
    
    # Create sample plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.exp(-x/10)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=3, label='Damped Sine Wave')
    plt.fill_between(x, y, alpha=0.3)
    plt.title('Export Example Plot', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Save in different formats
    formats = {
        'PNG': {'format': 'png', 'dpi': 300},
        'PDF': {'format': 'pdf', 'dpi': 300},
        'SVG': {'format': 'svg'},
        'EPS': {'format': 'eps', 'dpi': 300},
        'JPG': {'format': 'jpg', 'dpi': 300, 'quality': 95}
    }
    
    for name, params in formats.items():
        filename = f'export_example.{params["format"]}'
        
        if 'quality' in params:
            plt.savefig(filename, format=params['format'], 
                       dpi=params.get('dpi', 100), 
                       bbox_inches='tight', 
                       quality=params['quality'])
        else:
            plt.savefig(filename, format=params['format'], 
                       dpi=params.get('dpi', 100), 
                       bbox_inches='tight')
        
        print(f"✅ Saved as {filename}")
    
    plt.show()
    
    # High-resolution export
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'r-', linewidth=4)
    plt.title('High Resolution Export', fontsize=20)
    plt.xlabel('X values', fontsize=16)
    plt.ylabel('Y values', fontsize=16)
    plt.grid(True, alpha=0.3)
    
    # Ultra high resolution
    plt.savefig('high_res_plot.png', dpi=600, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("✅ High resolution plot saved (600 DPI)")
    
    plt.show()

export_options()
```

---

## 🎉 সমাপনী

### ✅ **Matplotlib এ আপনি শিখেছেন:**
- Basic plotting (line, bar, scatter, histogram)
- Advanced customization ও styling
- Statistical visualizations
- Pandas integration
- Multiple export formats
- Professional quality plots

### 🚀 **Next Steps:**
- **Seaborn** দিয়ে statistical plotting
- **Plotly** দিয়ে interactive plots
- **3D plotting** with mplot3d
- **Animation** with matplotlib.animation

**Matplotlib mastery সম্পন্ন! 📊🇧🇩**
