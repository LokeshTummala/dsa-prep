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

## 🔗 Practice Problems (LeetCode)

---

### 🟢 Easy Level

1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
3. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
4. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
5. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
6. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
7. [Plus One](https://leetcode.com/problems/plus-one/)
8. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
9. [Missing Number](https://leetcode.com/problems/missing-number/)
10. [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

---

### 🟡 Medium Level

1. [3Sum](https://leetcode.com/problems/3sum/)
2. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
3. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
4. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
5. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
6. [Sort Colors](https://leetcode.com/problems/sort-colors/)
7. [Rotate Array](https://leetcode.com/problems/rotate-array/)
8. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
9. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
10. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

---

### 🔴 Hard Level

1. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
2. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
3. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
4. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
5. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)


---

## 🧠 Pattern → Problem Mapping

| Pattern | Problems |
|--------|--------|
| Hashing | Two Sum, Contains Duplicate |
| Prefix Sum | Subarray Sum Equals K |
| Kadane’s | Maximum Subarray |
| Two Pointers | 3Sum, Container With Most Water |
| Sliding Window | Sliding Window Maximum |
