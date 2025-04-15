
# 📊 Livestock Analysis in Kazakhstan

This project presents an exploratory data analysis (EDA) of livestock statistics by region in Kazakhstan, using data from an Excel spreadsheet. The focus is on visualizing and summarizing the number of slaughtered animals by region and by type.

## 📁 Dataset

- **Source**: An Excel file `livestock.xls`
- **Sheet used**: Sheet `"3."`
- **Rows used**: 5th to 24th row (excluding headers and notes)
- **Columns include**:
  - Region (Oblast)
  - Total livestock
  - Specific types: Cattle, Sheep, Goats, Pigs, Horses, Poultry, Camels, Other Animals
![alt text](image-1.png)

## 🔍 What the script does

1. **Data Cleaning**:
   - Skips unnecessary rows(Almaty, Astana, Shymkent) and columns (e.g. "Marals")
   - Replaces missing values represented as `'-'` with `0`
   - Converts numerical values to float
   ![alt text](image-2.png)
2. **Data Summary**:
   - Prints structure of the cleaned data
   - Descriptive statistics and missing value check
   ![alt text](image-4.png)
   ![alt text](image-5.png)
3. **Visualization**:
   - Barplot of **total livestock** slaughtered per **region**
   - Barplot of **total slaughtered animals** by **type of livestock**
![alt text](image-3.png)
## 📈 Example Visualizations

### ✅ Total Livestock by Region
A horizontal bar plot showing which regions have the highest numbers of livestock slaughtered.

### ✅ Livestock Distribution by Type
A bar chart showing the distribution of slaughtered animals by type (e.g., Cattle, Sheep, Poultry, etc.).

## ▶️ How to Run

Make sure you have the required packages:

```bash
pip install pandas matplotlib seaborn openpyxl
```

Then run the notebook or Python script locally:

```python
python livestock_analysis.py  # If saved as a script
```

Or open and run the Jupyter notebook:

```bash
jupyter notebook
```

Place the Excel file in the same directory or update the path in the code.

## 📌 Dependencies

- `pandas`
- `matplotlib`
- `seaborn`
- `openpyxl` (for reading `.xls/.xlsx` files)

## 📂 File Structure

```
📁 assign4/
│
├── livestock.xls               # Source data
├── livestock_analysis.ipynb    # Jupyter notebook with all analysis
├── README.md                   # Project description (this file)
```

## 📬 Contact

Feel free to reach out for questions or collaboration ideas.
