// format_text.cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> get_strings(string text) {
    vector<string> vec_strings;
    string s = "";
    for (int i = 0; i < text.size(); ++i) {
        if (text[i] == ',') {
            while (s.size() > 0 && s.back() == ' ') s.pop_back();
        }
        s += text[i];
        if (text[i] == ',') s += ' ';
    }
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ') continue;
        int j = i;
        string t = "";
        while (j < s.size() && (s[j] != ' ' && s[j] != ',')) {
            t += s[j];
            j++;
        }
        if (j < s.size() && s[j] == ',') {
            t += s[j];
        }
        vec_strings.push_back(t);
        i = j;
    }
    return vec_strings;
}

string format_text(string input_text) {
    vector<string> vec_strings = get_strings(input_text);
    int mx_len = 0;
    for (int i = 0; i < vec_strings.size(); ++i) {
        int len = vec_strings[i].size();
        if (vec_strings[i].back() != ',') mx_len = max(mx_len, 3 * len);
        else mx_len = max(mx_len, 3 * (len - 1));
    }
    int added = -1;
    string result = "";
    for (int i = 0; i < vec_strings.size(); ++i) {
        int len = vec_strings[i].size();
        if (added + len + 1 > mx_len) {
            result += "\n";
            added = -1;
            i--;
            continue;
        }
        if (added != -1) result += " ";
        result += vec_strings[i];
        if (added == -1) added = len;
        else added += len + 1;
    }
    return result;
}

int main() {
    string input_text;
    getline(cin, input_text);
    string result = format_text(input_text);
    cout << result << endl;
    return 0;
}
