#ifndef MAZE_H_
#define MAZE_H_

#include <iostream>
#include <vector>

using std::vector;

enum Direction
{
  kUp,
  kDown,
  kLeft,
  kRight,
};

class Maze
{
private: 
  int x;
  int y;
  int direction;
  vector<vector<int>> map;
  vector<vector<int>> result;

public:
  Maze(const int start_x, const int start_y, const vector<vector<int>> &current_map);
  void GoForward();
  bool IsStillInMaze();
  bool EncounterWall();
  void TurnLeft();
  void TurnRight();
  void RightHandOnWall();
  vector<vector<int>> SearchShortestPath();
  ~Maze();
};

#endif