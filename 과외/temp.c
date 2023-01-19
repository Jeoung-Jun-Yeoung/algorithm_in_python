#include <iostream>
#include <stdio.h> 
#include <queue>
#include <utility>
int main(){
	
	/*1은 4방향을 익힘 1사이클마다 4방향 봐주고 익은거 체크하고 이미 본거 빼고, 
	다음 익은거 가서 또 4방향 익히는데 모든배열 다볼때까지 */
	
	int m; 
	int n;
	int array[1001][1001] = {0,}; // 4방향 탐색을 해야하는데, -1 index에 대해 오버플로우. 
	int dir[4][2] = {{0,-1}, {0,1}, {-1,0}, {1,0}};
	int x;
	int y;
	int qsize;
	int count = 0;
	
	pair<int,int> tmp;
	
	queue<pair<int, int>> tomato;
	
	scanf("%d %d", &m ,&n);
	
	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			scanf("%d", &array[i][j];	// tomato입력받기. 1은익은 토마토 -1은 아예없고, 0은 아직 안익은 토마토 
		}
	}
	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			if(array[i][j] == 1){
				tomato.push({i,j}) // 시작점 찾아서 queue에 넣기.
			} 
		}
	}	
	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			if(array[i][j] == 0 && tomato[i][j] == -1){
				return -1;
			}
		}
	}
	
	
	while(!tomato.empty(){ // queue가 비어있을때까지 탐색. 
		count ++;
		tmp = tomato.front();
		tomato.pop();
		qsize = tomato.size();
		
		while(qsize--){ 
			
			for(int i = 0; i < 4; i++){
		
			x = tmp.first + dir[i][0];	
			y = tmp.second + dir[i][1];
		
				if(x > 0 && x <= n && y > 0 && y <= m){
					if(tomato[x][y] == 0){
					
					tomato.push(make_pair(x,y));
					tomato[x][y] == 1;
					}
				}			
			}	
		} 	
	}
	printf("%d", count);
}