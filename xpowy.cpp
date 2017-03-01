#include <iostream>
using namespace std;

int main() {
	int n,num,x,y,check;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	    cin>>num;
	    check=2;
	    int flag=1;
	    for(x=2;x<=10;x++)
	    {
            for(y=2;y<=6;y++)
            {
                check*=x;
                if(check==num)
                {
                    flag=0;
                    break;
                }
              
            }
           
            check = x+1;
            
	    }
	    if((flag==0)||(num==1))
	        cout<<"1\n";
	   else
	        cout<<"0\n";
	    
	    
	}
	return 0;
}