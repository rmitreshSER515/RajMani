#include<iostream>
using namespace std;
void merge(int *arr, int start, int end){
    int mid = start + (end-start)/2;
    int len1 = mid - start + 1;
    int len2 = end - mid;
    int *first = new int[len1];
    int *second = new int[len2];

    int mainArrayIndex = start;
    //copy first array
    for(int i=0; i<len1; i++){
        first[i] = arr[mainArrayIndex++];
    }
    //copy second array
    for(int j = 0; j<len2; j++){
        second[j] = arr[mainArrayIndex++];
    }
    //merge two sorted arrays
    int index1 = 0;
    int index2 = 0;
    mainArrayIndex = start;
    while(index1 < len1 && index2 < len2){
        if(first[index1] < second[index2]){
            arr[mainArrayIndex++] = first[index1++];
        } else {
            arr[mainArrayIndex++] = second[index2++];
        }
    }
    while(index1 < len1){
        arr[mainArrayIndex++] = first[index1++];
    }
    while(index2 < len2){
        arr[mainArrayIndex++] = second[index2++];
    }
}
void mergeSort(int *arr, int start, int end){
    if (start >= end){
        return;
    }
    int mid = start + (end-start)/2;
    mergeSort(arr, start, mid);
    mergeSort(arr, mid+1, end);
    merge(arr, start, end);

}
int main(){
    int arr[] = {38,27,43,3,9,82,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    mergeSort(arr, 0, size-1);
    std::cout<<"Sorted Array is : "<<endl;
    for(int i = 0; i<size-1; i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<endl;
    return 0;    
}