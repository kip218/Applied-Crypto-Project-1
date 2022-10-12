#include<iostream>
#include<string>
#include<vector>
#define L 600

int keyGenAlgo(std::vector<int> key){
    int size = key.size();
    int idx = rand() % size;
    std::cout << "\t key: " << key[idx] << std::endl;
    return key[idx];
}

std::string cipherAlgo(std::vector<int> key, std::string message){
    int mtxt_ptr = 0;
    int rand_counter = 0;
    float rand_prob = 0.01;
    int round = 0;
    std::string ciphertxt = "";
    srand(time(NULL));

    std::string keyspace[27] = {" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}; 

    while (mtxt_ptr < message.size()){
        if (isalpha(message[mtxt_ptr])){
            float coin_val = ((double) rand() / (RAND_MAX)); //real number between 0 and 1, inclusively
            std::cout << round++ << ". coin_val: " << coin_val << std::endl;
            if ((rand_prob < coin_val) && (coin_val <= 1)){
                int j = keyGenAlgo(key);
                if (message[mtxt_ptr] + j <= 122){
                    std::cout << "\t letter: " << message[mtxt_ptr] << std::endl;
                    std::cout << "\t ci: " << static_cast<char>(message[mtxt_ptr] + j) << std::endl;
                    ciphertxt += (message[mtxt_ptr++] + j);
                }
                else {
                    std::cout << "\t letter: " << message[mtxt_ptr] << std::endl;
                    if (message[mtxt_ptr] + j == 123) {ciphertxt += " "; mtxt_ptr++; std::cout << "\t ci:<space>" << std::endl;}
                    else {
                    std::cout << "\t ci: " << static_cast<char>(message[mtxt_ptr] + j - 122 + 97) << std::endl;
                    ciphertxt += message[mtxt_ptr++] + j - 122 + 97 - 1;}
                }
            }
            else if ((coin_val >= 0) && (coin_val <= rand_prob)){
                char c = 'a' + rand()%26;
                ciphertxt += c;
                rand_counter++;
                std::cout << "    rand occur by 1" << std::endl;
            }
        }
        else {
            int j = keyGenAlgo(key);
            ciphertxt += keyspace[j];
            mtxt_ptr++;
        }
    }
    std::cout << "\t rand_counter: " << rand_counter << std::endl;
    std::cout << "plaintext  ::::: " << message << ", (" << message.length() << ")" << std::endl;
    std::cout << "ciphertext ::::: " << ciphertxt << ", (" << ciphertxt.length() << ")" << std::endl;
    std::cout << "----------------------------------" << std::endl;
    return ciphertxt;
}

int main() {
    //vector<int> key{1, 5, 9, 12};
    std::string msg = "autarchy muggiest capabilities snowier collect undivided superpower aspca tektites neuritis turtledoves miriest nonsectarian featherbrained confiscators glimpse domesticator dater houston bassoon antipathy lowdown hallucinative noses drowse wordlessly remembering lessening escargot intersects horace unroofs smokable wirepuller exteriorized auctioned cavils uprose sobbing preannouncements pests noodled minter symbiot rocketlike oops unalike readableness vivo affirmativeness plumier spaciously miseducating recessionals herbaceous recipient evanesce tightrope rester deleteriousness undiscriminati";
    std::string ciphertext = cipherAlgo(std::vector<int> {1, 5, 9, 12}, msg);
    return 0;
}


/*Pseudocode:
Let key be a list of whole numbers with a range {0, 26}
Let plaintext be a string of plaintext with a text space in {<space>, 'a', 'b', .., 'z'}
Let ciphertext be an empty string 
Encrypttion (key, plaintext, preset_prob){
    Let p_ptr be the index pointer of plaintext string 
    Let rand_count = 0
    while (p_pter < length of plaintext){
        Let coin_val be the randomly generated value use for every char encryption
        if ((preset_prob < coin_val) && (coin_val <= 1)){
            randomly choose a number from key and shift accordingly
            append the cipher char into ciphertext
            p_ptr increment by 1
        }
        else if ((coin_val >= 0) && (coin_val <= rand_prob)) {
            randomly select a char from text space
            append on the char into ciphertext
            rand_count increment by 1
        }
    }
    return ciphertext
}*/