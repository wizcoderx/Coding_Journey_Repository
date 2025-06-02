#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

class Student {
    private:
    int age;
    string first_name;
    string last_name;
    int standard;

    public:
    void set_age(int a)
    {
        age = a;
    }

    void set_first_name(const string &fn)
    {
        first_name = fn;
    }
    void set_last_name(const string &fn)
    {
        last_name = fn;
    }
        void set_standard(int st)
    {
        standard = st;
    }
    //getter method

    int get_age() const
    {
        return age;
    }

        string get_first_name() const {
        return first_name;
    }

    string get_last_name() const {
        return last_name;
    }


    int get_standard() const {
        return standard;
    }

        // Method to convert to string
    string to_string() const {
        stringstream ss;
        ss << age << "," << first_name << "," << last_name << "," << standard;
        return ss.str();
    }

};


int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age;
    cin >> first_name;
    cin >> last_name;
    cin >> standard;

    // Create Student object
    Student st;
    st.set_age(age);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    st.set_standard(standard);

    // Output
    cout << st.get_age() << endl;
    cout << st.get_last_name() << ", " << st.get_first_name() << endl;
    cout << st.get_standard() << endl;
    cout << "\n" <<st.to_string();
}
