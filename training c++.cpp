#include<iostream>
using namespace std;
int main ()

double square(double x)
{
    return x*x;
}

void print_square(double x)
{
    cout<<"the square of " << x << " is " << square(x) << "\n";
}

int main()
{
    double x = 0.0;
    cout <<"Type x:"<<;
    cin>>x;
    print_square(x);
}