/**************************************************************************
 * 
 * ** Authors: Jon-Eric Cook
 *             Shannon Jeffers
 *             Peter Moldenhauer
 * 
 * ** Date: 12-01-17
 * 
 * ** Description: Project-TSP - This specification file contains the
 *								 declarations of a class named Item.
 *
 ***************************************************************************/


#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <math.h>
#include "tsp.hpp"

using namespace std;

int calculate_distance(vector<int> cities, int city1, int city2){
    double distance = sqrt( pow(cities[city2*3 + 1] - cities[city1*3 + 1], 2) +
                            pow(cities[city2*3 + 2] - cities[city1*3 + 2], 2) );
    int rounded_distance = round(distance);
    return rounded_distance;
}

bool vector_contains(vector<int>& vec, int search){
    for (auto& x : vec){
        if (search == x)
            return true;
    }
    return false;
}

int main(int argc, char* argv[]) {
    vector<int> cities;
    vector<int> distances;
    vector<int> visited;
    int distance;

    clock_t clock_start = clock();

    if (argc != 2){
        cout << "Invalid number of arguments.\n";
        exit(1);
    }

    string file = argv[1];
    get_file_contents fin(file);

    while (true){
        get_row(fin, cities);
    
        if (fin.check_if_at_end())
            break;
    }

    int num_cities = cities.size() / 3;

    for (int i = 0; i < num_cities; i++){
        for (int j = 0; j < num_cities; j++){
            distance = calculate_distance(cities, i, j);
            distances.push_back(distance);
        }
    }

    int start = 11;
    visited.push_back(start);
    int min;
    int index;
    int dist_traveled = 0;

    while (visited.size() < num_cities){
        min = 999999;
        index = 123456;
        for (int i = 0; i < num_cities; i++){
            if (distances[start*num_cities + i] < min &&
                !vector_contains(visited, i) ){
                min = distances[start*num_cities + i];
                index = i;
            }
        }
        dist_traveled += min;
        visited.push_back(index);
        start = index;
    }

    dist_traveled += distances[visited[visited.size()-1] * num_cities + visited[0]];
    clock_t clock_end = clock();
    string file_tour = file + ".tour";
    output_to_file fout(file_tour);
    fout << dist_traveled << "\n";

    for (auto& x : visited)
        fout << x << "\n";

    double duration = ( clock_end - clock_start ) / (double) CLOCKS_PER_SEC;
    cout << file << "  ->  " << duration << " sec\n";
    
    return 0;
}