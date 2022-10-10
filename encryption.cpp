#include<iostream>
#include<string>
#include<vector>
using namespace std;
#define L 600

int keyGenAlgo(vector<int> key){
    int size = key.size();
    int idx = rand() % size;
    cout << "\t key: " << key[idx] << endl;
    return key[idx];
}

string cipherAlgo(vector<int> key, string message){
    int mtxt_ptr = 0;
    int rand_counter = 0;
    float rand_prob = 0.1;
    int round = 0;
    string ciphertxt = "";
    srand(time(NULL));

    while (mtxt_ptr < message.size()){
        if (isalpha(message[mtxt_ptr])){
            float coin_val = ((double) rand() / (RAND_MAX)); //real number between 0 and 1, inclusively
            cout << round++ << ". coin_val: " << coin_val << endl;
            if ((rand_prob < coin_val) && (coin_val <= 1)){
                int j = keyGenAlgo(key);
                if (message[mtxt_ptr] + j <= 122){
                    cout << "\t letter: " << message[mtxt_ptr] << endl;
                    cout << "\t ci: " << static_cast<char>(message[mtxt_ptr] + j) << endl;
                    ciphertxt += (message[mtxt_ptr++] + j);
                }
                else {
                    cout << "\t letter: " << message[mtxt_ptr] << endl;
                    cout << "\t ci: " << static_cast<char>(message[mtxt_ptr] + j - 122 + 97 - 1) << endl;
                    ciphertxt += message[mtxt_ptr++] + j - 122 + 97 - 1;
                }
            }
            if ((coin_val >= 0) && (coin_val <= rand_prob)){
                char c = 'a' + rand()%26;
                ciphertxt += c;
                rand_counter++;
                cout << "    rand occur by 1" << endl;
            }
        }
        else {
            ciphertxt += " ";
            mtxt_ptr++;
        }
    }
    cout << "\t rand_counter: " << rand_counter << endl;
    cout << "plaintext  ::::: " << message << ", (" << message.length() << ")" << endl;
    cout << "ciphertext ::::: " << ciphertxt << ", (" << ciphertxt.length() << ")" << endl;
    cout << "----------------------------------" << endl;
    return ciphertxt;
}

int main() {
    vector<int> key{1, 5, 9, 12};
    string msg = "autarchy";
    string ciphertext = cipherAlgo(vector<int> {1, 5, 9, 12}, msg);
    return 0;
}