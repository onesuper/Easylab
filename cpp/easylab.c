// Easylab.cpp

#include <iostream>
#include <string.h>
#include <stdarg.h>
#include <stdio.h>
#include <sys/time.h>

using namespace std;


class Easylab {
 private:
    string name;
    struct timeval start_time;
    struct timeval end_time;
    float elapsed_time;
    string timestring;
    string time_meassure;

 public:
    Easylab(const char*);
    int log(const char*, ...);
    int start(void);
    int end(void);
    float getElapsedTime(void);
    string timeStr(void);
};


Easylab::Easylab(const char* str) {
    name = str;
    time_meassure = "ms";
}


int Easylab::log(const char* format, ...) {
    cerr << name << endl;
    va_list arglist;
    va_start(arglist, format);
    vfprintf(stderr, format, arglist);
    return 0;
}

int Easylab::start(void) {
    gettimeofday(&start_time, 0);
    return 0;
}


int Easylab::end(void) {
    gettimeofday(&end_time, 0);
    elapsed_time = 1000000 * (end_time.tv_sec - start_time.tv_sec)
        + end_time.tv_usec - start_time.tv_usec;
    elapsed_time /= 1000000;
    char* buf = new char[30];
    sprintf(buf, "%3f", elapsed_time);
    timestring = buf;
    return 0;
}

float Easylab::getElapsedTime(void) {
    return elapsed_time;
}

string Easylab::timeStr(void) {
    return  timestring + time_meassure;
}
