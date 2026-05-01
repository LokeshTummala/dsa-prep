# 📚 Arrays – Complete Guide

---

## 🧠 What is an Array?

An **array** is a linear data structure that stores elements of the same type in **contiguous memory locations**.

* Elements are accessed using an **index**
* Indexing typically starts from **0**
* Supports **constant time access (O(1))**

👉 Example:

```id="eg1"
arr = [10, 20, 30, 40]
```

---

## ⚡ Key Characteristics

* Fixed or dynamic size (depending on language)
* Indexed access
* Efficient traversal
* Cache-friendly (due to contiguous memory)

---

## ⏱ Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Access    | O(1)       |
| Search    | O(n)       |
| Insertion | O(n)       |
| Deletion  | O(n)       |

---

## 🔥 Types of Arrays

### 1. Static Array

* Fixed size
* Example: C, Java arrays

### 2. Dynamic Array

* Resizable
* Example: Python list, Java ArrayList

---

## 🧩 Common Operations

* Traversal
* Insertion
* Deletion
* Searching
* Sorting

---

## 🚀 Important Patterns in Arrays

---

### 🔹 1. Prefix Sum

Used for:

* Subarray sum problems
* Range queries

👉 Idea:
Store cumulative sum to avoid recomputation

---

### 🔹 2. Kadane’s Algorithm

Used for:

* Maximum subarray problems

👉 Key Insight:
Track current sum and reset when it becomes negative

---

### 🔹 3. Two Pointers

Used for:

* Pair problems (2Sum, 3Sum)
* Sorted arrays

👉 Idea:
Use left & right pointers to reduce complexity

---

### 🔹 4. Sliding Window

Used for:

* Subarray/substring problems

👉 Idea:
Expand → Shrink window to maintain condition

---

### 🔹 5. Hashing

Used for:

* Frequency counting
* Duplicate detection

👉 Data Structure:

* HashMap / Set

---

## ❗ Common Interview Problems

* Two Sum
* Maximum Subarray
* Subarray Sum Equals K
* 3Sum / 4Sum
* Container With Most Water
* Longest Consecutive Sequence
* Trapping Rain Water

---

## ⚠️ Common Mistakes

* Ignoring edge cases (empty array, single element)
* Not optimizing from O(n²) → O(n)
* Incorrect index handling
* Forgetting integer overflow cases

---

## 🧠 When to Use Arrays?

Use arrays when:

* Data needs **fast access**
* You need to iterate sequentially
* Memory locality matters

---

## 📌 Key Takeaways

* Arrays are the **foundation of DSA**
* Most advanced problems reduce to array patterns
* Mastering patterns = solving 50% of coding interviews

---

## 🚀 Final Thought

> “If you can recognize patterns in arrays, you can solve most problems efficiently.”

---
## Links to the problems: 
   ## Easy: 
      1. [Two Sum](# https://leetcode.com/problems/two-sum/description/)
      2. 
