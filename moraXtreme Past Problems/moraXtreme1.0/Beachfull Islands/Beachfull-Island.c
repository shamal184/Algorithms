#include <stdio.h>

int main(int argc, char const *argv[])
{
    int t, m, n;
    scanf("%d",&t);
    scanf("%d %d",&m,&n);

    int map[m+2][n+2];
    char num[n+1];

    for (int i = 0; i < m+2; i++)
    {
        if ( i!=0 && i!=m+1)
        {
            num[n] = '\0';
            scanf("%s",num);    
        }
        
        for (int j = 0; j < n+2; j++)
        {
            if (j==0 || j == n+1 || i==0 || i==m+1)
            {
                map[i][j] = 0;
            }
            else
            {
                map[i][j] = num[j-1] - '0';
            }
            
        }
        
    }
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (map[i][j] == 0 && (map[i-1][j-1]==1 || map[i-1][j]==1 || map[i-1][j+1]==1 ||
            map[i][j-1]==1 || map[i][j+1]==1 || map[i+1][j-1]==1 || map[i+1][j]==1 || map[i+1][j+1]==1))
            {
                map[i][j] = 2;
            }
            
        }
        
    }
    

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            printf("%d",map[i][j]);
            
        }
        printf("\n");
    }
    return 0;
}
