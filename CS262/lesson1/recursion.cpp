#include <iostream> //input/output library in c++
using namespace std;    //name space for standard library

int recursion(int times){
    if (times < 3){
        cout << times << endl; //end with break line
        times++;
        recursion(times);
    }
}//FUNCTION: RECURSION

int main(){
    recursion(0);
}//MAIN PROGRAM