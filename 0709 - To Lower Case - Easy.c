char* toLowerCase(char* s) {

    for(int i = 0; i<strlen(s); i++){
        if(isalpha(s[i])){
            if(s[i] < 97)
                s[i] += 32;
        }
        
    }
    return s;
}
