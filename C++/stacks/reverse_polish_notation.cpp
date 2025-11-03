#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>
#include <functional>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {

        std::unordered_map<std::string, std::function<int(int, int)>> keymap;
        std::stack<int> thestack;
        int a, b;

        keymap = {
            {"+", [](int a, int b) { return a + b; }},
            {"-", [](int a, int b) { return b - a; }},
            {"/", [](int a, int b) { return b / a; }},
            {"*", [](int a, int b) { return a * b; }}
        };

        int length = tokens.size();
        int output=stoi(tokens[0]);

        for (int i = 0; i < length; i++) {

            if (keymap.find(tokens[i]) == keymap.end()) { // check the existance of the element 
                thestack.push(stoi(tokens[i]));
            }

            else {
                a = thestack.top();
                thestack.pop();
                b = thestack.top();
                thestack.pop();
                output = keymap[tokens[i]](a, b);
                thestack.push(output);
            }
        }

        std::cout << output;

        return output;
    }
};