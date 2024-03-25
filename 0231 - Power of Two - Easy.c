bool isPowerOfTwo(int n) {
    for(int i = 0; i<32; i++){
        if(n == pow(2, i))
            return true;
    }
    return false;
}
