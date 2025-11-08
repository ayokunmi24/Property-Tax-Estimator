# 🏡 Residential Property Tax Estimator

This Python-based tool helps users estimate residential property taxes based on building size, land dimensions, and exemption status. It calculates square footage, land area in acres, land and building market values, and applies eligible property tax exemptions.

---

# 📌 Features

- ✅ Calculates land square footage and acreage from user input
- ✅ Computes market value of land and building
- ✅ Applies exemption-based tax deductions (Homestead, Over 65, None)
- ✅ Displays a formatted summary report with property tax breakdown
- ✅ Generates a unique confirmation number per estimate

---

# 🛠️ Technologies Used

- Python 3.9
- Standard Libraries: `random` (for confirmation number generation)

---

# 📥 Input Parameters

When run, the program prompts the user for:

- **Property address**
- **Building size** (in square feet)
- **Land effective front and depth** (in feet)
- **Exemption code**:
  - `H` → Homestead
  - `O` → Over 65
  - `N` → None

---

# 📤 Output Example
*******************************************************************************
                    Victorino County Tax Assessor                    
*******************************************************************************

      Welcome to the Residential Property Tax Estimation Tool!       

   Enter Property Address: 1825 Sout 5th Street
   Enter Building Size (sqft): 3300
   Enter Land Effective Front (ft): 135.55
   Enter Land Effective depth (ft): 175.55
   Enter Exemption Code - (H)omestead, (O)ver 65, or (N)one: h

    ----------------------------------------------------------------------     
                     Property Tax Estimate Report                     
    ----------------------------------------------------------------------     

   >>>> Report for Property Located at:  1825 Sout 5th Street

   Building:  3300 sqft

   Land Info
     Front:    135.55  	  Depth: 175.55         
     Sqft:  23,795.80  	  Acres: 0.5463         

   Building Market Value:         429,000.00
   Land Market Value:              54,627.65
   Taxes w/Current Exemptions:      8,221.67 (H - Homestead)
   Taxes w/o Exemptions:            9,672.55
   ----------------------------------------------------------------------
   Confirmation No:  355908

---

# 🧮 How It Works

1. **Land Area Calculation**:
   - Square footage = `front * depth`
   - Acres = `square footage / 43,560`
2. **Market Value**:
   - Building: `avg_home_value * building_size`
   - Land: `market_value_per_acre * acres`
3. **Property Tax**:
   - Base: `(building + land value) * tax rate`
   - With Exemptions:
     - Homestead → 15% reduction
     - Over 65 → 20% reduction

---

# 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ayokunmi24/property-tax-estimator.git
   cd property-tax-estimator
   ```

2. Run the script:
   ```bash
   python property_tax_estimator.py
   ```

---

# 📄 File Structure

```
property-tax-estimator/
├── property_tax_estimator.py
└── README.md
```

---

# 🧑‍💻 Author

Ayokunmi – Product Manager  
[GitHub](https://github.com/ayokunmi24)

---

# 📝 License

This project is licensed under the MIT License.
