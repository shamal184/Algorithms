#include <stdio.h>

int max(int x, int y, int z){
    if (x >= y && x >= z) return x;
    else if (y >= x && y >= z) return y;
    else if (z >= x && z >= y) return z;
    else if (x == y && y == z && x == z) return x;
    else return 0;
}

int main(int argc, char const *argv[])
{
    int t;
    
    scanf("%d",&t);

    for (int x = 0; x < t; x++)
    {
        int n,k;
        scanf("%d %d",&n, &k);
        int wt[n+1];
        wt[0] = 0;
        for ( int j = 1; j < n+1; j++)
        {
            scanf("%d",&wt[j]);
        }

        int v[n+1][k+1];
        
        for (int i = 0; i <= n; i++)
        {
            for (int w = 0; w <= k; w++)
            {
                if (i == 0 || w == 0)
                {
                    v[i][w] = 0;
                }

                else if (wt[i] <= w)
                {   
                    int y;
                    
                    if (wt[i] > 0 && w % wt[i] == 0)  y = w/wt[i];
                    else y = 0;
                    v[i][w] = max(v[i-1][w], v[i-1][w-wt[i]] + wt[i], y * wt[i] );
                    //printf("%d ",v[i][w]);
                }
                 else
                 {
                     v[i][w] = v[i-1][w];
                     
                 }
                 
                
            }
            
        }

        printf("%d\n",v[n][k]);
        
    }
    

    return 0;
}
