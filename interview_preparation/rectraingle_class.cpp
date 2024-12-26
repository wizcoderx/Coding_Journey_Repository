//Create a class Rectangle with member variables for length and width, and a method to calculate the area. Write a main function to demonstrate the class functionality.

#include <iostream>
using namespace std;

class Rectangle {
    public:
        int length;
        int width;
        int area() {
            return length * width;
        }
};

int main() {
    Rectangle r;
    r.length = 10;
    r.width = 5;
    cout << "Area of the rectangle is " << r.area();
}