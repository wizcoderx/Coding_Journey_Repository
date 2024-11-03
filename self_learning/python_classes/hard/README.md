### Based on Previous Medium-Difficulty Questions

1. **Enhance the `Dog` Class with Health and Training Attributes**
   Add attributes `health` (an integer) and `is_trained` (a boolean) to the `Dog` class. Implement a `train` method that improves the dog’s `is_trained` attribute to `True` if the dog’s `health` is above a certain level. Add a `visit_vet` method that adjusts the health level based on random checks and returns the new health level.

2. **Enhance the `Circle` Class with Comparisons and Static Methods**
   Add a `compare` method to the `Circle` class that takes another circle as input and returns which circle is larger in terms of area. Also, implement a static method `circle_from_diameter(diameter)` that takes a diameter as input and returns a `Circle` instance with that diameter.

3. **Create a `BookCollection` Class to Manage Multiple Books**
   Design a `BookCollection` class that can store multiple `Book` instances. Implement methods `add_book`, `remove_book`, and `find_book` to manage the collection. Also, add a method `most_recent` that returns the most recently published book in the collection. Ensure `find_book` can find books by title, author, or genre.

4. **Enhance the `Car` Class with Fuel Logs and Maintenance**
   Add a `fuel_log` attribute to the `Car` class, which stores a list of fuel refills (in gallons) over time. Implement a method `add_fuel(amount)` to add fuel to this log, and a method `average_fuel_usage` that calculates the average fuel used per refill. Add a `service_due` method that returns `True` if the car has traveled more than a certain threshold (e.g., 10,000 miles) since the last service.

5. **Add Subject-Specific Operations to the `Student` Class**
   Update the `Student` class so that each subject in the `grades` dictionary can store multiple grades as a list. Implement a `get_best_subject` method that returns the subject with the highest average grade. Also, add a `print_report_card` method that displays each subject’s average grade in a structured report format.

---

### Project-Like Exercises with Hard Difficulty

6. **Online Shopping Cart System**
   Design a `Cart` class that allows users to add and remove multiple `Product` instances, representing products in an online store. The `Product` class should have attributes `name`, `price`, and `stock`. Implement a `checkout` method in the `Cart` class that calculates the total price and deducts quantities from the `Product` stock. If an item’s stock is insufficient, the checkout should give an error message.

7. **Movie Rental System**
   Create a `Movie` class with attributes `title`, `genre`, `release_year`, and `available_copies`. Implement a `RentalService` class that has a collection of movies and manages movie rentals. Add methods for `rent_movie(title)`, `return_movie(title)`, and `get_available_movies_by_genre(genre)`. Also, add a `recommend_movie` method that suggests a random movie in the same genre as a recently rented one.

8. **Warehouse Management System**
   Define a `Warehouse` class that stores information about multiple `Item` instances, each with attributes `name`, `quantity`, `supplier`, and `last_ordered_date`. Implement methods to `restock_item(name, quantity)` and `generate_report` to list items low on stock. Add a `order_frequency` method that estimates the frequency of restocks needed based on previous orders and last order date.

9. **Social Media Post Scheduler**
   Create a `Post` class with attributes `content`, `post_date`, and `posted` (boolean). Then create a `Scheduler` class that can schedule multiple posts. Implement methods `add_post(post)`, `remove_post(post_id)`, and `publish_posts()` which publishes all scheduled posts for the current date and marks them as posted. Add a `view_scheduled_posts()` method that lists all posts not yet published.

10. **School Management System**
    Create classes `Teacher` and `Classroom`. The `Teacher` class should have attributes `name`, `subject`, and `students` (a list of student names). The `Classroom` class should manage multiple teachers and students across different classes. Implement methods to add/remove teachers, add students to specific teachers, and generate a list of students for each teacher. Add functionality to switch a student’s teacher if needed.