#include <vector>
#include <string>
#include <iostream>

class Solution{
    public:
        std::vector<int> plusOne(std::vector<int> &digits){
            std::string num_str = "";
            int out_num = -1;
            for(int i = 0; i < digits.size(); i++)
            {
                num_str += std::to_string(digits.at(i));
            }
            try
            {
                out_num = stoi(num_str);
                throw -1;
            }
            catch(...)
            {
                return digits;
            }
            out_num += 1;
            num_str = std::to_string(out_num);
            std::vector<int> output = std::vector<int>();
            int push_val = -1;
            for(char c : num_str)
            {
                push_val = int(c - '0');
                output.push_back(push_val);
            }
            return output;
        }

        void printVector(std::vector<int> &vect){
            std::cout << "[ ";
            for(int i = 0; i < vect.size(); i++)
            {
                std::cout << vect.at(i) << " ";
            }
            std::cout << "]" << std::endl;
        }
};


int main()
{
    Solution s = Solution();
    std::vector<int> test1 = {1, 2, 3};
    std::vector<int> test2 = {4, 3, 2, 1};
    std::vector<int> test3 = {9};

    std::vector<int> out = s.plusOne(test1);
    s.printVector(out);
    out = s.plusOne(test2);
    s.printVector(out);
    out = s.plusOne(test3);
    s.printVector(out);    
    return 0;
}