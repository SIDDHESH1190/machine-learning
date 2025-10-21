import pandas as pd
import numpy as np

class CleanDataset:
    """Class to encapsulate dataset cleaning operations"""
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        """Load dataset from CSV file"""
        try:
            print(f"Loading data from {self.filepath}")
            self.df = pd.read_csv(self.filepath, encoding='utf-8')
            print("Data loaded successfully.")
            return self.df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def analyze_data(self):
        """Perform initial data analysis and report"""
        try:
            if self.df is None:
                raise ValueError("Data not loaded. Call load_data() first.")
            
            print("📊 INITIAL DATA ANALYSIS")
            print("=" * 50)
            print(f"Dataset Shape: {self.df.shape[0]:,} rows × {self.df.shape[1]} columns")

            # Combined missing and infinite values analysis
            missing_values = self.df.isnull().sum()
            numeric_cols = self.df.select_dtypes(include=[np.number])
            infinite_values = np.isinf(numeric_cols).sum()
            
            print("\n🔍 DATA QUALITY ISSUES:")
            quality_issues = pd.DataFrame({
                'Missing': missing_values,
                'Infinite': infinite_values
            }).fillna(0)
            print(quality_issues[~(quality_issues == 0).all(axis=1)])
            return True
        except Exception as e:
            print(f"Error during analysis: {e}")
            return False

    def clean_missing_values(self, df):
        """Clean all missing values with mark-percent consistency"""
        print("\n🧹 CLEANING MISSING VALUES")
        print("=" * 50)
        
        # Basic missing value filling
        cleaning_ops = [
            ('weight_kg', df['weight_kg'].mean(), 'mean'),
            ('improvement', 0, 'zero'),
        ]
        
        for col, fill_value, method in cleaning_ops:
            before = df[col].isnull().sum()
            df[col].fillna(fill_value, inplace=True)
            if before > 0:
                print(f"✅ {col}: Filled {before} values with {method}")
        
        # Handle academic marks and percentage
        print("\n📊 Handling Academic Data:")
            
        # Case 1: Both math_marks and percent are missing
        both_missing = df['math_marks'].isna() & df['percent'].isna()
        if both_missing.any():
            df.loc[both_missing, 'math_marks'] = df['math_marks'].mean()
            df.loc[both_missing, 'percent'] = (
                df.loc[both_missing, 'math_marks'] + 
                df.loc[both_missing, 'science_marks'] + 
                df.loc[both_missing, 'english_marks']
            ) / 3
            print(f"✅ Filled {both_missing.sum()} rows where both math_marks and percent were missing")
        
        # Case 2: percent available, math_marks missing
        percent_available = df['percent'].notna() & df['math_marks'].isna()
        if percent_available.any():
            df.loc[percent_available, 'math_marks'] = np.clip(
                df.loc[percent_available, 'percent'] * 3 - 
                df.loc[percent_available, 'science_marks'] - 
                df.loc[percent_available, 'english_marks'], 0, 100
            )
            print(f"✅ Calculated {percent_available.sum()} math_marks from percent")
        
        # Case 3: math_marks available, percent missing
        math_available = df['math_marks'].notna() & df['percent'].isna()
        if math_available.any():
            df.loc[math_available, 'percent'] = (
                df.loc[math_available, 'math_marks'] + 
                df.loc[math_available, 'science_marks'] + 
                df.loc[math_available, 'english_marks']
            ) / 3
            print(f"✅ Calculated {math_available.sum()} percent from marks")
        
        # Final check for any remaining missing
        math_after = df['math_marks'].isnull().sum()
        percent_after = df['percent'].isnull().sum()
        
        if math_after > 0:
            df['math_marks'].fillna(df['math_marks'].mean(), inplace=True)
            print(f"✅ Filled remaining {math_after} math_marks with mean")
        
        if percent_after > 0:
            df['percent'].fillna(df['percent'].mean(), inplace=True)
            print(f"✅ Filled remaining {percent_after} percent with mean")
        
        return df

    def clean_family_income(self, df):
        """Clean family_income column comprehensively"""
        print("\n💰 CLEANING FAMILY INCOME")
        print("=" * 50)
        
        # Track initial state
        initial_inf = np.isinf(df['family_income']).sum()
        initial_neg = (df['family_income'] < 0).sum()
        
        # Step 1: Handle infinite and negative values
        df['family_income'] = df['family_income'].replace([np.inf, -np.inf], np.nan)
        df.loc[df['family_income'] < 0, 'family_income'] = np.nan
        
        # Step 2: Calculate bounds using IQR
        valid_incomes = df['family_income'].dropna()
        Q1, Q3 = valid_incomes.quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower_bound = max(0, Q1 - 1.5 * IQR)
        upper_bound = Q3 + 1.5 * IQR
        
        print(f"📈 Income Statistics:")
        print(f"   Q1: ₹{Q1:,.2f}, Q3: ₹{Q3:,.2f}, IQR: ₹{IQR:,.2f}")
        print(f"   Bounds: [₹{lower_bound:,.2f}, ₹{upper_bound:,.2f}]")
        
        # Step 3: Cap outliers
        outliers_mask = (df['family_income'] < lower_bound) | (df['family_income'] > upper_bound)
        df.loc[df['family_income'] < lower_bound, 'family_income'] = lower_bound
        df.loc[df['family_income'] > upper_bound, 'family_income'] = upper_bound
        
        # Step 4: Impute missing values
        impute_value = valid_incomes.median()
        df['family_income'] = df['family_income'].fillna(impute_value)
        
        # Report results
        print(f"\n✅ Cleaning Results:")
        print(f"   Handled {initial_inf} infinite values")
        print(f"   Handled {initial_neg} negative values") 
        print(f"   Capped {outliers_mask.sum()} outliers")
        print(f"   Imputed with median: ₹{impute_value:,.2f}")
        print(f"   Final range: ₹{df['family_income'].min():,.2f} to ₹{df['family_income'].max():,.2f}")
        
        return df

    def final_quality_check(self, df):
        """Perform final data quality check"""
        print("\n✅ FINAL DATA QUALITY CHECK")
        print("=" * 50)
        
        remaining_missing = df.isnull().sum().sum()
        remaining_inf = np.isinf(df.select_dtypes(include=[np.number])).sum().sum()
        
        if remaining_missing == 0 and remaining_inf == 0:
            print("🎉 All data quality issues resolved!")
        else:
            print(f"⚠️  Remaining issues - Missing: {remaining_missing}, Infinite: {remaining_inf}")
        
        print(f"Final dataset shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

    def clean_data(self):
        """Main method to clean the dataset"""
        print("\n🧼 STARTING DATA CLEANING PROCESS")
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        try:
            self.df = self.clean_missing_values(self.df)
            self.df = self.clean_family_income(self.df)
            
            duplicates_before = self.df.duplicated().sum()
            self.df.drop_duplicates(inplace=True)
            duplicates_after = self.df.duplicated().sum()
            if duplicates_before > 0:
                print(f"Removed {duplicates_before - duplicates_after} duplicate rows")
            
            self.final_quality_check(self.df)
            return True
        except Exception as e:
            print(f"Error during cleaning: {e}")
            return False

    def save_cleaned_data(self, output_path):
        try:
            print(f"\n💾 SAVING CLEANED DATA to {output_path}")
            if self.df is None:
                raise ValueError("Data not loaded or cleaned. Call load_data() and clean_data() first.")
            self.df.to_csv(output_path, index=False, encoding='utf-8')
            print(f"Cleaned data saved to {output_path}")
            return True
        except Exception as e:
            print(f"Error saving cleaned data: {e}")
            return False
