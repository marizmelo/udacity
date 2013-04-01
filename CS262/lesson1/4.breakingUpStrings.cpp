#include <iostream>
#include <string>
using namespace std;

int rsplit(string str, int pos=0){
    size_t found;
    found=str.find(" ", pos);
    int cache = int(found);
    if( pos < str.length() && cache >=0 ){
        cout << cache << endl;
        pos = cache + 1;
        rsplit(str, pos);
    }//if
}//RSPLIT()

int main(){
    rsplit("jose mariz melo formiga viana");
}//MAIN()