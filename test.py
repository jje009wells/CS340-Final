include "endianess.h"
include <assert.h>


def test_bytes_to_words():
    int res
    uint8_t b2[2] = { 9, 3 }
    uint8_t b9[9] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
    uint64_t w2[2] = { 6, 4 }
    uint64_t w2_0[2]
    uint8_t b17[17]

    res = bytes_to_words(NULL, 10, b2, 2);
    assert(res == ERR_NULL);
    res = bytes_to_words(w2, 10, NULL, 2);
    assert(res == ERR_NULL);
    res = bytes_to_words(w2, 2, b2, 0);
    assert(res == ERR_NOT_ENOUGH_DATA);
    res = bytes_to_words(w2, 0, b2, 2);
    assert(res == ERR_NOT_ENOUGH_DATA);
   
    memset(b17, 0, 17);
    b17[0] = 1;
    res = bytes_to_words(w2, 2, b17, 17);
    assert(res == ERR_MAX_DATA);

    b17[0] = 0;
    res = bytes_to_words(w2, 2, b17, 17);
    assert(res == 0);
    assert(w2[0] == 0 && w2[1] == 0);

    res = bytes_to_words(w2_0, 2, b2, 2);
    assert(w2_0[0] == 0x0903);
    assert(w2_0[1] == 0);
    assert(res == 0);
    
    res = bytes_to_words(w2_0, 2, b9, 9);
    assert(w2_0[0] == 0x0203040506070809);
    assert(w2_0[1] == 0x01);
    assert(res == 0);

void test_words_to_bytes(void)
{
    int res;
    uint8_t b2[2] = { 9, 3 };
    uint8_t b9[9];
    uint64_t w2[2] = { 6, 4 };
    uint8_t b17[17];
    uint64_t w3[3];
    unsigned i;

    memset(b17, 0xFF, 17);

    res = words_to_bytes(NULL, 16, w2, 2);
    assert(res == ERR_NULL);
    res = words_to_bytes(b2, 16, NULL, 2);
    assert(res == ERR_NULL);
    res = words_to_bytes(b2, 2, w2, 0);
    assert(res == ERR_NOT_ENOUGH_DATA);
    res = words_to_bytes(b2, 0, w2, 2);
    assert(res == ERR_NOT_ENOUGH_DATA);
    
    res = words_to_bytes(b9, 8, w2, 2);
    assert(res == ERR_MAX_DATA);
   
    res = words_to_bytes(b9, 9, w2, 2);
    assert(res == 0);
    assert(0 == memcmp(b9, "\x04\x00\x00\x00\x00\x00\x00\x00\x06", 9));
    
    res = words_to_bytes(b9, 9, w2, 1);
    assert(res == 0);
    assert(0 == memcmp(b9, "\x00\x00\x00\x00\x00\x00\x00\x00\x06", 9));

    res = words_to_bytes(b17, 17, w2, 2);
    assert(b17[0] == 0);
    assert(0 == memcmp(b17+1, "\x00\x00\x00\x00\x00\x00\x00\x04", 8));
    assert(0 == memcmp(b17+9, "\x00\x00\x00\x00\x00\x00\x00\x06", 8));
    assert(res == 0);

    memset(b17, 0xFF, sizeof b17);
    memset(w3, 0, sizeof w3);
    res = words_to_bytes(b17, 17, w3, 3);
    assert(res == 0);
    for (i=0; i<sizeof b17; i++) {
        assert(b17[i] == 0);
    }
}

def main():
    test_bytes_to_words()
    test_words_to_bytes()

