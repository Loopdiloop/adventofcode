#include <iostream>
#include <fstream>

#include <map>
#include <string>

using namespace std;

//Declaration of functions
int do_calculation(int a, int b);

int main()
{   
    /* Part 1 of Advent of code 2022, day 02. */
    std::cout << "The secret rock-paper-scissors tactics \n";

    string line; 
    string opponent;
    string mymove; 

    int points = 0;

    // 3x3 matrix of  winning conditions of rock, paper, scissors
    int point_matrix[3][3] = {{3,6,0}, 
                              {0,3,6}, 
                              {6,0,3}};

    map<string,int> move_index = {{"A", 0}, {"X", 0}, 
                             {"B", 1}, {"Y", 1}, 
                             {"C", 2}, {"Z", 2}};

    // Reading file
    ifstream inputfile ("strategy.txt");
    
    if (inputfile.is_open()){
        while ( getline (inputfile, line)){
            opponent = line[0]; 
            mymove = line[2];

            points += move_index[mymove] + 1;
            points += point_matrix[move_index[opponent]][move_index[mymove]];
        }
        inputfile.close();
    }
    else cout << "Couldn't read file. Help \n";

    cout << "Points from strategy, star 1: " << points << "\n";

    return 0;
}
