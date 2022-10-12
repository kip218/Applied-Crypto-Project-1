#include<iostream>
#include<vector>
#include<string>
#include<unordered_map>
#include<cmath>
using namespace std;

//obtain chopped cipher from the beginning and the end of the ciphertext
//the chopped cipher is guaranteed to be twice longer than the original plaintext
vector<string> chopped_cipher (string ciphertext, int first, int last, int plain_len){
    string chopped_first_ci = "";
    string chopped_last_ci = "";
    for (int i = 0; i < first*2; i++){
        chopped_first_ci += ciphertext[i];
    }
    for (int i = plain_len-1; i  > plain_len - last*2; i--){
        chopped_last_ci += ciphertext;
    }
    vector<string> vec{chopped_first_ci, chopped_last_ci};
    return vec;
}

//obtain potential key by getting the absolute difference between the plainttet and the chopped cipher
//this is obtain through brute force, therefore the potential key will be much longer than the length of plaintext
vector<int> obtainPotentialKey(string first, string first_ci){
    vector<int> p_key;
    for (int i = 0; i < first_ci.length(); i++){
        for (int j = 0; j < first.length(); j++){
            p_key.push_back(abs(first[i] - first_ci[j]));
        }
    }
    return p_key;
}

//calculate the ngram frequency on letter-level for the plaintext
vector<float> ngram(string word){
    unordered_map<string, int> mp;
    string s = "_";
    word = s + word;
    s = word + s;

    for (int i = 0; i < s.length() - 1; i++){
        if (! mp[string() + s[i]+s[i+1]]) mp[string() + s[i] + s[i+1]] = 0;
        else mp[string() + s[i] + s[i+1]]++;
    }
    int i = 0, alphabet[26] = {0}, j;
    while (word[i] != '\0') {
        if (word[i] >= 'a' && word[i] <= 'z') {
            j = word[i] - 'a';
            ++alphabet[j];
        }
        ++i;
    }
    vector<float> ngram_prob;
    float log_prob = 0;
    for (auto x : mp){
        for (auto y : x.first){
            log_prob = log_prob + log(x.second / (word[i] - 'a') );
            ngram_prob.push_back(log_prob);
        }
    }

    return ngram_prob;
}

//purpose is to obtain the key that has the highest likelihood to be the real key
vector<int> eliminateKey (vector<int> key, vector<float> ngram_prob, string first, string first_ci){
    //obtain the key occurrence into a map
    unordered_map<int, int> mp;
    vector<float> key_order;
    for (int i = 0; i < first_ci.length(); i++){
        for (int j = 0; j < key.size(); j++){
            if (first_ci[i] - key[j] == first[i]){
                mp[key[j]]++;
                key_order.push_back(key[j]*1.0);
            } 
        }
    }

    //compare against the density level of key occurrence with the ngram frequency
    //store the occurrence of key is the density > ngram freq
    unordered_map<int, int> ngram_key;
    int k = 0;
    for (int i = 0; i < key_order.size(); i++){
        if (mp[key_order[i]]){
            float percentage = 1 / mp[key_order[i]];
            if (percentage > ngram_prob[k++]) ngram_key[key_order[i]]++;
            if (k == ngram_prob.size()) k = 0;
        }
    }

    //obtain the distinct key from the above map
    //if (the density level of the key that have occurrences > ngram) >= 0.5 then we decide is a valueble key
    vector<int> cleaned_key;
    for (auto x : ngram_key){
        if (x.second / key_order.size() >= 0.5)
            cleaned_key.push_back(x.first);
    }

    return cleaned_key;
    
}

vector<int> ngramApproachKey(std::string ciphertext, string plaintext){
    //obtain the first and last plaintext word
    string first = "";
    string last = "";
    for (int i = 0; i < plaintext.length(); i++){
        if (isalpha(plaintext[i])) first += plaintext[i];
        else break;
    }
    for (int j = plaintext.length() - 1; j > 0; j--){
        if (isalpha(plaintext[j])) last += plaintext[j];
        else break;
    }
    reverse(last.begin(), last.end());

    //obtain the double length chopped cipher
    vector<string> vec{chopped_cipher(ciphertext, first.length(), last.length(), plaintext.length())};

    string first_ci = vec[0];
    string last_ci = vec[1];

    //obtain the potential key with respect to first and last chopped cipher
    vector<int> first_key = obtainPotentialKey(first, first_ci);
    vector<int> last_key = obtainPotentialKey(last, last_ci);

    //obtain ngram with respect with first and last plaintext words
    vector<float> f_ngram {ngram(first)};
    vector<float> l_ngram {ngram(last)};

    //obtain the potential *valuable* key based on the first and last text
    vector<int> potential_key {eliminateKey(first_key, f_ngram, first, first_ci)};
    vector<int> potential_key2 {eliminateKey(last_key, l_ngram, last, last_ci)};

    //sort both vector and we will take the common key from both vector to be our finalized key set
    sort(potential_key.begin(), potential_key.end());
    sort(potential_key2.begin(), potential_key2.end());

    int size = potential_key.size();
    if (potential_key2.size() < size) size = potential_key2.size();

    vector<int> finalized_key;
    for (int i = 0; i < size; i++){
        if (potential_key[i] == potential_key2[i])
            finalized_key.push_back(potential_key[i]);
        else break;
    }

    return finalized_key;
}