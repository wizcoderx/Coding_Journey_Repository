### Based on Previous Questions

1. **Extend the `Dog` Class with Additional Methods and Attributes**
   Add a `breed` attribute to the `Dog` class. Implement a method called `play` that takes an activity (e.g., "fetch") as a parameter and returns a string like "{name} is playing {activity}!". Add a method `age_in_dog_years` that calculates and returns the dog’s age in "dog years" (using a multiplier of 7).

2. **Modify the `Circle` Class with Perimeter Calculation**
   Add a method to the `Circle` class called `perimeter` that calculates and returns the perimeter of the circle using the formula: \( \text{perimeter} = 2 \times \pi \times \text{radius} \). Also, add a method `diameter` that returns the diameter of the circle.

3. **Enhance the `Book` Class with Additional Functionalities**
   Add a `genre` attribute to the `Book` class. Implement a method called `is_classic` that returns `True` if the book was published before 1980 and `False` otherwise. Add another method `compare` that takes another book as a parameter and returns the title of the book published earlier.

4. **Extend the `Car` Class with a Method for Fuel Efficiency**
   In the `Car` class, add attributes for `mileage` and `fuel_capacity`. Implement a method `range` that calculates and returns the maximum distance the car can travel on a full tank. Also, add a method `is_fuel_efficient` that returns `True` if the car has a mileage greater than 20 mpg, `False` otherwise.

5. **Modify the `Student` Class to Track Multiple Subjects**
   Update the `Student` class to have a dictionary attribute `grades`, where keys are subject names and values are grades. Add methods `add_grade(subject, grade)` to add a grade and `average_grade` to calculate the average grade across subjects. Add a class method `change_school_name` to modify the class variable `school_name`.

---

### Small Project-Like Medium-Difficulty Exercises

6. **Inventory System for a Store**
   Create a class called `Product` with attributes `name`, `price`, and `quantity_in_stock`. Implement methods to add and remove stock. Then create a class `Inventory` that can store multiple products. Implement methods to add a product, remove a product, and get the total value of all products in the inventory.

7. **Bank Account System**
   Create a class `BankAccount` with attributes `account_number` and `balance`. Add methods `deposit(amount)` and `withdraw(amount)`. Create another class `Customer` that has an attribute `accounts`, a list to store multiple `BankAccount` instances. Add methods to allow a customer to open a new account, close an account, and check the balance of all accounts.

8. **Library Management System**
   Create a class `Library` with an attribute `catalog` that holds a dictionary of book titles and the number of available copies for each. Implement methods to `add_book(title, copies)`, `borrow_book(title)`, and `return_book(title)`. Track borrowed books and display which titles are unavailable.

9. **Employee and Department Management System**
   Define a class `Employee` with attributes `name`, `position`, and `salary`. Create a `Department` class that stores multiple employees and has methods to add an employee, remove an employee, calculate the average salary in the department, and list all employees.

10. **Task Manager**
    Create a class `Task` with attributes `title`, `description`, and `completed` (a boolean). Implement methods to mark a task as completed and change the description. Then, create a class `TaskManager` that can hold multiple tasks. Add methods to add a task, remove a task, list all tasks, and show all completed tasks.