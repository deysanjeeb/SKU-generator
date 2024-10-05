# 📦 SKU Generator for Product Variations

Welcome to the **SKU Generator for Product Variations** project! 🎉 This tool helps you generate **child SKUs** for product variations by appending only the unique parts of the product names. It's perfect for managing SKUs for variable products, ensuring each variation gets a unique identifier! 🚀

## 📑 Features
- **Dynamic SKU generation** for product variations
- Only the **unique part of the variation name** is appended to the parent SKU
- Outputs results in a neat CSV format 🧾

## 🛠️ How It Works
1. **Parent Products** have a specific SKU and Name.
2. **Variations** under the parent products have unique attributes in their names.
3. The script extracts the **unique part** of the variation name and appends it to the **Parent SKU**.
4. **No repetitive SKUs!** If no unique part exists, the parent SKU is reused.

## 📋 Prerequisites
- Python 🐍
- `pandas` library 📊

Install `pandas` via pip if you don’t already have it:
```bash
pip install pandas
```
## 📂 Usage Instructions
1. Prepare your CSV:

- The input CSV should have the following columns: Type, SKU, and Name.
- Ensure your products are marked as variable and their respective variations are marked as variation.

2. Run the Script:

- The script reads your CSV file, generates the unique child SKUs, and outputs them to a new CSV file.
Here’s how to run it:

```bash
python main.py
```
3. Output
- The output CSV will have the following columns: Parent SKU, Variation Name, and Generated Child SKU. 


## 🚨 Important Notes
- Make sure your Name column doesn’t contain extraneous characters, as these will be cleaned during SKU generation (spaces and commas are replaced with -, for example).
- The script intelligently removes double dashes (--).



## 🎯 Future Improvements
- Option to handle more complex naming structures.
- Support for additional product types.
Enjoy managing your SKUs with ease! 🎉
