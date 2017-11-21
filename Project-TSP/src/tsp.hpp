/**************************************************************************
 * 
 * ** Authors: Jon-Eric Cook
 *             Shannon Jeffers
 *             Peter Moldenhauer
 * 
 * ** Date: 12-01-17
 * 
 * ** Description: Project-TSP - This specification file contains the
 *                              declarations of class get_file_contents
 *                              and class output_to_file.
 *
 ***************************************************************************/


#ifndef functions_hpp
#define functions_hpp

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

class get_file_contents {
    friend void get_line(get_file_contents&, string&);
    friend void get_row(get_file_contents&, vector<int>&);
    friend get_file_contents& operator>>(get_file_contents&, int&);

public:
    get_file_contents(const string& file_name);
    bool check_if_at_end();
    ~get_file_contents();
    operator bool();

private:
    ifstream fin;
};

class output_to_file{
    friend output_to_file& operator<<(output_to_file&, int);
    friend output_to_file& operator<<(output_to_file&, const string&);

public:
    output_to_file(const string& file_name);
    ~output_to_file();

private:
    ofstream fout;
};

#endif
