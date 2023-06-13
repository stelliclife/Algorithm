#include <iostream>
#include <vector>
#include <algorithm>
#include "maze.h"

using std::cout;
using std::endl;

Maze::Maze(const int start_x, const int start_y, const vector<vector<int>> &current_map)
  : x(start_x), y(start_y), direction(kUp)
{
  map = current_map;
  result.push_back({x, y});
}

void Maze::GoForward()
{
  if (direction == kUp)
    --x;
  else if (direction == kDown)
    ++x;
  else if (direction == kLeft)
    --y;
  else if(direction == kRight)
    ++y;
  result.push_back({x, y});
}

bool Maze::IsStillInMaze()
{
  int size = (int)map[0].size();
  bool x_position_state = (x <= 0 || x >= size - 1);
  bool y_position_state = (y <= 0 || y >= size - 1);

  if (x_position_state || y_position_state)
    return false;
  return true;
}

bool Maze::EncounterWall()
{
  if (direction == kUp && map[x-1][y] == 1)
    return true;
  else if (direction == kDown && map[x+1][y] == 1)
    return true;
  else if (direction == kLeft && map[x][y-1] == 1)
    return true;
  else if (direction == kRight && map[x][y+1] == 1)
    return true;
  return false;
}

void Maze::TurnLeft()
{
  if (direction == kUp)
    direction = kLeft;
  else if (direction == kDown)
    direction = kRight;
  else if (direction == kLeft)
    direction = kDown;
  else if(direction == kRight)
    direction = kUp;
}

void Maze::TurnRight()
{
  if (direction == kUp)
    direction = kRight;
  else if (direction == kDown)
    direction = kLeft;
  else if (direction == kLeft)
    direction = kUp;
  else if(direction == kRight)
    direction = kDown;
}

void Maze::RightHandOnWall()
{
  while (IsStillInMaze())
  {
    TurnRight();
    while (EncounterWall())
      TurnLeft();
    GoForward();
  }
}

vector<vector<int>> Maze::SearchShortestPath()
{
  result.erase(unique(result.begin(), result.end()), result.end());

  return result;
}

Maze::~Maze()
{
  map.clear();
  result.clear();
}

int main()
{
  vector<vector<int>> arrMaze = \
  { { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
    { 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
    { 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1 },
    { 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1 },
    { 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
    { 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
    { 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1 },
    { 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
    { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }};
  
  Maze* maze_search = new Maze(17, 17, arrMaze);
  maze_search->RightHandOnWall();
  vector<vector<int>> path = maze_search->SearchShortestPath();
  for (int i = 0; i < (int)path.size(); ++i)
  {
    cout << path[i][0] << ", " << path[i][1] << endl;
  }
  path.clear();
  
  delete maze_search;

  return 0;
}