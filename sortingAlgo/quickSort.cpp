#include<iostream>
using namespace std;
int partition(int *arr, int start, int end){
    int pivot = arr[start];
    int pivotPosition = 0;
    for(int i = start+1; i<=end; i++){
        if(arr[i] <= pivot){
            pivotPosition++;
        }
    }
    int pivotIndex = pivotPosition+start;
    swap(arr[pivotIndex], arr[start]);
    int i = start, j = end;
    while( i < pivotIndex && j > pivotIndex){
        while(arr[i] < pivot){
            i++;
        } 
        while(arr[j] > pivot){
            j--;
        }
        if(i < pivotIndex && j > pivotIndex){
            swap(arr[i++], arr[j--]);
        }
    }
    return pivotIndex;

}
void quickSort(int *arr, int start, int end){
    if(start >= end){
        return;
    }
    int pivot = partition(arr, start, end);
    quickSort(arr, start, pivot-1);
    quickSort(arr, pivot+1, end);
}
int main(){
    int arr[] = {38,27,43,3,9,82,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    quickSort(arr, 0, size-1);
    std::cout<<"Sorted Array is : "<<endl;
    for(int i = 0; i<size-1; i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<endl;
    return 0;
}
