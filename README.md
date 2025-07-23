

# 🔢 Luhn's Algorithm Validator

Luhn's Algorithm (also known as the Mod 10 Algorithm) is a simple checksum formula used to validate identification numbers such as **credit card numbers**, **IMEIs**, and **government-issued IDs**.

This project provides a basic implementation of Luhn’s algorithm to check whether a given number is valid.

---

## 📚 How Luhn’s Algorithm Works

1. Starting from the **rightmost digit** (the check digit), move left.
2. **Double every second digit**. If the result is greater than 9, subtract 9 from it.
3. **Add** all the digits together.
4. If the total modulo 10 is equal to 0, the number is **valid**.

---

## 🚀 Example

For input: `4539 1488 0343 6467`

1. Strip spaces: `4539148803436467`
2. Starting from the right, double every second digit and adjust:
   - Adjusted digits: `[8, 5, 6, 9, 2, 8, 8, 7, 0, 3, 4, 6, 3, 4, 6, 7]`
3. Sum: `8 + 5 + 6 + 9 + 2 + 8 + 8 + 7 + 0 + 3 + 4 + 6 + 3 + 4 + 6 + 7 = 90`
4. `90 % 10 = 0` → ✅ Valid

---
# Usage

number = "4539148803436467" //Your card number
output: VALID or INVALID 

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Contributions Welcome!

Feel free to fork the project, improve the code, and submit a pull request. Suggestions, bug reports, and feedback are highly appreciated!

---
