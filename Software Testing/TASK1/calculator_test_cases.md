# 📌 Calculator Test Cases

## 📋 Introduction
This document contains detailed test cases for a calculator that performs **Addition, Subtraction, Multiplication, and Division** operations.  

Each test case includes:  
- **Test Case ID**  
- **Test Description**  
- **Preconditions**  
- **Test Steps**  
- **Expected Result**  

---

## ✅ **Functional Test Cases (Valid Inputs)**

### **TC-001: Addition of Two Positive Integers**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `5`  
  2. Select `+`  
  3. Enter `10`  
  4. Press `=`  
- **Expected Result:** The output should be `15`  

---

### **TC-002: Addition of a Positive and Negative Integer**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `15`  
  2. Select `+`  
  3. Enter `-5`  
  4. Press `=`  
- **Expected Result:** The output should be `10`  

---

### **TC-003: Subtraction of Two Numbers**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `20`  
  2. Select `-`  
  3. Enter `8`  
  4. Press `=`  
- **Expected Result:** The output should be `12`  

---

### **TC-004: Multiplication of Two Numbers**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `7`  
  2. Select `×`  
  3. Enter `6`  
  4. Press `=`  
- **Expected Result:** The output should be `42`  

---

### **TC-005: Division of Two Numbers**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `18`  
  2. Select `/`  
  3. Enter `3`  
  4. Press `=`  
- **Expected Result:** The output should be `6`  

---

### **TC-006: Decimal Number Calculation**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `2.5`  
  2. Select `×`  
  3. Enter `4.2`  
  4. Press `=`  
- **Expected Result:** The output should be `10.5`  

---

### **TC-007: BODMAS Rule Verification**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `5 + 3 × 2`  
  2. Press `=`  
- **Expected Result:** The output should be `11` (Multiplication first, then addition)  

---

## ❌ **Negative Test Cases (Invalid Inputs)**

### **TC-008: Division by Zero**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `9`  
  2. Select `/`  
  3. Enter `0`  
  4. Press `=`  
- **Expected Result:** The calculator should display an **error message** like `"Cannot divide by zero"`  

---

### **TC-009: Non-Numeric Input Handling**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `"abc"`  
  2. Press `=`  
- **Expected Result:** The calculator should **reject input** and show `"Invalid input"`  

---

### **TC-010: Empty Input Handling**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Press `=` without entering any value  
- **Expected Result:** The calculator should display `"Enter a valid number"`  

---

## 🔄 **Edge Cases**
### **TC-011: Large Number Handling**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `999999999999`  
  2. Select `+`  
  3. Enter `1`  
  4. Press `=`  
- **Expected Result:** Should display correct result or `"Overflow error"` if limit is exceeded  

---

### **TC-012: Negative Result Handling**
- **Preconditions:** Calculator is running  
- **Test Steps:**  
  1. Enter `5`  
  2. Select `-`  
  3. Enter `10`  
  4. Press `=`  
- **Expected Result:** Should return `-5`  

---

## ✅ **Conclusion**
These test cases cover a **wide range of valid, invalid, and edge cases** to ensure the calculator operates correctly and handles all possible scenarios.  
