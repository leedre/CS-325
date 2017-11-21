/**************************************************************************
 * 
 * ** Authors: Jon-Eric Cook
 *             Shannon Jeffers
 *             Peter Moldenhauer
 * 
 * ** Date: 12-01-17
 * 
 * ** Description: Project-TSP - This implementation file defines the
 *                              declarations of class get_file_contents
 *                              and class output_to_file.
 *
 ***************************************************************************/


#include "tsp.hpp"

get_file_contents::get_file_contents(const string& file_name) : fin(file_name) {
    if (fin.fail()){
        cout << "Couldn't open file!\n";
        exit(1);
    }
};

bool get_file_contents::check_if_at_end(){
    return fin.eof();
}

get_file_contents::~get_file_contents(){
    fin.close();
}

void get_line(get_file_contents& file, string& s){
    getline(file.fin, s);
}

void get_row(get_file_contents& file, vector<int>& v){
    string row;
    get_line(file, row);
    istringstream str(row);
    int temp = 0;
    while (str >> temp) {
        v.push_back(temp);
    }
}

get_file_contents& operator>>(get_file_contents& input_file, int& a){
    input_file.fin >> a;
    return input_file;
}

get_file_contents::operator bool(){
    return !fin.fail();
}

output_to_file::output_to_file(const string& file_name) : fout(file_name) { }

output_to_file& operator<<(output_to_file& output_file, int a){
    output_file.fout << a;
    return output_file;
}

output_to_file& operator<<(output_to_file& output_file, const string& s){
    output_file.fout << s;
    return output_file;
}

output_to_file::~output_to_file(){
    fout.close();
}
