// stupid.cpp
// stupid, too!

#include "../cpp/easylab.h"

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;


int main(int argc, char** argv)
{



    if (argc < 4) {
        cout << "wrong arguments!\n";
        exit(1);
    }

    //Easylab e("stupid");
    Easylab* e = new Easylab("stupidcpp");
    e->start();

    int var1 = atoi(argv[1]);
    int var2 = atoi(argv[2]);
    int var3 = atoi(argv[3]);

    int j;
    for (int i=0; i<var1; i++) {
        j--;
    }
    for (int i=0; i<var2; i++) {
        j--;
    }
    for (int i=0; i<var3; i++) {
        j++;
    }

    // end timer and show time
    e->end();
    cout << e->timeStr() << endl;

    // log
    float time = e->getElapsedTime();
    e->log("var1=%d, var2=%d, var3=%d, time=%f", var1, var2, var3, time);
}
