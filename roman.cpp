#include <iostream>
#include<string.h>
using namespace std;
int main() {
	int n,arr[15],num;
	char roman[15];
	int length;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	    num = 0;
	    cin>>roman;
	    length= strlen(roman);
	    for(int j=0;j<length;j++)
	    {
	        if(roman[j]=='I')
	            arr[j]=1;
	        else if(roman[j]=='V')
	            arr[j]=5;
	        else if(roman[j]=='X')
	            arr[j]=10;
	       else if(roman[j]=='L')
	            arr[j]=50;
	       else if(roman[j]=='C')
	            arr[j]=100;
	       else if(roman[j]=='D')
	            arr[j]=500;
	       else if(roman[j]=='M')
	            arr[j]=1000;
	    }
	    int k=0;
	    while(k<length)
	    {
	        if((arr[k]<arr[k+1])&&(length!=k+1))
	        {
	            num = num + (arr[k+1]-arr[k]);
	            k+=2;
	        }
	        else
	        {
	            num += arr[k];
	            k++;
	        }
	    }
	
	    cout<<num<<"\n";        
	}
	
	
	return 0;
}