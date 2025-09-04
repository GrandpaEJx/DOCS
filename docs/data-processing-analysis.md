# 📊 Data Processing ও Analysis - Complete Guide

## 📚 সূচিপত্র
1. [Data Cleaning ও Preprocessing](#data-cleaning)
2. [CSV/Excel Processing](#csv-excel)
3. [JSON Data Manipulation](#json-manipulation)
4. [Database Operations](#database-operations)
5. [Data Visualization](#data-visualization)
6. [Statistical Analysis](#statistical-analysis)

---

## 🧹 Data Cleaning ও Preprocessing {#data-cleaning}

### Advanced Data Cleaning:
```python
import pandas as pd
import numpy as np
import re
from datetime import datetime
import json

class DataCleaner:
    def __init__(self):
        self.cleaning_log = []
        self.original_shape = None
        self.cleaned_shape = None
    
    def load_data(self, file_path, file_type='auto'):
        """Data load করা different formats থেকে"""
        
        try:
            if file_type == 'auto':
                file_type = file_path.split('.')[-1].lower()
            
            if file_type in ['csv']:
                # Try different encodings
                encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
                for encoding in encodings:
                    try:
                        df = pd.read_csv(file_path, encoding=encoding)
                        print(f"✅ CSV loaded with {encoding} encoding")
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    raise ValueError("Could not decode CSV file")
            
            elif file_type in ['xlsx', 'xls']:
                df = pd.read_excel(file_path)
                print("✅ Excel file loaded")
            
            elif file_type == 'json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                df = pd.json_normalize(data)
                print("✅ JSON file loaded")
            
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
            
            self.original_shape = df.shape
            print(f"📊 Data shape: {df.shape[0]} rows, {df.shape[1]} columns")
            
            return df
            
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def basic_info(self, df):
        """Data এর basic information"""
        
        print("\n📋 Dataset Information:")
        print(f"Shape: {df.shape}")
        print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        print("\n📊 Column Information:")
        for col in df.columns:
            dtype = df[col].dtype
            null_count = df[col].isnull().sum()
            null_percent = (null_count / len(df)) * 100
            unique_count = df[col].nunique()
            
            print(f"  {col}:")
            print(f"    Type: {dtype}")
            print(f"    Null: {null_count} ({null_percent:.1f}%)")
            print(f"    Unique: {unique_count}")
        
        return df.info()
    
    def clean_text_columns(self, df, text_columns=None):
        """Text columns clean করা"""
        
        if text_columns is None:
            text_columns = df.select_dtypes(include=['object']).columns
        
        cleaned_count = 0
        
        for col in text_columns:
            if col in df.columns:
                original_nulls = df[col].isnull().sum()
                
                # Remove extra whitespaces
                df[col] = df[col].astype(str).str.strip()
                
                # Replace empty strings with NaN
                df[col] = df[col].replace('', np.nan)
                df[col] = df[col].replace('nan', np.nan)
                
                # Remove special characters (optional)
                # df[col] = df[col].str.replace(r'[^\w\s]', '', regex=True)
                
                # Standardize case (optional)
                # df[col] = df[col].str.title()
                
                new_nulls = df[col].isnull().sum()
                
                if new_nulls != original_nulls:
                    cleaned_count += 1
                    self.cleaning_log.append(f"Cleaned text column: {col}")
        
        print(f"🧹 Cleaned {cleaned_count} text columns")
        return df
    
    def clean_numeric_columns(self, df, numeric_columns=None):
        """Numeric columns clean করা"""
        
        if numeric_columns is None:
            numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        cleaned_count = 0
        
        for col in numeric_columns:
            if col in df.columns:
                original_nulls = df[col].isnull().sum()
                
                # Remove outliers using IQR method
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers_count = len(df[(df[col] < lower_bound) | (df[col] > upper_bound)])
                
                if outliers_count > 0:
                    print(f"⚠️ Found {outliers_count} outliers in {col}")
                    # Option 1: Remove outliers
                    # df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
                    
                    # Option 2: Cap outliers
                    df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
                    cleaned_count += 1
                    self.cleaning_log.append(f"Capped outliers in: {col}")
        
        print(f"🔢 Cleaned {cleaned_count} numeric columns")
        return df
    
    def handle_missing_values(self, df, strategy='auto'):
        """Missing values handle করা"""
        
        missing_summary = df.isnull().sum()
        missing_columns = missing_summary[missing_summary > 0]
        
        if len(missing_columns) == 0:
            print("✅ No missing values found")
            return df
        
        print(f"🔍 Found missing values in {len(missing_columns)} columns:")
        
        for col, missing_count in missing_columns.items():
            missing_percent = (missing_count / len(df)) * 100
            print(f"  {col}: {missing_count} ({missing_percent:.1f}%)")
            
            if strategy == 'auto':
                if missing_percent > 50:
                    # Drop column if more than 50% missing
                    df = df.drop(columns=[col])
                    self.cleaning_log.append(f"Dropped column (>50% missing): {col}")
                    print(f"    🗑️ Dropped column: {col}")
                
                elif df[col].dtype in ['object']:
                    # Fill with mode for categorical
                    mode_value = df[col].mode().iloc[0] if not df[col].mode().empty else 'Unknown'
                    df[col] = df[col].fillna(mode_value)
                    self.cleaning_log.append(f"Filled with mode: {col}")
                    print(f"    📝 Filled with mode: {mode_value}")
                
                else:
                    # Fill with median for numeric
                    median_value = df[col].median()
                    df[col] = df[col].fillna(median_value)
                    self.cleaning_log.append(f"Filled with median: {col}")
                    print(f"    🔢 Filled with median: {median_value}")
        
        return df
    
    def remove_duplicates(self, df, subset=None):
        """Duplicate rows remove করা"""
        
        original_count = len(df)
        
        if subset:
            df = df.drop_duplicates(subset=subset)
        else:
            df = df.drop_duplicates()
        
        removed_count = original_count - len(df)
        
        if removed_count > 0:
            print(f"🔄 Removed {removed_count} duplicate rows")
            self.cleaning_log.append(f"Removed {removed_count} duplicates")
        else:
            print("✅ No duplicates found")
        
        return df
    
    def standardize_date_columns(self, df, date_columns=None):
        """Date columns standardize করা"""
        
        if date_columns is None:
            # Auto-detect date columns
            date_columns = []
            for col in df.columns:
                if df[col].dtype == 'object':
                    # Check if column contains date-like strings
                    sample = df[col].dropna().iloc[:100] if len(df[col].dropna()) > 0 else []
                    date_like_count = 0
                    
                    for value in sample:
                        if isinstance(value, str):
                            # Check for common date patterns
                            date_patterns = [
                                r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
                                r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
                                r'\d{2}-\d{2}-\d{4}',  # MM-DD-YYYY
                            ]
                            
                            for pattern in date_patterns:
                                if re.search(pattern, str(value)):
                                    date_like_count += 1
                                    break
                    
                    if date_like_count > len(sample) * 0.5:  # 50% threshold
                        date_columns.append(col)
        
        converted_count = 0
        
        for col in date_columns:
            if col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                    converted_count += 1
                    self.cleaning_log.append(f"Converted to datetime: {col}")
                    print(f"📅 Converted {col} to datetime")
                except Exception as e:
                    print(f"⚠️ Could not convert {col} to datetime: {e}")
        
        return df
    
    def comprehensive_clean(self, df):
        """Comprehensive data cleaning"""
        
        print("🚀 Starting comprehensive data cleaning...")
        
        # Basic info
        self.basic_info(df)
        
        # Clean text columns
        df = self.clean_text_columns(df)
        
        # Clean numeric columns
        df = self.clean_numeric_columns(df)
        
        # Handle missing values
        df = self.handle_missing_values(df)
        
        # Remove duplicates
        df = self.remove_duplicates(df)
        
        # Standardize dates
        df = self.standardize_date_columns(df)
        
        self.cleaned_shape = df.shape
        
        print(f"\n🎉 Cleaning completed!")
        print(f"Original shape: {self.original_shape}")
        print(f"Cleaned shape: {self.cleaned_shape}")
        
        return df
    
    def save_cleaning_report(self, filename="cleaning_report.txt"):
        """Cleaning report save করা"""
        
        with open(filename, 'w') as f:
            f.write("Data Cleaning Report\n")
            f.write("===================\n\n")
            f.write(f"Original shape: {self.original_shape}\n")
            f.write(f"Cleaned shape: {self.cleaned_shape}\n\n")
            f.write("Cleaning steps performed:\n")
            
            for i, step in enumerate(self.cleaning_log, 1):
                f.write(f"{i}. {step}\n")
        
        print(f"📄 Cleaning report saved: {filename}")

# Usage
def data_cleaning_example():
    """Data cleaning example"""
    
    cleaner = DataCleaner()
    
    # Load data
    df = cleaner.load_data("sample_data.csv")
    
    if df is not None:
        # Comprehensive cleaning
        cleaned_df = cleaner.comprehensive_clean(df)
        
        # Save cleaned data
        cleaned_df.to_csv("cleaned_data.csv", index=False)
        print("💾 Cleaned data saved")
        
        # Save cleaning report
        cleaner.save_cleaning_report()

# data_cleaning_example()
```

---

## 📄 CSV/Excel Processing {#csv-excel}

### Advanced CSV/Excel Operations:
```python
class ExcelProcessor:
    def __init__(self):
        self.workbooks = {}
    
    def read_multiple_sheets(self, file_path):
        """Multiple sheets read করা"""
        
        try:
            # Read all sheets
            all_sheets = pd.read_excel(file_path, sheet_name=None)
            
            print(f"📊 Found {len(all_sheets)} sheets:")
            for sheet_name, df in all_sheets.items():
                print(f"  {sheet_name}: {df.shape[0]} rows, {df.shape[1]} columns")
            
            return all_sheets
            
        except Exception as e:
            print(f"❌ Error reading Excel file: {e}")
            return None
    
    def merge_sheets(self, sheets_dict, merge_type='concat'):
        """Multiple sheets merge করা"""
        
        if merge_type == 'concat':
            # Concatenate all sheets
            merged_df = pd.concat(sheets_dict.values(), ignore_index=True)
            
            # Add source sheet column
            source_column = []
            for sheet_name, df in sheets_dict.items():
                source_column.extend([sheet_name] * len(df))
            
            merged_df['source_sheet'] = source_column
            
            print(f"🔗 Merged {len(sheets_dict)} sheets: {merged_df.shape}")
            return merged_df
        
        elif merge_type == 'join':
            # Join sheets on common columns
            merged_df = None
            
            for sheet_name, df in sheets_dict.items():
                if merged_df is None:
                    merged_df = df
                else:
                    # Find common columns
                    common_cols = list(set(merged_df.columns) & set(df.columns))
                    
                    if common_cols:
                        merged_df = pd.merge(merged_df, df, on=common_cols, how='outer')
                        print(f"🔗 Joined {sheet_name} on {common_cols}")
                    else:
                        print(f"⚠️ No common columns with {sheet_name}")
            
            return merged_df
    
    def create_excel_report(self, data_dict, output_file):
        """Multiple DataFrames থেকে Excel report তৈরি"""
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet_name, df in data_dict.items():
                # Write data to sheet
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Get worksheet for formatting
                worksheet = writer.sheets[sheet_name]
                
                # Auto-adjust column widths
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    
                    adjusted_width = min(max_length + 2, 50)
                    worksheet.column_dimensions[column_letter].width = adjusted_width
                
                # Add header formatting
                from openpyxl.styles import Font, PatternFill
                
                header_font = Font(bold=True, color="FFFFFF")
                header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
                
                for cell in worksheet[1]:
                    cell.font = header_font
                    cell.fill = header_fill
        
        print(f"📊 Excel report created: {output_file}")
    
    def csv_to_excel_converter(self, csv_files, output_file):
        """Multiple CSV files কে Excel এ convert করা"""
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for csv_file in csv_files:
                try:
                    # Read CSV
                    df = pd.read_csv(csv_file)
                    
                    # Sheet name from filename
                    sheet_name = os.path.splitext(os.path.basename(csv_file))[0]
                    sheet_name = sheet_name[:31]  # Excel sheet name limit
                    
                    # Write to Excel
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    
                    print(f"✅ Converted {csv_file} to sheet: {sheet_name}")
                    
                except Exception as e:
                    print(f"❌ Error converting {csv_file}: {e}")
        
        print(f"🎉 All CSV files converted to: {output_file}")

# Usage
def excel_processing_example():
    """Excel processing example"""
    
    processor = ExcelProcessor()
    
    # Read multiple sheets
    sheets = processor.read_multiple_sheets("data.xlsx")
    
    if sheets:
        # Merge sheets
        merged_data = processor.merge_sheets(sheets, merge_type='concat')
        
        # Create report
        report_data = {
            'Summary': merged_data.describe(),
            'Full_Data': merged_data,
            'Missing_Values': merged_data.isnull().sum().to_frame('Missing_Count')
        }
        
        processor.create_excel_report(report_data, "analysis_report.xlsx")
        
        # Convert CSV files to Excel
        csv_files = ["file1.csv", "file2.csv", "file3.csv"]
        processor.csv_to_excel_converter(csv_files, "combined_data.xlsx")

# excel_processing_example()
```

---

## 🔧 JSON Data Manipulation {#json-manipulation}

### Advanced JSON Processing:
```python
import json
import jsonpath_ng
from collections import defaultdict

class JSONProcessor:
    def __init__(self):
        self.data = None
        self.processed_data = []

    def load_json(self, file_path):
        """JSON file load করা"""

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

            print(f"✅ JSON loaded: {type(self.data)} with {len(self.data) if isinstance(self.data, (list, dict)) else 'N/A'} items")
            return self.data

        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            return None

    def flatten_json(self, data, parent_key='', sep='_'):
        """Nested JSON flatten করা"""

        items = []

        if isinstance(data, dict):
            for k, v in data.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k

                if isinstance(v, dict):
                    items.extend(self.flatten_json(v, new_key, sep=sep).items())
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            items.extend(self.flatten_json(item, f"{new_key}{sep}{i}", sep=sep).items())
                        else:
                            items.append((f"{new_key}{sep}{i}", item))
                else:
                    items.append((new_key, v))

        return dict(items)

    def extract_with_jsonpath(self, data, path_expressions):
        """JSONPath দিয়ে data extract করা"""

        results = {}

        for name, expression in path_expressions.items():
            try:
                jsonpath_expr = jsonpath_ng.parse(expression)
                matches = [match.value for match in jsonpath_expr.find(data)]
                results[name] = matches
                print(f"🎯 {name}: Found {len(matches)} matches")

            except Exception as e:
                print(f"❌ Error with JSONPath {name}: {e}")
                results[name] = []

        return results

    def json_to_dataframe(self, data, normalize_level=0):
        """JSON data কে DataFrame এ convert করা"""

        try:
            if isinstance(data, list):
                # List of objects
                df = pd.json_normalize(data, max_level=normalize_level)
            elif isinstance(data, dict):
                # Single object or nested structure
                df = pd.json_normalize([data], max_level=normalize_level)
            else:
                print("❌ Unsupported JSON structure")
                return None

            print(f"📊 DataFrame created: {df.shape}")
            return df

        except Exception as e:
            print(f"❌ Error converting to DataFrame: {e}")
            return None

    def aggregate_json_data(self, data, group_by_field, aggregation_fields):
        """JSON data aggregate করা"""

        if not isinstance(data, list):
            print("❌ Data must be a list for aggregation")
            return None

        # Group data
        grouped = defaultdict(list)

        for item in data:
            if isinstance(item, dict) and group_by_field in item:
                key = item[group_by_field]
                grouped[key].append(item)

        # Aggregate
        aggregated = {}

        for group_key, group_items in grouped.items():
            group_result = {'group': group_key, 'count': len(group_items)}

            for field, agg_type in aggregation_fields.items():
                values = [item.get(field, 0) for item in group_items if field in item]

                if values:
                    if agg_type == 'sum':
                        group_result[f"{field}_sum"] = sum(values)
                    elif agg_type == 'avg':
                        group_result[f"{field}_avg"] = sum(values) / len(values)
                    elif agg_type == 'max':
                        group_result[f"{field}_max"] = max(values)
                    elif agg_type == 'min':
                        group_result[f"{field}_min"] = min(values)

            aggregated[group_key] = group_result

        print(f"📊 Aggregated into {len(aggregated)} groups")
        return aggregated

    def transform_json_structure(self, data, transformation_rules):
        """JSON structure transform করা"""

        def apply_transformation(item, rules):
            transformed = {}

            for new_field, rule in rules.items():
                if isinstance(rule, str):
                    # Simple field mapping
                    if rule in item:
                        transformed[new_field] = item[rule]

                elif isinstance(rule, dict):
                    if 'source' in rule:
                        source_value = item.get(rule['source'])

                        # Apply transformations
                        if 'type' in rule:
                            if rule['type'] == 'int':
                                try:
                                    transformed[new_field] = int(source_value)
                                except:
                                    transformed[new_field] = 0
                            elif rule['type'] == 'float':
                                try:
                                    transformed[new_field] = float(source_value)
                                except:
                                    transformed[new_field] = 0.0
                            elif rule['type'] == 'str':
                                transformed[new_field] = str(source_value)

                        # Apply default value
                        if 'default' in rule and (source_value is None or source_value == ''):
                            transformed[new_field] = rule['default']

                        # Apply prefix/suffix
                        if 'prefix' in rule:
                            transformed[new_field] = f"{rule['prefix']}{transformed.get(new_field, source_value)}"
                        if 'suffix' in rule:
                            transformed[new_field] = f"{transformed.get(new_field, source_value)}{rule['suffix']}"

            return transformed

        if isinstance(data, list):
            return [apply_transformation(item, transformation_rules) for item in data]
        elif isinstance(data, dict):
            return apply_transformation(data, transformation_rules)
        else:
            return data

    def save_processed_json(self, data, output_file, indent=2):
        """Processed JSON save করা"""

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)

            print(f"💾 Processed JSON saved: {output_file}")
            return True

        except Exception as e:
            print(f"❌ Error saving JSON: {e}")
            return False

# Usage
def json_processing_example():
    """JSON processing example"""

    processor = JSONProcessor()

    # Sample nested JSON data
    sample_data = [
        {
            "id": 1,
            "name": "John Doe",
            "contact": {
                "email": "john@example.com",
                "phone": "123-456-7890"
            },
            "orders": [
                {"product": "Laptop", "price": 1200, "quantity": 1},
                {"product": "Mouse", "price": 25, "quantity": 2}
            ],
            "location": {"city": "New York", "country": "USA"}
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "contact": {
                "email": "jane@example.com",
                "phone": "987-654-3210"
            },
            "orders": [
                {"product": "Keyboard", "price": 75, "quantity": 1}
            ],
            "location": {"city": "Los Angeles", "country": "USA"}
        }
    ]

    # Flatten JSON
    flattened = [processor.flatten_json(item) for item in sample_data]
    print("🔄 Flattened JSON:")
    print(json.dumps(flattened[0], indent=2))

    # Extract with JSONPath
    path_expressions = {
        'all_names': '$.*.name',
        'all_emails': '$.*.contact.email',
        'all_products': '$.*.orders[*].product',
        'all_prices': '$.*.orders[*].price'
    }

    extracted = processor.extract_with_jsonpath(sample_data, path_expressions)
    print(f"🎯 Extracted data: {extracted}")

    # Convert to DataFrame
    df = processor.json_to_dataframe(sample_data)
    if df is not None:
        print("📊 DataFrame columns:", df.columns.tolist())

    # Transform structure
    transformation_rules = {
        'customer_id': 'id',
        'customer_name': 'name',
        'email': {'source': 'contact.email', 'type': 'str'},
        'city': {'source': 'location.city', 'default': 'Unknown'},
        'order_count': {'source': 'orders', 'type': 'int', 'default': 0}
    }

    # Note: This is a simplified example - real transformation would be more complex
    print("🔄 Transformation rules defined")

# json_processing_example()
```

---

## 🗄️ Database Operations {#database-operations}

### SQLite Database Operations:
```python
import sqlite3
import pandas as pd
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="data.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Database এ connect করা"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"✅ Connected to database: {self.db_path}")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False

    def create_table_from_dataframe(self, df, table_name, if_exists='replace'):
        """DataFrame থেকে table তৈরি করা"""

        try:
            df.to_sql(table_name, self.connection, if_exists=if_exists, index=False)
            print(f"📊 Table '{table_name}' created with {len(df)} rows")
            return True
        except Exception as e:
            print(f"❌ Error creating table: {e}")
            return False

    def execute_query(self, query, params=None):
        """SQL query execute করা"""

        try:
            cursor = self.connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]

                # Convert to DataFrame
                df = pd.DataFrame(results, columns=columns)
                print(f"📊 Query returned {len(df)} rows")
                return df
            else:
                self.connection.commit()
                print(f"✅ Query executed successfully")
                return True

        except Exception as e:
            print(f"❌ Query execution failed: {e}")
            return None

    def bulk_insert(self, table_name, data, batch_size=1000):
        """Bulk data insert করা"""

        try:
            cursor = self.connection.cursor()

            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in cursor.fetchall()]

            # Prepare insert statement
            placeholders = ','.join(['?' for _ in columns])
            insert_query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"

            # Insert in batches
            total_inserted = 0

            for i in range(0, len(data), batch_size):
                batch = data[i:i + batch_size]
                cursor.executemany(insert_query, batch)
                total_inserted += len(batch)

                if i % (batch_size * 10) == 0:  # Progress update every 10 batches
                    print(f"📊 Inserted {total_inserted}/{len(data)} rows...")

            self.connection.commit()
            print(f"✅ Bulk insert completed: {total_inserted} rows")
            return True

        except Exception as e:
            print(f"❌ Bulk insert failed: {e}")
            return False

    def create_indexes(self, table_name, index_columns):
        """Table এ index তৈরি করা"""

        for column in index_columns:
            try:
                index_name = f"idx_{table_name}_{column}"
                query = f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column})"

                self.execute_query(query)
                print(f"📈 Index created: {index_name}")

            except Exception as e:
                print(f"❌ Error creating index on {column}: {e}")

    def analyze_table(self, table_name):
        """Table analysis করা"""

        try:
            # Basic stats
            stats_query = f"""
            SELECT
                COUNT(*) as total_rows,
                COUNT(DISTINCT *) as unique_rows
            FROM {table_name}
            """

            stats = self.execute_query(stats_query)

            # Column info
            column_info_query = f"PRAGMA table_info({table_name})"
            column_info = self.execute_query(column_info_query)

            print(f"📊 Table Analysis: {table_name}")
            print(f"  Total rows: {stats.iloc[0]['total_rows']}")
            print(f"  Unique rows: {stats.iloc[0]['unique_rows']}")
            print(f"  Columns: {len(column_info)}")

            return {
                'stats': stats,
                'columns': column_info
            }

        except Exception as e:
            print(f"❌ Table analysis failed: {e}")
            return None

    def export_to_csv(self, table_name, output_file, query=None):
        """Table data CSV এ export করা"""

        try:
            if query:
                df = self.execute_query(query)
            else:
                df = self.execute_query(f"SELECT * FROM {table_name}")

            if df is not None:
                df.to_csv(output_file, index=False)
                print(f"💾 Data exported to: {output_file}")
                return True

            return False

        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False

    def backup_database(self, backup_path):
        """Database backup করা"""

        try:
            backup_conn = sqlite3.connect(backup_path)
            self.connection.backup(backup_conn)
            backup_conn.close()

            print(f"💾 Database backed up to: {backup_path}")
            return True

        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return False

    def close(self):
        """Database connection close করা"""
        if self.connection:
            self.connection.close()
            print("👋 Database connection closed")

# Usage
def database_operations_example():
    """Database operations example"""

    db = DatabaseManager("analysis.db")

    if db.connect():
        # Sample data
        sample_data = pd.DataFrame({
            'id': range(1, 1001),
            'name': [f'User_{i}' for i in range(1, 1001)],
            'age': np.random.randint(18, 80, 1000),
            'salary': np.random.randint(30000, 150000, 1000),
            'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 1000),
            'join_date': pd.date_range('2020-01-01', periods=1000, freq='D')
        })

        # Create table
        db.create_table_from_dataframe(sample_data, 'employees')

        # Create indexes
        db.create_indexes('employees', ['department', 'age'])

        # Analyze table
        analysis = db.analyze_table('employees')

        # Complex query
        query = """
        SELECT
            department,
            COUNT(*) as employee_count,
            AVG(age) as avg_age,
            AVG(salary) as avg_salary,
            MIN(join_date) as earliest_join,
            MAX(join_date) as latest_join
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
        """

        results = db.execute_query(query)
        print("📊 Department Analysis:")
        print(results)

        # Export results
        db.export_to_csv('employees', 'employees_export.csv')

        # Backup database
        db.backup_database('analysis_backup.db')

        db.close()

# database_operations_example()
```

---

## 📈 Data Visualization {#data-visualization}

### Advanced Visualization with Matplotlib & Seaborn:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class DataVisualizer:
    def __init__(self, style='seaborn', figsize=(12, 8)):
        plt.style.use(style)
        self.figsize = figsize
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

        # Set up seaborn
        sns.set_palette("husl")

    def create_dashboard(self, df, output_file="dashboard.html"):
        """Interactive dashboard তৈরি করা"""

        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Distribution', 'Correlation', 'Time Series', 'Category Analysis'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": True}, {"secondary_y": False}]]
        )

        # Numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) > 0:
            # Distribution plot
            fig.add_trace(
                go.Histogram(x=df[numeric_cols[0]], name=numeric_cols[0]),
                row=1, col=1
            )

            # Correlation heatmap (if multiple numeric columns)
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                fig.add_trace(
                    go.Heatmap(
                        z=corr_matrix.values,
                        x=corr_matrix.columns,
                        y=corr_matrix.columns,
                        colorscale='RdBu'
                    ),
                    row=1, col=2
                )

        # Time series (if date column exists)
        date_cols = df.select_dtypes(include=['datetime64']).columns
        if len(date_cols) > 0 and len(numeric_cols) > 0:
            df_sorted = df.sort_values(date_cols[0])
            fig.add_trace(
                go.Scatter(
                    x=df_sorted[date_cols[0]],
                    y=df_sorted[numeric_cols[0]],
                    mode='lines+markers',
                    name='Time Series'
                ),
                row=2, col=1
            )

        # Category analysis
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            value_counts = df[categorical_cols[0]].value_counts().head(10)
            fig.add_trace(
                go.Bar(x=value_counts.index, y=value_counts.values, name='Categories'),
                row=2, col=2
            )

        # Update layout
        fig.update_layout(
            title="Data Analysis Dashboard",
            height=800,
            showlegend=True
        )

        # Save interactive HTML
        fig.write_html(output_file)
        print(f"📊 Interactive dashboard saved: {output_file}")

        return fig

    def advanced_statistical_plots(self, df, target_column=None):
        """Advanced statistical plots"""

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) == 0:
            print("❌ No numeric columns found")
            return

        # Create figure with subplots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Advanced Statistical Analysis', fontsize=16)

        # 1. Distribution with KDE
        sns.histplot(data=df, x=numeric_cols[0], kde=True, ax=axes[0, 0])
        axes[0, 0].set_title(f'Distribution of {numeric_cols[0]}')

        # 2. Box plot
        if len(numeric_cols) > 1:
            sns.boxplot(data=df[numeric_cols[:5]], ax=axes[0, 1])
            axes[0, 1].set_title('Box Plot Comparison')
            axes[0, 1].tick_params(axis='x', rotation=45)

        # 3. Correlation heatmap
        if len(numeric_cols) > 2:
            corr_matrix = df[numeric_cols].corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[0, 2])
            axes[0, 2].set_title('Correlation Matrix')

        # 4. Scatter plot with regression
        if len(numeric_cols) > 1:
            sns.regplot(data=df, x=numeric_cols[0], y=numeric_cols[1], ax=axes[1, 0])
            axes[1, 0].set_title(f'{numeric_cols[0]} vs {numeric_cols[1]}')

        # 5. Violin plot
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0 and len(numeric_cols) > 0:
            # Take first few categories to avoid overcrowding
            top_categories = df[categorical_cols[0]].value_counts().head(5).index
            df_filtered = df[df[categorical_cols[0]].isin(top_categories)]

            sns.violinplot(data=df_filtered, x=categorical_cols[0], y=numeric_cols[0], ax=axes[1, 1])
            axes[1, 1].set_title(f'{numeric_cols[0]} by {categorical_cols[0]}')
            axes[1, 1].tick_params(axis='x', rotation=45)

        # 6. Pair plot (sample)
        if len(numeric_cols) > 2:
            # Use a sample for performance
            sample_df = df[numeric_cols[:4]].sample(min(1000, len(df)))

            # Create pair plot in the last subplot
            axes[1, 2].text(0.5, 0.5, 'See separate pair plot',
                           ha='center', va='center', transform=axes[1, 2].transAxes)
            axes[1, 2].set_title('Pair Plot (separate)')

            # Create separate pair plot
            plt.figure(figsize=(12, 10))
            sns.pairplot(sample_df)
            plt.suptitle('Pair Plot Analysis', y=1.02)
            plt.tight_layout()
            plt.savefig('pair_plot.png', dpi=300, bbox_inches='tight')
            print("📊 Pair plot saved: pair_plot.png")

        plt.tight_layout()
        plt.savefig('statistical_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("📊 Statistical plots saved: statistical_analysis.png")

    def create_animated_plot(self, df, x_col, y_col, time_col, category_col=None):
        """Animated plot তৈরি করা"""

        if time_col not in df.columns:
            print(f"❌ Time column '{time_col}' not found")
            return

        # Create animated scatter plot
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            animation_frame=time_col,
            color=category_col if category_col else None,
            size_max=55,
            title=f'Animated {y_col} vs {x_col} over {time_col}'
        )

        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col,
            height=600
        )

        # Save as HTML
        fig.write_html("animated_plot.html")
        print("🎬 Animated plot saved: animated_plot.html")

        return fig

    def financial_charts(self, df, date_col, price_cols):
        """Financial charts (candlestick, etc.)"""

        if not all(col in df.columns for col in [date_col] + price_cols):
            print("❌ Required columns not found")
            return

        # Sort by date
        df_sorted = df.sort_values(date_col)

        # Create subplots
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=('Price Chart', 'Volume'),
            row_width=[0.7, 0.3]
        )

        # Price line chart
        for col in price_cols:
            fig.add_trace(
                go.Scatter(
                    x=df_sorted[date_col],
                    y=df_sorted[col],
                    mode='lines',
                    name=col
                ),
                row=1, col=1
            )

        # Volume chart (if exists)
        if 'volume' in df.columns:
            fig.add_trace(
                go.Bar(
                    x=df_sorted[date_col],
                    y=df_sorted['volume'],
                    name='Volume',
                    marker_color='rgba(158,202,225,0.8)'
                ),
                row=2, col=1
            )

        fig.update_layout(
            title="Financial Analysis",
            xaxis_title="Date",
            height=800
        )

        fig.write_html("financial_chart.html")
        print("💹 Financial chart saved: financial_chart.html")

        return fig

    def export_all_plots(self, df, output_dir="plots"):
        """সব plots export করা"""

        import os
        os.makedirs(output_dir, exist_ok=True)

        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object']).columns

        plots_created = []

        # 1. Basic histograms
        for col in numeric_cols[:5]:  # First 5 numeric columns
            plt.figure(figsize=self.figsize)
            plt.hist(df[col].dropna(), bins=30, alpha=0.7, color=self.colors[0])
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')

            filename = f"{output_dir}/hist_{col}.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close()
            plots_created.append(filename)

        # 2. Category bar charts
        for col in categorical_cols[:3]:  # First 3 categorical columns
            plt.figure(figsize=self.figsize)
            value_counts = df[col].value_counts().head(10)

            plt.bar(range(len(value_counts)), value_counts.values, color=self.colors[1])
            plt.title(f'Top Categories in {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(range(len(value_counts)), value_counts.index, rotation=45)

            filename = f"{output_dir}/bar_{col}.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close()
            plots_created.append(filename)

        # 3. Correlation matrix
        if len(numeric_cols) > 1:
            plt.figure(figsize=(10, 8))
            corr_matrix = df[numeric_cols].corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            plt.title('Correlation Matrix')

            filename = f"{output_dir}/correlation_matrix.png"
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close()
            plots_created.append(filename)

        print(f"📊 Created {len(plots_created)} plots in {output_dir}/")
        return plots_created

# Usage
def visualization_example():
    """Data visualization example"""

    # Sample data
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=365, freq='D')

    sample_data = pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(1000, 200, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 100,
        'profit': np.random.normal(150, 50, 365),
        'customers': np.random.poisson(50, 365),
        'category': np.random.choice(['A', 'B', 'C', 'D'], 365),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 365),
        'temperature': np.random.normal(20, 10, 365)
    })

    visualizer = DataVisualizer()

    # Create dashboard
    dashboard = visualizer.create_dashboard(sample_data)

    # Advanced statistical plots
    visualizer.advanced_statistical_plots(sample_data)

    # Animated plot
    animated_fig = visualizer.create_animated_plot(
        sample_data,
        'temperature',
        'sales',
        'date',
        'category'
    )

    # Export all plots
    plots = visualizer.export_all_plots(sample_data)

    print(f"🎨 Visualization complete! Created {len(plots)} plots")

# visualization_example()
```

---

## 📊 Statistical Analysis {#statistical-analysis}

### Advanced Statistical Operations:
```python
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

class StatisticalAnalyzer:
    def __init__(self):
        self.results = {}
        self.models = {}

    def descriptive_statistics(self, df):
        """Comprehensive descriptive statistics"""

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) == 0:
            print("❌ No numeric columns found")
            return None

        stats_summary = {}

        for col in numeric_cols:
            data = df[col].dropna()

            stats_summary[col] = {
                'count': len(data),
                'mean': data.mean(),
                'median': data.median(),
                'mode': data.mode().iloc[0] if not data.mode().empty else np.nan,
                'std': data.std(),
                'var': data.var(),
                'min': data.min(),
                'max': data.max(),
                'range': data.max() - data.min(),
                'q1': data.quantile(0.25),
                'q3': data.quantile(0.75),
                'iqr': data.quantile(0.75) - data.quantile(0.25),
                'skewness': stats.skew(data),
                'kurtosis': stats.kurtosis(data),
                'cv': data.std() / data.mean() if data.mean() != 0 else np.nan
            }

        # Convert to DataFrame for better display
        stats_df = pd.DataFrame(stats_summary).T

        print("📊 Descriptive Statistics:")
        print(stats_df.round(4))

        self.results['descriptive_stats'] = stats_df
        return stats_df

    def hypothesis_testing(self, df, col1, col2=None, test_type='ttest'):
        """Hypothesis testing"""

        if col1 not in df.columns:
            print(f"❌ Column '{col1}' not found")
            return None

        data1 = df[col1].dropna()

        if test_type == 'normality':
            # Shapiro-Wilk test for normality
            statistic, p_value = stats.shapiro(data1.sample(min(5000, len(data1))))

            result = {
                'test': 'Shapiro-Wilk Normality Test',
                'statistic': statistic,
                'p_value': p_value,
                'is_normal': p_value > 0.05,
                'interpretation': 'Data is normally distributed' if p_value > 0.05 else 'Data is not normally distributed'
            }

        elif test_type == 'ttest' and col2:
            # Two-sample t-test
            if col2 not in df.columns:
                print(f"❌ Column '{col2}' not found")
                return None

            data2 = df[col2].dropna()
            statistic, p_value = stats.ttest_ind(data1, data2)

            result = {
                'test': 'Two-sample t-test',
                'statistic': statistic,
                'p_value': p_value,
                'significant': p_value < 0.05,
                'interpretation': 'Significant difference' if p_value < 0.05 else 'No significant difference'
            }

        elif test_type == 'one_sample':
            # One-sample t-test against population mean
            pop_mean = data1.mean()  # or specify a different value
            statistic, p_value = stats.ttest_1samp(data1, pop_mean)

            result = {
                'test': 'One-sample t-test',
                'statistic': statistic,
                'p_value': p_value,
                'population_mean': pop_mean,
                'sample_mean': data1.mean()
            }

        print(f"🧪 {result['test']} Results:")
        for key, value in result.items():
            print(f"  {key}: {value}")

        self.results[f'hypothesis_{test_type}'] = result
        return result

    def correlation_analysis(self, df, method='pearson'):
        """Correlation analysis"""

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) < 2:
            print("❌ Need at least 2 numeric columns for correlation")
            return None

        # Calculate correlation matrix
        if method == 'pearson':
            corr_matrix = df[numeric_cols].corr(method='pearson')
        elif method == 'spearman':
            corr_matrix = df[numeric_cols].corr(method='spearman')
        elif method == 'kendall':
            corr_matrix = df[numeric_cols].corr(method='kendall')

        # Find strong correlations
        strong_correlations = []

        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                corr_value = corr_matrix.iloc[i, j]

                if abs(corr_value) > 0.7:  # Strong correlation threshold
                    strong_correlations.append({
                        'variable1': col1,
                        'variable2': col2,
                        'correlation': corr_value,
                        'strength': 'Strong' if abs(corr_value) > 0.8 else 'Moderate'
                    })

        print(f"🔗 {method.title()} Correlation Analysis:")
        print(f"Found {len(strong_correlations)} strong correlations")

        for corr in strong_correlations:
            print(f"  {corr['variable1']} ↔ {corr['variable2']}: {corr['correlation']:.3f} ({corr['strength']})")

        self.results['correlation_analysis'] = {
            'matrix': corr_matrix,
            'strong_correlations': strong_correlations
        }

        return corr_matrix, strong_correlations

    def regression_analysis(self, df, target_col, feature_cols=None):
        """Linear regression analysis"""

        if target_col not in df.columns:
            print(f"❌ Target column '{target_col}' not found")
            return None

        if feature_cols is None:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            feature_cols = [col for col in numeric_cols if col != target_col]

        if len(feature_cols) == 0:
            print("❌ No feature columns available")
            return None

        # Prepare data
        X = df[feature_cols].dropna()
        y = df.loc[X.index, target_col]

        # Fit model
        model = LinearRegression()
        model.fit(X, y)

        # Predictions
        y_pred = model.predict(X)

        # Calculate metrics
        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)

        # Feature importance (coefficients)
        feature_importance = pd.DataFrame({
            'feature': feature_cols,
            'coefficient': model.coef_,
            'abs_coefficient': np.abs(model.coef_)
        }).sort_values('abs_coefficient', ascending=False)

        result = {
            'model': model,
            'r2_score': r2,
            'mse': mse,
            'rmse': rmse,
            'intercept': model.intercept_,
            'feature_importance': feature_importance,
            'n_samples': len(X),
            'n_features': len(feature_cols)
        }

        print(f"📈 Regression Analysis Results:")
        print(f"  R² Score: {r2:.4f}")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  Intercept: {model.intercept_:.4f}")
        print(f"\n🎯 Feature Importance:")
        print(feature_importance.head())

        self.results['regression_analysis'] = result
        self.models['regression'] = model

        return result

    def clustering_analysis(self, df, n_clusters=3, features=None):
        """K-means clustering analysis"""

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if features is None:
            features = numeric_cols.tolist()

        if len(features) < 2:
            print("❌ Need at least 2 features for clustering")
            return None

        # Prepare data
        X = df[features].dropna()

        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Perform clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)

        # Add cluster labels to original data
        df_clustered = X.copy()
        df_clustered['cluster'] = clusters

        # Cluster analysis
        cluster_summary = df_clustered.groupby('cluster')[features].agg(['mean', 'std', 'count'])

        # Calculate silhouette score
        from sklearn.metrics import silhouette_score
        silhouette_avg = silhouette_score(X_scaled, clusters)

        result = {
            'model': kmeans,
            'scaler': scaler,
            'clusters': clusters,
            'cluster_centers': kmeans.cluster_centers_,
            'silhouette_score': silhouette_avg,
            'cluster_summary': cluster_summary,
            'n_clusters': n_clusters,
            'features_used': features
        }

        print(f"🎯 Clustering Analysis Results:")
        print(f"  Number of clusters: {n_clusters}")
        print(f"  Silhouette score: {silhouette_avg:.4f}")
        print(f"  Features used: {features}")
        print(f"\n📊 Cluster Summary:")
        print(cluster_summary)

        self.results['clustering_analysis'] = result
        self.models['clustering'] = kmeans

        return result

    def generate_statistical_report(self, output_file="statistical_report.txt"):
        """Complete statistical report generate করা"""

        with open(output_file, 'w') as f:
            f.write("STATISTICAL ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")

            for analysis_name, result in self.results.items():
                f.write(f"{analysis_name.upper()}\n")
                f.write("-" * 30 + "\n")

                if isinstance(result, dict):
                    for key, value in result.items():
                        if not isinstance(value, (pd.DataFrame, np.ndarray)):
                            f.write(f"{key}: {value}\n")

                f.write("\n")

        print(f"📄 Statistical report saved: {output_file}")

# Usage
def statistical_analysis_example():
    """Statistical analysis example"""

    # Sample data
    np.random.seed(42)
    n_samples = 1000

    sample_data = pd.DataFrame({
        'height': np.random.normal(170, 10, n_samples),
        'weight': np.random.normal(70, 15, n_samples),
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.lognormal(10, 0.5, n_samples),
        'education_years': np.random.randint(8, 20, n_samples),
        'satisfaction': np.random.randint(1, 11, n_samples)
    })

    # Add some correlation
    sample_data['bmi'] = sample_data['weight'] / (sample_data['height']/100)**2
    sample_data['income'] = sample_data['income'] + sample_data['education_years'] * 1000

    analyzer = StatisticalAnalyzer()

    # Descriptive statistics
    desc_stats = analyzer.descriptive_statistics(sample_data)

    # Hypothesis testing
    normality_test = analyzer.hypothesis_testing(sample_data, 'height', test_type='normality')
    ttest_result = analyzer.hypothesis_testing(sample_data, 'height', 'weight', test_type='ttest')

    # Correlation analysis
    corr_matrix, strong_corrs = analyzer.correlation_analysis(sample_data, method='pearson')

    # Regression analysis
    regression_result = analyzer.regression_analysis(
        sample_data,
        target_col='income',
        feature_cols=['education_years', 'age', 'satisfaction']
    )

    # Clustering analysis
    clustering_result = analyzer.clustering_analysis(
        sample_data,
        n_clusters=4,
        features=['height', 'weight', 'age', 'income']
    )

    # Generate report
    analyzer.generate_statistical_report()

    print("📊 Statistical analysis completed!")

# statistical_analysis_example()
```

---

## 🎉 সমাপনী

এই Data Processing ও Analysis গাইডে আপনি পেয়েছেন:

✅ **Data Cleaning:** Comprehensive data preprocessing ও cleaning
✅ **CSV/Excel:** Advanced file processing ও manipulation
✅ **JSON Processing:** Complex JSON data handling ও transformation
✅ **Database Operations:** SQLite database management ও optimization
✅ **Data Visualization:** Interactive charts, dashboards ও statistical plots
✅ **Statistical Analysis:** Hypothesis testing, regression, clustering

### 🚀 Key Features:
- **Automated cleaning** with detailed logging
- **Multi-format support** (CSV, Excel, JSON, Database)
- **Interactive visualizations** with Plotly
- **Statistical testing** with scipy
- **Machine learning** integration
- **Professional reporting** capabilities

### 📈 Next Steps:
1. **Practice** করুন real datasets দিয়ে
2. **Customize** করুন আপনার specific needs অনুযায়ী
3. **Integrate** করুন web scraping data এর সাথে
4. **Scale** করুন big data processing এর জন্য

**Happy Data Analysis! 📊🚀**
```
```
