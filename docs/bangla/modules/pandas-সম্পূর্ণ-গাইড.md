# 🐼 Pandas - সম্পূর্ণ বাংলা গাইড

## 🌟 Pandas কি?

Pandas হলো Python এর সবচেয়ে শক্তিশালী **data manipulation ও analysis library** যা দিয়ে আপনি সহজেই structured data নিয়ে কাজ করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **DataFrame ও Series** - Powerful data structures
- ✅ **Data cleaning** - Missing data handling
- ✅ **File I/O** - CSV, Excel, JSON, SQL support
- ✅ **Data transformation** - Grouping, merging, reshaping
- ✅ **Statistical analysis** - Descriptive statistics
- ✅ **Time series** - Date/time data handling

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# Pandas install
pip install pandas>=2.1.0

# Additional dependencies
pip install numpy>=1.24.0      # Numerical computing
pip install openpyxl>=3.1.0     # Excel support
pip install xlsxwriter>=3.1.0   # Excel writing
```

### ✅ **Installation Verify:**
```python
# test_pandas.py
import pandas as pd
import numpy as np

def test_pandas():
    print("🧪 Pandas installation test...")
    
    # Create sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['Dhaka', 'Chittagong', 'Sylhet']
    }
    
    df = pd.DataFrame(data)
    print("✅ DataFrame created:")
    print(df)
    
    # Basic operations
    print(f"✅ Shape: {df.shape}")
    print(f"✅ Columns: {list(df.columns)}")
    print("🎉 Pandas working perfectly!")

test_pandas()
```

---

## 📊 Data Structures

### 📋 **Series (1D Data):**
```python
import pandas as pd
import numpy as np

def series_examples():
    """Pandas Series examples"""
    
    # Create Series from list
    ages = pd.Series([25, 30, 35, 40])
    print("Series from list:")
    print(ages)
    print(f"Data type: {ages.dtype}")
    
    # Series with custom index
    names_ages = pd.Series([25, 30, 35], index=['Alice', 'Bob', 'Charlie'])
    print("\nSeries with custom index:")
    print(names_ages)
    
    # Series from dictionary
    cities = pd.Series({
        'Dhaka': 9000000,
        'Chittagong': 2500000,
        'Sylhet': 500000
    })
    print("\nSeries from dictionary:")
    print(cities)
    
    # Series operations
    print(f"\nMax age: {names_ages.max()}")
    print(f"Mean age: {names_ages.mean()}")
    print(f"Age of Bob: {names_ages['Bob']}")
    
    # Boolean indexing
    older_than_30 = names_ages[names_ages > 30]
    print(f"\nPeople older than 30:")
    print(older_than_30)

series_examples()
```

### 📊 **DataFrame (2D Data):**
```python
def dataframe_examples():
    """Pandas DataFrame examples"""
    
    # Create DataFrame from dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi'],
        'Salary': [50000, 60000, 70000, 55000],
        'Department': ['IT', 'Finance', 'HR', 'IT']
    }
    
    df = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df)
    
    # DataFrame info
    print(f"\nShape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Index: {list(df.index)}")
    print(f"Data types:\n{df.dtypes}")
    
    # Basic statistics
    print(f"\nBasic statistics:")
    print(df.describe())
    
    # Column access
    print(f"\nNames column:")
    print(df['Name'])
    
    # Multiple columns
    print(f"\nName and Age columns:")
    print(df[['Name', 'Age']])
    
    # Row access
    print(f"\nFirst row:")
    print(df.iloc[0])
    
    # Conditional selection
    it_employees = df[df['Department'] == 'IT']
    print(f"\nIT employees:")
    print(it_employees)

dataframe_examples()
```

---

## 📁 File Operations

### 📄 **CSV Operations:**
```python
def csv_operations():
    """CSV file operations"""
    
    # Create sample data
    data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphone'],
        'Price': [50000, 1500, 3000, 25000, 8000],
        'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
        'Stock': [10, 50, 30, 15, 25],
        'Rating': [4.5, 4.0, 4.2, 4.8, 4.3]
    }
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('products.csv', index=False, encoding='utf-8')
    print("✅ Data saved to products.csv")
    
    # Read from CSV
    loaded_df = pd.read_csv('products.csv')
    print("✅ Data loaded from CSV:")
    print(loaded_df)
    
    # CSV with custom options
    df.to_csv('products_custom.csv', 
              index=False, 
              encoding='utf-8',
              sep=';',  # Custom separator
              columns=['Product', 'Price', 'Rating'])  # Specific columns
    
    # Read with custom options
    custom_df = pd.read_csv('products_custom.csv', 
                           sep=';',
                           usecols=['Product', 'Price'])  # Specific columns
    
    print("✅ Custom CSV loaded:")
    print(custom_df)

csv_operations()
```

### 📊 **Excel Operations:**
```python
def excel_operations():
    """Excel file operations"""
    
    # Create sample data
    sales_data = {
        'Month': ['January', 'February', 'March', 'April', 'May'],
        'Sales': [100000, 120000, 110000, 130000, 140000],
        'Expenses': [80000, 90000, 85000, 95000, 100000],
        'Profit': [20000, 30000, 25000, 35000, 40000]
    }
    
    df = pd.DataFrame(sales_data)
    
    # Save to Excel
    df.to_excel('sales_report.xlsx', index=False, sheet_name='Monthly_Sales')
    print("✅ Data saved to Excel")
    
    # Read from Excel
    loaded_df = pd.read_excel('sales_report.xlsx', sheet_name='Monthly_Sales')
    print("✅ Data loaded from Excel:")
    print(loaded_df)
    
    # Multiple sheets
    with pd.ExcelWriter('multi_sheet_report.xlsx') as writer:
        df.to_excel(writer, sheet_name='Sales', index=False)
        
        # Create another sheet
        summary_data = {
            'Metric': ['Total Sales', 'Total Expenses', 'Total Profit'],
            'Value': [df['Sales'].sum(), df['Expenses'].sum(), df['Profit'].sum()]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    print("✅ Multi-sheet Excel created")
    
    # Read specific sheet
    summary = pd.read_excel('multi_sheet_report.xlsx', sheet_name='Summary')
    print("Summary sheet:")
    print(summary)

excel_operations()
```

### 🔗 **JSON Operations:**
```python
def json_operations():
    """JSON file operations"""
    
    # Create sample data
    employees = {
        'Employee_ID': [1, 2, 3, 4],
        'Name': ['Alice Ahmed', 'Bob Rahman', 'Charlie Khan', 'Diana Islam'],
        'Position': ['Developer', 'Designer', 'Manager', 'Analyst'],
        'Salary': [60000, 55000, 80000, 50000],
        'Join_Date': ['2020-01-15', '2019-06-20', '2018-03-10', '2021-09-05']
    }
    
    df = pd.DataFrame(employees)
    
    # Convert Join_Date to datetime
    df['Join_Date'] = pd.to_datetime(df['Join_Date'])
    
    # Save to JSON
    df.to_json('employees.json', orient='records', date_format='iso', indent=2)
    print("✅ Data saved to JSON")
    
    # Read from JSON
    loaded_df = pd.read_json('employees.json')
    print("✅ Data loaded from JSON:")
    print(loaded_df)
    
    # Different JSON orientations
    # Records format
    records_json = df.to_json(orient='records', date_format='iso')
    print("Records format JSON:")
    print(records_json[:100] + "...")
    
    # Index format
    index_json = df.to_json(orient='index', date_format='iso')
    print("Index format JSON:")
    print(index_json[:100] + "...")

json_operations()
```

---

## 🔍 Data Exploration

### 📊 **Basic Information:**
```python
def data_exploration():
    """Data exploration techniques"""
    
    # Create sample dataset
    np.random.seed(42)
    
    data = {
        'Name': [f'Person_{i}' for i in range(1, 101)],
        'Age': np.random.randint(18, 65, 100),
        'Salary': np.random.normal(50000, 15000, 100),
        'Department': np.random.choice(['IT', 'Finance', 'HR', 'Marketing'], 100),
        'Experience': np.random.randint(0, 20, 100),
        'City': np.random.choice(['Dhaka', 'Chittagong', 'Sylhet', 'Rajshahi'], 100)
    }
    
    df = pd.DataFrame(data)
    df['Salary'] = df['Salary'].round(2)  # Round salary
    
    # Basic info
    print("Dataset shape:", df.shape)
    print("\nColumn names:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)
    
    # First and last rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nLast 5 rows:")
    print(df.tail())
    
    # Statistical summary
    print("\nStatistical summary:")
    print(df.describe())
    
    # Info about dataset
    print("\nDataset info:")
    df.info()
    
    # Unique values
    print(f"\nUnique departments: {df['Department'].unique()}")
    print(f"Department counts:")
    print(df['Department'].value_counts())
    
    # Missing values check
    print(f"\nMissing values:")
    print(df.isnull().sum())

data_exploration()
```

### 🔍 **Filtering ও Selection:**
```python
def filtering_selection():
    """Data filtering and selection"""
    
    # Use previous dataset
    np.random.seed(42)
    data = {
        'Name': [f'Person_{i}' for i in range(1, 21)],
        'Age': np.random.randint(18, 65, 20),
        'Salary': np.random.normal(50000, 15000, 20),
        'Department': np.random.choice(['IT', 'Finance', 'HR', 'Marketing'], 20),
        'Experience': np.random.randint(0, 20, 20)
    }
    
    df = pd.DataFrame(data)
    df['Salary'] = df['Salary'].round(2)
    
    # Single condition filtering
    it_employees = df[df['Department'] == 'IT']
    print("IT employees:")
    print(it_employees)
    
    # Multiple conditions
    senior_it = df[(df['Department'] == 'IT') & (df['Experience'] > 5)]
    print(f"\nSenior IT employees: {len(senior_it)}")
    
    # Salary range
    high_earners = df[df['Salary'] > 60000]
    print(f"\nHigh earners (>60k): {len(high_earners)}")
    
    # Multiple values
    tech_finance = df[df['Department'].isin(['IT', 'Finance'])]
    print(f"\nIT & Finance employees: {len(tech_finance)}")
    
    # String operations
    df['Name_Length'] = df['Name'].str.len()
    long_names = df[df['Name_Length'] > 8]
    print(f"\nPeople with long names: {len(long_names)}")
    
    # Query method
    query_result = df.query('Age > 30 and Salary < 50000')
    print(f"\nQuery result: {len(query_result)} people")
    
    # Top N values
    top_earners = df.nlargest(5, 'Salary')
    print("\nTop 5 earners:")
    print(top_earners[['Name', 'Salary']])

filtering_selection()
```

---

## 🔄 Data Transformation

### 🧹 **Data Cleaning:**
```python
def data_cleaning():
    """Data cleaning techniques"""
    
    # Create messy dataset
    messy_data = {
        'Name': ['Alice Ahmed', 'Bob Rahman', '', 'Charlie Khan', None, 'Diana Islam'],
        'Age': [25, 30, np.nan, 35, 28, 45],
        'Email': ['alice@email.com', 'BOB@EMAIL.COM', 'invalid-email', 
                 'charlie@email.com', '', 'diana@email.com'],
        'Salary': [50000, 60000, 0, 70000, np.nan, 55000],
        'Phone': ['01712345678', '880171234567', '123', '01798765432', '', '01687654321']
    }
    
    df = pd.DataFrame(messy_data)
    print("Original messy data:")
    print(df)
    
    # Check missing values
    print(f"\nMissing values:")
    print(df.isnull().sum())
    
    # Drop rows with missing names
    df_clean = df.dropna(subset=['Name'])
    print(f"\nAfter dropping missing names: {len(df_clean)} rows")
    
    # Fill missing ages with mean
    df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].mean())
    
    # Fill missing salary with median
    df_clean['Salary'] = df_clean['Salary'].fillna(df_clean['Salary'].median())
    
    # Clean email addresses
    df_clean['Email'] = df_clean['Email'].str.lower()
    df_clean['Email'] = df_clean['Email'].replace('', np.nan)
    
    # Validate emails (simple check)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    df_clean['Valid_Email'] = df_clean['Email'].str.match(email_pattern, na=False)
    
    # Clean phone numbers
    df_clean['Phone_Clean'] = df_clean['Phone'].str.replace(r'[^\d]', '', regex=True)
    df_clean['Phone_Clean'] = df_clean['Phone_Clean'].str.replace(r'^880', '', regex=True)
    
    # Remove invalid entries
    df_clean = df_clean[df_clean['Salary'] > 0]  # Remove zero salaries
    df_clean = df_clean[df_clean['Phone_Clean'].str.len() >= 10]  # Valid phone length
    
    print("\nCleaned data:")
    print(df_clean)
    
    # Data validation summary
    print(f"\nData validation:")
    print(f"Valid emails: {df_clean['Valid_Email'].sum()}")
    print(f"Average age: {df_clean['Age'].mean():.1f}")
    print(f"Salary range: {df_clean['Salary'].min()} - {df_clean['Salary'].max()}")

data_cleaning()
```

### 🔄 **Data Transformation:**
```python
def data_transformation():
    """Data transformation techniques"""
    
    # Create sample data
    sales_data = {
        'Date': pd.date_range('2023-01-01', periods=12, freq='M'),
        'Product': ['Laptop', 'Mouse', 'Keyboard'] * 4,
        'Sales': [100, 200, 150, 120, 180, 160, 140, 220, 170, 110, 190, 180],
        'Region': ['North', 'South'] * 6
    }
    
    df = pd.DataFrame(sales_data)
    
    # Add calculated columns
    df['Quarter'] = df['Date'].dt.quarter
    df['Month_Name'] = df['Date'].dt.month_name()
    df['Sales_Category'] = pd.cut(df['Sales'], 
                                 bins=[0, 150, 200, float('inf')], 
                                 labels=['Low', 'Medium', 'High'])
    
    print("Data with new columns:")
    print(df.head())
    
    # Group by operations
    monthly_sales = df.groupby('Month_Name')['Sales'].sum().sort_values(ascending=False)
    print(f"\nMonthly sales (sorted):")
    print(monthly_sales)
    
    # Multiple aggregations
    product_stats = df.groupby('Product').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Region': 'nunique'
    }).round(2)
    
    print(f"\nProduct statistics:")
    print(product_stats)
    
    # Pivot table
    pivot_table = df.pivot_table(
        values='Sales',
        index='Product',
        columns='Region',
        aggfunc='sum',
        fill_value=0
    )
    
    print(f"\nPivot table:")
    print(pivot_table)
    
    # Melting (unpivot)
    melted = pivot_table.reset_index().melt(
        id_vars='Product',
        var_name='Region',
        value_name='Total_Sales'
    )
    
    print(f"\nMelted data:")
    print(melted)

data_transformation()
```

---

## 📈 Statistical Analysis

### 📊 **Descriptive Statistics:**
```python
def descriptive_statistics():
    """Descriptive statistics examples"""
    
    # Create sample dataset
    np.random.seed(42)
    
    data = {
        'Student_ID': range(1, 101),
        'Math_Score': np.random.normal(75, 15, 100),
        'Science_Score': np.random.normal(80, 12, 100),
        'English_Score': np.random.normal(70, 18, 100),
        'Grade': np.random.choice(['A', 'B', 'C', 'D'], 100, p=[0.2, 0.3, 0.3, 0.2])
    }
    
    df = pd.DataFrame(data)
    
    # Round scores
    score_columns = ['Math_Score', 'Science_Score', 'English_Score']
    df[score_columns] = df[score_columns].round(1)
    
    # Basic statistics
    print("Basic statistics:")
    print(df[score_columns].describe())
    
    # Individual statistics
    print(f"\nMath Score Statistics:")
    print(f"Mean: {df['Math_Score'].mean():.2f}")
    print(f"Median: {df['Math_Score'].median():.2f}")
    print(f"Mode: {df['Math_Score'].mode().iloc[0]:.2f}")
    print(f"Standard Deviation: {df['Math_Score'].std():.2f}")
    print(f"Variance: {df['Math_Score'].var():.2f}")
    
    # Percentiles
    print(f"\nPercentiles:")
    percentiles = [25, 50, 75, 90, 95]
    for p in percentiles:
        value = df['Math_Score'].quantile(p/100)
        print(f"{p}th percentile: {value:.2f}")
    
    # Correlation analysis
    correlation_matrix = df[score_columns].corr()
    print(f"\nCorrelation matrix:")
    print(correlation_matrix.round(3))
    
    # Grade distribution
    grade_distribution = df['Grade'].value_counts().sort_index()
    print(f"\nGrade distribution:")
    print(grade_distribution)
    
    # Cross-tabulation
    df['Math_Category'] = pd.cut(df['Math_Score'], 
                                bins=[0, 60, 80, 100], 
                                labels=['Below Average', 'Average', 'Above Average'])
    
    crosstab = pd.crosstab(df['Grade'], df['Math_Category'])
    print(f"\nGrade vs Math Category:")
    print(crosstab)

descriptive_statistics()
```

---

## 🎯 Advanced Operations

### 🔗 **Merging ও Joining:**
```python
def merging_joining():
    """Data merging and joining"""
    
    # Create sample datasets
    employees = pd.DataFrame({
        'Employee_ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Department_ID': [101, 102, 101, 103, 102]
    })
    
    departments = pd.DataFrame({
        'Department_ID': [101, 102, 103, 104],
        'Department_Name': ['IT', 'Finance', 'HR', 'Marketing'],
        'Budget': [500000, 300000, 200000, 250000]
    })
    
    salaries = pd.DataFrame({
        'Employee_ID': [1, 2, 3, 4, 6],
        'Salary': [60000, 55000, 65000, 50000, 58000],
        'Bonus': [5000, 4000, 6000, 4500, 5500]
    })
    
    print("Employees:")
    print(employees)
    print("\nDepartments:")
    print(departments)
    print("\nSalaries:")
    print(salaries)
    
    # Inner join
    emp_dept = pd.merge(employees, departments, on='Department_ID', how='inner')
    print(f"\nInner join (employees + departments):")
    print(emp_dept)
    
    # Left join
    emp_salary = pd.merge(employees, salaries, on='Employee_ID', how='left')
    print(f"\nLeft join (employees + salaries):")
    print(emp_salary)
    
    # Outer join
    all_data = pd.merge(employees, salaries, on='Employee_ID', how='outer')
    print(f"\nOuter join:")
    print(all_data)
    
    # Multiple joins
    complete_data = employees.merge(departments, on='Department_ID') \
                            .merge(salaries, on='Employee_ID', how='left')
    
    print(f"\nComplete data (multiple joins):")
    print(complete_data)
    
    # Concatenation
    more_employees = pd.DataFrame({
        'Employee_ID': [6, 7],
        'Name': ['Frank', 'Grace'],
        'Department_ID': [104, 101]
    })
    
    all_employees = pd.concat([employees, more_employees], ignore_index=True)
    print(f"\nConcatenated employees:")
    print(all_employees)

merging_joining()
```

---

## 🎉 সমাপনী

### ✅ **Pandas এ আপনি শিখেছেন:**
- Series ও DataFrame data structures
- File operations (CSV, Excel, JSON)
- Data exploration ও filtering
- Data cleaning ও transformation
- Statistical analysis
- Merging ও joining operations

### 🚀 **Next Steps:**
- **Matplotlib/Seaborn** দিয়ে data visualization
- **NumPy** এর সাথে advanced numerical operations
- **Machine Learning** with scikit-learn
- **Time series analysis** with pandas

**Pandas mastery সম্পন্ন! 🐼🇧🇩**
