#include "../endianess.h"
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>


void fuzz_test_bytes_to_words(uint8_t in_arr[9])
{
    int res;
    uint64_t w2[2] = { 6, 4 }; //default values for ease of testing
    uint64_t w2_0[2];
    uint8_t orig[9];

    for(int i = 0; i <= sizeof(in_arr); i++)
    {
        //printf("in_arr i is: %hhx\n", in_arr[i]);
        orig[i] = in_arr[i];
    }

    FILE* fp = fopen("output.txt", "a");
    if (fp == NULL) {
        printf("no such file.\n");
        return; //exit
    }
    fprintf(fp, "On input: ");
    for(int i = 0; i < sizeof(orig); i++)
    {
        fprintf(fp, "0x%02hhx, ", orig[i]);
    }

    fprintf(fp, " -- ");

    
    // Test some of the basic error cases
    // If certain lines are broken in endianness.h, for example, one of the if statements
    // around endianness.h line 200, then the asserts fail, and the specific issue is
    // printed to output.txt along with exact input
    res = bytes_to_words(NULL, 10, in_arr, 2);
    if(res != ERR_NULL)
    {
        fprintf(fp, "Null error not behaving as expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == ERR_NULL);
    res = bytes_to_words(w2, 10, NULL, 2);
    if(res != ERR_NULL)
    {
        fprintf(fp, "Null error not behaving as expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == ERR_NULL);
    res = bytes_to_words(w2, 2, in_arr, 0);
    if(res != ERR_NOT_ENOUGH_DATA)
    {
        fprintf(fp, "Not enough data error not behaving as expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == ERR_NOT_ENOUGH_DATA);
    res = bytes_to_words(w2, 0, in_arr, 2);
    if(res != ERR_NOT_ENOUGH_DATA)
    {
        fprintf(fp, "Not enough data error not behaving as expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == ERR_NOT_ENOUGH_DATA);

    res = bytes_to_words(w2, 1, in_arr, 9);
    if(res != ERR_MAX_DATA)
    {
        fprintf(fp, "Max data error not behaving as expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == ERR_MAX_DATA);

    //general test that 0 returns when bad input not intentionally put in
    res = bytes_to_words(w2_0, 2, in_arr, 9);
    if(res != 0)
    {
        fprintf(fp, "Failed to return 0 when 0 expected\n");
        fclose(fp); //close the file when finished
    }
    assert(res == 0);


    printf("No asserts failed here\n"); //for ease of testing
    fprintf(fp, "No unexpected behavior found."); //all 

    fprintf(fp, "\n");
    fclose(fp); //close the file when finished
}




int main(int argc, char* argv[])
{
    // check command line args
    // printf("argc: %d \n", argc);
    // printf("argv size: %d \n", sizeof(argv));

    // for(int i = 0; i < sizeof(argv); i++)
    // {
    //     printf("ARg %d is %s",i,argv[i]);
    //     printf("\n");
    // }

    uint8_t test[9];
    
    int n1,n2,n3,n4,n5,n6,n7,n8,n9;
    //printf("%d",sscanf( argv[1], "[%d, %d, %d, %d, %d, %d, %d, %d, %d]", &n1,&n2,&n3,&n4,&n5,&n6,&n7,&n8,&n9));
    sscanf( argv[1], "[%d, %d, %d, %d, %d, %d, %d, %d, %d]", &n1,&n2,&n3,&n4,&n5,&n6,&n7,&n8,&n9);

    // input array to test function
    uint8_t test_arr[9] = {n1,n2,n3,n4,n5,n6,n7,n8,n9};

    // Check the input array
    // for(int i = 0; i < sizeof(test_arr); i++)
    // {
    //     printf("Test i is: %hhx\n", test_arr[i]);
    // }
    
    fuzz_test_bytes_to_words(test_arr);

    return 0;
}
