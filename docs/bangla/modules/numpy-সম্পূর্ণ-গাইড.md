# 🔢 NumPy - সম্পূর্ণ বাংলা গাইড

## 🌟 NumPy কি?

NumPy (Numerical Python) হলো Python এর **fundamental package for scientific computing** যা দিয়ে আপনি high-performance numerical operations করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **N-dimensional arrays** - Powerful array objects
- ✅ **Mathematical functions** - Comprehensive math library
- ✅ **Broadcasting** - Element-wise operations
- ✅ **Linear algebra** - Matrix operations
- ✅ **Random number generation** - Statistical functions
- ✅ **Performance** - C-level speed in Python

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# NumPy install
pip install numpy>=1.24.0

# Verify installation
python -c "import numpy as np; print(f'NumPy version: {np.__version__}')"
```

### ✅ **Installation Verify:**
```python
# test_numpy.py
import numpy as np

def test_numpy():
    print("🧪 NumPy installation test...")
    
    # Create array
    arr = np.array([1, 2, 3, 4, 5])
    print(f"✅ Array created: {arr}")
    print(f"✅ Array type: {type(arr)}")
    print(f"✅ Array dtype: {arr.dtype}")
    
    # Basic operations
    result = np.sum(arr)
    print(f"✅ Sum: {result}")
    
    # Matrix operations
    matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(matrix)
    print(f"✅ Matrix determinant: {determinant}")
    
    print("🎉 NumPy working perfectly!")

test_numpy()
```

---

## 📊 Array Creation

### 🔢 **Basic Array Creation:**
```python
import numpy as np

def array_creation():
    """NumPy array creation methods"""
    
    # From Python list
    list_array = np.array([1, 2, 3, 4, 5])
    print(f"From list: {list_array}")
    print(f"Shape: {list_array.shape}, Dtype: {list_array.dtype}")
    
    # 2D array from nested list
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n2D Array:\n{matrix}")
    print(f"Shape: {matrix.shape}, Dimensions: {matrix.ndim}")
    
    # Specify data type
    float_array = np.array([1, 2, 3], dtype=np.float64)
    int_array = np.array([1.5, 2.7, 3.9], dtype=np.int32)
    print(f"\nFloat array: {float_array}")
    print(f"Int array: {int_array}")
    
    # Array from range
    range_array = np.arange(0, 10, 2)  # start, stop, step
    print(f"\nRange array: {range_array}")
    
    # Linearly spaced array
    linear_array = np.linspace(0, 1, 5)  # start, stop, num_points
    print(f"Linear array: {linear_array}")
    
    # Special arrays
    zeros = np.zeros((3, 4))  # 3x4 array of zeros
    ones = np.ones((2, 3))    # 2x3 array of ones
    empty = np.empty((2, 2))  # Uninitialized array
    
    print(f"\nZeros array:\n{zeros}")
    print(f"Ones array:\n{ones}")
    
    # Identity matrix
    identity = np.eye(3)  # 3x3 identity matrix
    print(f"\nIdentity matrix:\n{identity}")
    
    # Array with specific value
    full_array = np.full((2, 3), 7)  # 2x3 array filled with 7
    print(f"Full array:\n{full_array}")

array_creation()
```

### 🎲 **Random Arrays:**
```python
def random_arrays():
    """Random array generation"""
    
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Random floats between 0 and 1
    random_floats = np.random.random((3, 3))
    print(f"Random floats:\n{random_floats}")
    
    # Random integers
    random_ints = np.random.randint(1, 10, size=(2, 4))
    print(f"\nRandom integers:\n{random_ints}")
    
    # Normal distribution
    normal_dist = np.random.normal(0, 1, (3, 3))  # mean=0, std=1
    print(f"\nNormal distribution:\n{normal_dist}")
    
    # Uniform distribution
    uniform_dist = np.random.uniform(-1, 1, (2, 3))  # min=-1, max=1
    print(f"\nUniform distribution:\n{uniform_dist}")
    
    # Random choice from array
    choices = np.random.choice([10, 20, 30, 40], size=(2, 2))
    print(f"\nRandom choices:\n{choices}")
    
    # Random permutation
    original = np.arange(10)
    shuffled = np.random.permutation(original)
    print(f"\nOriginal: {original}")
    print(f"Shuffled: {shuffled}")
    
    # Random sampling without replacement
    sample = np.random.choice(100, size=5, replace=False)
    print(f"\nRandom sample: {sample}")

random_arrays()
```

---

## 🔧 Array Operations

### ➕ **Mathematical Operations:**
```python
def mathematical_operations():
    """Mathematical operations on arrays"""
    
    # Create sample arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    
    print(f"Array a: {a}")
    print(f"Array b: {b}")
    
    # Basic arithmetic (element-wise)
    addition = a + b
    subtraction = b - a
    multiplication = a * b
    division = b / a
    power = a ** 2
    
    print(f"\nAddition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Power (a^2): {power}")
    
    # Mathematical functions
    sqrt_a = np.sqrt(a)
    exp_a = np.exp(a)
    log_b = np.log(b)
    sin_a = np.sin(a)
    
    print(f"\nSquare root of a: {sqrt_a}")
    print(f"Exponential of a: {exp_a}")
    print(f"Natural log of b: {log_b}")
    print(f"Sine of a: {sin_a}")
    
    # Aggregate functions
    print(f"\nSum of a: {np.sum(a)}")
    print(f"Mean of a: {np.mean(a)}")
    print(f"Standard deviation: {np.std(a)}")
    print(f"Min value: {np.min(a)}")
    print(f"Max value: {np.max(a)}")
    print(f"Median: {np.median(a)}")
    
    # 2D array operations
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Sum of all elements: {np.sum(matrix)}")
    print(f"Sum along axis 0 (columns): {np.sum(matrix, axis=0)}")
    print(f"Sum along axis 1 (rows): {np.sum(matrix, axis=1)}")
    print(f"Mean along axis 0: {np.mean(matrix, axis=0)}")

mathematical_operations()
```

### 🔄 **Array Manipulation:**
```python
def array_manipulation():
    """Array shape manipulation"""
    
    # Create sample array
    original = np.arange(12)
    print(f"Original array: {original}")
    print(f"Shape: {original.shape}")
    
    # Reshape
    reshaped_2d = original.reshape(3, 4)
    reshaped_3d = original.reshape(2, 2, 3)
    
    print(f"\nReshaped to 3x4:\n{reshaped_2d}")
    print(f"\nReshaped to 2x2x3:\n{reshaped_3d}")
    
    # Flatten
    flattened = reshaped_2d.flatten()
    print(f"\nFlattened: {flattened}")
    
    # Transpose
    transposed = reshaped_2d.T
    print(f"\nTransposed:\n{transposed}")
    
    # Concatenation
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    concatenated = np.concatenate([arr1, arr2])
    print(f"\nConcatenated: {concatenated}")
    
    # Stack arrays
    stacked_vertical = np.vstack([arr1, arr2])
    stacked_horizontal = np.hstack([arr1, arr2])
    
    print(f"\nVertical stack:\n{stacked_vertical}")
    print(f"Horizontal stack: {stacked_horizontal}")
    
    # Split arrays
    split_arrays = np.split(concatenated, 2)
    print(f"\nSplit arrays: {split_arrays}")
    
    # Add/remove dimensions
    expanded = np.expand_dims(arr1, axis=0)
    squeezed = np.squeeze(expanded)
    
    print(f"\nOriginal shape: {arr1.shape}")
    print(f"Expanded shape: {expanded.shape}")
    print(f"Squeezed shape: {squeezed.shape}")

array_manipulation()
```

---

## 🎯 Indexing ও Slicing

### 🔍 **Array Indexing:**
```python
def array_indexing():
    """Array indexing and slicing"""
    
    # 1D array indexing
    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"First element: {arr[0]}")
    print(f"Last element: {arr[-1]}")
    print(f"Slice [1:4]: {arr[1:4]}")
    print(f"Every 2nd element: {arr[::2]}")
    
    # 2D array indexing
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Element at [1,2]: {matrix[1, 2]}")
    print(f"First row: {matrix[0, :]}")
    print(f"Second column: {matrix[:, 1]}")
    print(f"Submatrix [0:2, 1:3]:\n{matrix[0:2, 1:3]}")
    
    # Boolean indexing
    arr = np.array([1, 5, 3, 8, 2, 7])
    condition = arr > 4
    print(f"\nArray: {arr}")
    print(f"Condition (>4): {condition}")
    print(f"Elements > 4: {arr[condition]}")
    print(f"Elements <= 4: {arr[~condition]}")
    
    # Fancy indexing
    indices = [0, 2, 4]
    selected = arr[indices]
    print(f"\nSelected by indices {indices}: {selected}")
    
    # Multi-condition indexing
    complex_condition = (arr > 2) & (arr < 7)
    print(f"Elements between 2 and 7: {arr[complex_condition]}")
    
    # Where function
    result = np.where(arr > 4, arr, 0)  # Replace values <= 4 with 0
    print(f"Where arr > 4, keep value, else 0: {result}")

array_indexing()
```

---

## 🧮 Linear Algebra

### 📐 **Matrix Operations:**
```python
def linear_algebra():
    """Linear algebra operations"""
    
    # Create matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    
    # Matrix multiplication
    matrix_mult = np.dot(A, B)  # or A @ B
    print(f"\nMatrix multiplication A @ B:\n{matrix_mult}")
    
    # Element-wise multiplication
    element_mult = A * B
    print(f"\nElement-wise multiplication:\n{element_mult}")
    
    # Matrix properties
    print(f"\nDeterminant of A: {np.linalg.det(A)}")
    print(f"Trace of A: {np.trace(A)}")
    print(f"Rank of A: {np.linalg.matrix_rank(A)}")
    
    # Matrix inverse
    try:
        A_inv = np.linalg.inv(A)
        print(f"\nInverse of A:\n{A_inv}")
        
        # Verify inverse
        identity_check = np.dot(A, A_inv)
        print(f"A @ A_inv (should be identity):\n{identity_check}")
        
    except np.linalg.LinAlgError:
        print("Matrix is singular (not invertible)")
    
    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"\nEigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")
    
    # Solve linear system Ax = b
    b = np.array([1, 2])
    x = np.linalg.solve(A, b)
    print(f"\nSolving Ax = b where b = {b}")
    print(f"Solution x: {x}")
    print(f"Verification A @ x: {np.dot(A, x)}")
    
    # SVD (Singular Value Decomposition)
    U, s, Vt = np.linalg.svd(A)
    print(f"\nSVD of A:")
    print(f"U:\n{U}")
    print(f"Singular values: {s}")
    print(f"V transpose:\n{Vt}")

linear_algebra()
```

---

## 📊 Statistics ও Random

### 📈 **Statistical Functions:**
```python
def statistics_functions():
    """Statistical operations"""
    
    # Generate sample data
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)  # mean=100, std=15, size=1000
    
    print(f"Sample data (first 10): {data[:10]}")
    print(f"Data shape: {data.shape}")
    
    # Basic statistics
    print(f"\n📊 Basic Statistics:")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Standard deviation: {np.std(data):.2f}")
    print(f"Variance: {np.var(data):.2f}")
    print(f"Min: {np.min(data):.2f}")
    print(f"Max: {np.max(data):.2f}")
    print(f"Range: {np.ptp(data):.2f}")  # peak-to-peak
    
    # Percentiles
    percentiles = [25, 50, 75, 90, 95, 99]
    print(f"\n📈 Percentiles:")
    for p in percentiles:
        value = np.percentile(data, p)
        print(f"{p}th percentile: {value:.2f}")
    
    # Correlation and covariance
    data2 = data + np.random.normal(0, 5, 1000)  # Correlated data
    
    correlation = np.corrcoef(data, data2)[0, 1]
    covariance = np.cov(data, data2)[0, 1]
    
    print(f"\n🔗 Correlation & Covariance:")
    print(f"Correlation coefficient: {correlation:.3f}")
    print(f"Covariance: {covariance:.2f}")
    
    # Histogram
    hist, bins = np.histogram(data, bins=20)
    print(f"\n📊 Histogram (first 5 bins):")
    for i in range(5):
        print(f"Bin [{bins[i]:.1f}, {bins[i+1]:.1f}): {hist[i]} values")
    
    # 2D statistics
    matrix_data = np.random.random((5, 4))
    print(f"\n🔢 2D Array Statistics:")
    print(f"Matrix:\n{matrix_data}")
    print(f"Mean by columns: {np.mean(matrix_data, axis=0)}")
    print(f"Mean by rows: {np.mean(matrix_data, axis=1)}")
    print(f"Overall mean: {np.mean(matrix_data)}")

statistics_functions()
```

### 🎲 **Advanced Random Operations:**
```python
def advanced_random():
    """Advanced random number generation"""
    
    # Different random distributions
    np.random.seed(42)
    
    # Normal distribution
    normal = np.random.normal(0, 1, 1000)
    
    # Exponential distribution
    exponential = np.random.exponential(2, 1000)
    
    # Poisson distribution
    poisson = np.random.poisson(3, 1000)
    
    # Binomial distribution
    binomial = np.random.binomial(10, 0.3, 1000)
    
    # Uniform distribution
    uniform = np.random.uniform(-5, 5, 1000)
    
    distributions = {
        'Normal': normal,
        'Exponential': exponential,
        'Poisson': poisson,
        'Binomial': binomial,
        'Uniform': uniform
    }
    
    print("📊 Distribution Statistics:")
    for name, dist in distributions.items():
        print(f"\n{name} Distribution:")
        print(f"  Mean: {np.mean(dist):.3f}")
        print(f"  Std: {np.std(dist):.3f}")
        print(f"  Min: {np.min(dist):.3f}")
        print(f"  Max: {np.max(dist):.3f}")
    
    # Random sampling techniques
    population = np.arange(1, 101)  # 1 to 100
    
    # Simple random sampling
    simple_sample = np.random.choice(population, size=10, replace=False)
    print(f"\n🎯 Sampling Techniques:")
    print(f"Simple random sample: {simple_sample}")
    
    # Weighted sampling
    weights = np.arange(1, 101)  # Higher numbers more likely
    weighted_sample = np.random.choice(population, size=10, p=weights/np.sum(weights))
    print(f"Weighted sample: {weighted_sample}")
    
    # Stratified sampling simulation
    strata = [population[:25], population[25:50], population[50:75], population[75:]]
    stratified_sample = []
    
    for stratum in strata:
        sample = np.random.choice(stratum, size=2, replace=False)
        stratified_sample.extend(sample)
    
    print(f"Stratified sample: {stratified_sample}")

advanced_random()
```

---

## 🎯 Performance ও Broadcasting

### ⚡ **Performance Comparison:**
```python
import time

def performance_comparison():
    """NumPy vs Python performance"""
    
    # Large arrays for testing
    size = 1000000
    
    # Python list operations
    python_list1 = list(range(size))
    python_list2 = list(range(size, 2*size))
    
    # NumPy array operations
    numpy_array1 = np.arange(size)
    numpy_array2 = np.arange(size, 2*size)
    
    print(f"🏃‍♂️ Performance Comparison (size: {size:,})")
    
    # Addition comparison
    # Python list addition
    start_time = time.time()
    python_result = [a + b for a, b in zip(python_list1, python_list2)]
    python_time = time.time() - start_time
    
    # NumPy array addition
    start_time = time.time()
    numpy_result = numpy_array1 + numpy_array2
    numpy_time = time.time() - start_time
    
    print(f"\n➕ Addition:")
    print(f"Python list: {python_time:.4f} seconds")
    print(f"NumPy array: {numpy_time:.4f} seconds")
    print(f"NumPy is {python_time/numpy_time:.1f}x faster")
    
    # Mathematical operations comparison
    # Python list square root
    start_time = time.time()
    python_sqrt = [x**0.5 for x in python_list1]
    python_sqrt_time = time.time() - start_time
    
    # NumPy array square root
    start_time = time.time()
    numpy_sqrt = np.sqrt(numpy_array1)
    numpy_sqrt_time = time.time() - start_time
    
    print(f"\n√ Square Root:")
    print(f"Python list: {python_sqrt_time:.4f} seconds")
    print(f"NumPy array: {numpy_sqrt_time:.4f} seconds")
    print(f"NumPy is {python_sqrt_time/numpy_sqrt_time:.1f}x faster")
    
    # Memory usage comparison
    import sys
    
    python_memory = sys.getsizeof(python_list1)
    numpy_memory = numpy_array1.nbytes
    
    print(f"\n💾 Memory Usage:")
    print(f"Python list: {python_memory:,} bytes")
    print(f"NumPy array: {numpy_memory:,} bytes")
    print(f"NumPy uses {python_memory/numpy_memory:.1f}x less memory")

performance_comparison()
```

### 📡 **Broadcasting:**
```python
def broadcasting_examples():
    """NumPy broadcasting examples"""
    
    print("📡 Broadcasting Examples:")
    
    # Scalar with array
    arr = np.array([1, 2, 3, 4, 5])
    scalar = 10
    
    result = arr + scalar
    print(f"Array + Scalar: {arr} + {scalar} = {result}")
    
    # 1D array with 2D array
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[10], [20], [30]])
    
    print(f"\n1D array: {arr_1d}")
    print(f"2D array:\n{arr_2d}")
    
    result_2d = arr_1d + arr_2d
    print(f"Broadcasting result:\n{result_2d}")
    
    # Different shapes
    a = np.array([[1, 2, 3]])      # Shape: (1, 3)
    b = np.array([[4], [5], [6]])  # Shape: (3, 1)
    
    print(f"\nArray a (1x3): {a}")
    print(f"Array b (3x1):\n{b}")
    
    result = a * b  # Broadcasting to (3, 3)
    print(f"Broadcasting multiplication:\n{result}")
    
    # Broadcasting rules demonstration
    print(f"\n📏 Broadcasting Rules:")
    print(f"Rule 1: Arrays are aligned from the rightmost dimension")
    print(f"Rule 2: Dimensions of size 1 are stretched")
    print(f"Rule 3: Missing dimensions are assumed to be 1")
    
    # Complex broadcasting example
    x = np.arange(12).reshape(3, 4)  # Shape: (3, 4)
    y = np.arange(4)                 # Shape: (4,)
    z = np.arange(3).reshape(3, 1)   # Shape: (3, 1)
    
    print(f"\nComplex Broadcasting:")
    print(f"x (3x4):\n{x}")
    print(f"y (4,): {y}")
    print(f"z (3x1):\n{z}")
    
    result_xy = x + y  # (3,4) + (4,) -> (3,4)
    result_xz = x + z  # (3,4) + (3,1) -> (3,4)
    
    print(f"\nx + y:\n{result_xy}")
    print(f"\nx + z:\n{result_xz}")

broadcasting_examples()
```

---

## 🎉 সমাপনী

### ✅ **NumPy এ আপনি শিখেছেন:**
- Array creation ও manipulation
- Mathematical operations ও functions
- Indexing, slicing ও boolean operations
- Linear algebra ও matrix operations
- Statistical functions ও random generation
- Performance optimization ও broadcasting
- Real-world numerical computing

### 🚀 **Next Steps:**
- **Pandas** দিয়ে data analysis
- **SciPy** দিয়ে scientific computing
- **Matplotlib** দিয়ে data visualization
- **Machine Learning** with scikit-learn

**NumPy mastery সম্পন্ন! 🔢🇧🇩**
