class Solution {
public:
    int getAsciiCode(char ch) {
        return static_cast<int>(ch);
    }

    void process_string(std::string &s) {
        std::string* new_string;
        new_string = new std::string;

        int lofs = s.length();
        int i;

        for (i = 0; i < lofs; i++) {
            if (((getAsciiCode(s[i]) >= 65) && (getAsciiCode(s[i]) <= 90)) ||
                ((getAsciiCode(s[i]) >= 97) && (getAsciiCode(s[i]) <= 122)) || (getAsciiCode(s[i]) >= 48 && getAsciiCode(s[i]) <= 57) ) {
                *new_string += toupper(s[i]);
            }
        }

        s = *new_string;
        delete new_string;
    }

    bool isPalindrome(std::string s) {
        int i;
        bool is_palindrome = true;

        process_string(s);
        int back_tracker = s.length() - 1;

        for (i = 0; i < s.length(); i++) {
            if (s[i] != s[back_tracker]) {
                is_palindrome = false;
                break;
            }
            back_tracker -= 1;
        }

        return is_palindrome;
    }
};


